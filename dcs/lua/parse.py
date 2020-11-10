from typing import Dict, Any, Optional, List, Union


def loads(tablestr, _globals: Optional[Dict[str, Any]] = None):

    class Parser:
        def __init__(self, buffer: str, _globals: dict = None):
            self.buffer: str = buffer
            if _globals:
                self.variables = _globals.copy()
            else:
                self.variables = {}

            self._variable_assignment_queue: List[str] = []

            self.buflen: int = len(buffer)
            self.pos: int = 0
            self.lineno: int = 1

        def parse(self):
            self.eat_ws()

            c = self.buffer[self.pos]
            if c == '{':
                return self.object()
            elif c == '"':
                return self.string()
            elif c.isnumeric() or c == '-':
                return self.number()
            elif c == '_':
                return self.str_function()
            else:  # varname
                self.eat_ws()

                varname = self.eatvarname()
                if varname == 'false' or varname == 'true':
                    return varname == 'true'
                elif varname == 'local':
                    self.eat_ws()
                    # push names for assignment into queue
                    self.push_assigned_variable_names(self.eatvarnamelist())

                elif varname == 'return':
                    self.eat_ws()

                    name = self.eatvarname()
                    return {name: self.variables[name]}
                elif varname in self.variables:
                    # substitute value from variables
                    return self.variables[varname]
                else:
                    # shortcut syntax without `local`
                    self.push_assigned_variable_names([varname])

                self.eat_ws()
                if not self.eob() and self.buffer[self.pos] == '=':
                    while True:
                        # skip comma or whitespace
                        self.advance()

                        self.eat_ws()
                        self.assign_local_variable(self.parse())

                        if self.eob():
                            return None

                        self.eat_ws()

                        if self.eob():
                            # file ended on variable declaration
                            return None
                        elif self.char() != ',':
                            # value list ended
                            break

                    return self.parse()
                else:
                    se = SyntaxError()
                    se.text = varname + " '" + self.buffer[self.pos] + "'"
                    se.lineno = self.lineno
                    se.offset = self.pos
                    raise se

        def str_function(self) -> str:
            if self.buffer[self.pos] != '_':
                se = SyntaxError()
                se.lineno = self.lineno
                se.offset = self.pos
                se.text = "Expected character '_', got '{char}'".format(char=self.buffer[self.pos])
                raise se

            if self.advance():
                raise self.eob_exception()

            self.eat_ws()

            if self.buffer[self.pos] != '(':
                se = SyntaxError()
                se.lineno = self.lineno
                se.offset = self.pos
                se.text = "Expected character '(', got '{char}'".format(char=self.buffer[self.pos])
                raise se

            self.advance()
            self.eat_ws()

            s = self.string()

            self.eat_ws()

            if self.buffer[self.pos] != ')':
                se = SyntaxError()
                se.lineno = self.lineno
                se.offset = self.pos
                se.text = "Expected character ')', got '{char}'".format(char=self.buffer[self.pos])
                raise se

            self.pos += 1
            return s

        def string(self) -> str:
            if self.buffer[self.pos] != '"':
                se = SyntaxError()
                se.lineno = self.lineno
                se.offset = self.pos
                se.text = "Expected character '\"', got '{char}'".format(char=self.buffer[self.pos])
                raise se

            state = 0
            s = ''
            while state != 1:
                if self.advance():
                    raise self.eob_exception()

                c = self.buffer[self.pos]
                if state == 0:
                    if c == '"':
                        state = 1
                        self.pos += 1
                    elif c == '\\':
                        state = 2
                    else:
                        s += c
                elif state == 2:
                    s += c
                    state = 0
            return s

        def number(self) -> Union[int, float]:
            n = ''
            sign = 1
            if self.buffer[self.pos] == '-':
                sign = -1
                if self.advance():
                    raise self.eob_exception()

            found_exponent, found_exponent_sign, found_separator = False, False, False
            while not self.eob():
                if self.buffer[self.pos].isnumeric():
                    pass
                elif self.buffer[self.pos] == '.':
                    if not found_separator:
                        found_separator = True
                    else:
                        raise SyntaxError()
                elif self.buffer[self.pos].lower() == 'e':
                    if not found_exponent:
                        found_exponent = True
                    else:
                        raise SyntaxError()
                elif self.buffer[self.pos] == '-':
                    if not found_exponent_sign:
                        found_exponent_sign = True
                    else:
                        raise SyntaxError()
                else:
                    break

                n += self.buffer[self.pos]
                self.pos += 1

            num = float(n) * sign
            if num.is_integer():
                return int(num)
            return num

        def object(self) -> Dict[Union[int, str], Any]:
            d = {}
            if self.buffer[self.pos] != '{':
                se = SyntaxError()
                se.lineno = self.lineno
                se.offset = self.pos
                se.text = "Expected character '{{', got '{char}'".format(char=self.buffer[self.pos])
                raise se

            if self.advance():
                raise self.eob_exception()

            self.eat_ws()

            inc_key = 1
            while self.buffer[self.pos] != '}':
                self.eat_ws()

                if self.buffer[self.pos] == '[':
                    # key given
                    if self.advance():
                        raise self.eob_exception()

                    self.eat_ws()
                    if self.buffer[self.pos] == '"':
                        key = self.string()
                    else:
                        key = self.number()

                    if self.eob():
                        raise self.eob_exception()

                    self.eat_ws()

                    if self.buffer[self.pos] != ']':
                        se = SyntaxError()
                        se.lineno = self.lineno
                        se.offset = self.pos
                        se.text = "Expected character ']', got '{char}'".format(char=self.buffer[self.pos])
                        raise se

                    if self.advance():
                        raise self.eob_exception()

                    self.eat_ws()

                    if self.buffer[self.pos] != '=':
                        se = SyntaxError()
                        se.lineno = self.lineno
                        se.offset = self.pos
                        se.text = "Expected character '=', got '{char}'".format(char=self.buffer[self.pos])
                        raise se

                    if self.advance():
                        raise self.eob_exception()
                else:
                    key = inc_key
                    inc_key += 1

                val = self.parse()

                self.eat_ws()

                d[key] = val
                # print(key, ':', val)

                if self.eob():
                    raise self.eob_exception()

                c = self.buffer[self.pos]
                if c == '}':
                    break
                elif c == ',':
                    if self.advance():
                        raise self.eob_exception()
                    self.eat_ws()
                else:
                    se = SyntaxError()
                    se.lineno = self.lineno
                    se.offset = self.pos
                    se.text = "Unexpected character '{char}'".format(char=self.buffer[self.pos])
                    raise se

            self.pos += 1

            return d

        def push_assigned_variable_names(self, variable_names: List[str]):
            self._variable_assignment_queue += variable_names

        def assign_local_variable(self, value):
            self.variables[self._variable_assignment_queue.pop(0)] = value

        def eatvarname(self) -> str:
            varname = ''
            while (not self.eob()) and (self.buffer[self.pos].isalnum() or self.buffer[self.pos] == '_'):
                varname += self.buffer[self.pos]
                self.pos += 1

            return varname

        def eatvarnamelist(self) -> List[str]:
            varnames = []
            while not self.eob():
                self.eat_ws()
                name = self.eatvarname()
                if len(name) > 0:
                    varnames.append(name)
                self.eat_ws()

                if self.char() == ',':
                    self.advance()
                else:
                    break

            return varnames

        def eat_comment(self):
            if (self.pos + 1 < self.buflen
                    and self.buffer[self.pos] == '-'
                    and self.buffer[self.pos + 1] == '-'):
                while not self.eob() and self.buffer[self.pos] != '\n':
                    self.pos += 1

        def eat_ws(self):
            """
            Advances the internal buffer until it reaches a non comment or whitespace.
            :return: None
            """
            self.eat_comment()
            while True:
                if self.pos >= self.buflen:
                    return
                c: str = self.buffer[self.pos]
                if c == '\n':
                    self.lineno += 1
                if c == '-':
                    self.eat_comment()
                    c = self.buffer[self.pos]
                if not c.isspace():
                    return

                self.pos += 1

        def eob(self) -> bool:
            """
            Checks if we are at the end of buffer.

            :return: True if end of buffer is reached, else False.
            """
            return self.pos >= self.buflen

        def eob_exception(self):
            se = SyntaxError()
            se.lineno = self.lineno
            se.offset = self.pos
            se.text = "Unexpected end of buffer"
            return se

        def char(self):
            return self.buffer[self.pos]

        def advance(self) -> bool:
            """
            Advances the internal buffer position by 1 and checks if we are at the end of buffer.
            :return: True if end of buffer is reached, else False.
            """
            self.pos += 1
            return self.eob()

    p = Parser(tablestr, _globals)
    p.parse()
    return p.variables
