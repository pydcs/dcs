from typing import Dict, Any, Callable, Optional, List, Union


def loads(
        tablestr,
        _globals: Optional[Dict[str, Any]] = None,
        unknown_variable_lookup: Optional[Callable[[str], Any]] = None,
) -> Dict[str, Any]:

    class Parser:
        def __init__(
                self,
                buffer: str,
                _globals: Optional[Dict[str, Any]] = None,
                unknown_variable_lookup: Optional[Callable[[str], Any]] = None,
        ) -> None:
            self.buffer: str = buffer
            if _globals:
                self.variables = _globals.copy()
            else:
                self.variables = {}
            self.unknown_variable_lookup = unknown_variable_lookup

            self._variable_assignment_queue: List[str] = []

            self.buflen: int = len(buffer)
            self.pos: int = 0
            self.lineno: int = 1

            # Tracks whether we are at the global scope or in an object. The parser
            # doesn't currently handle function declarations. Variable declarations are
            # only allowed when object_depth is zero.
            self.object_depth = 0

        def parse(self):
            self.eat_ws()

            if self.eob():
                return

            c = self.char()
            if c == '{':
                return self.object()
            elif c in ('"', "'"):
                return self.string()
            elif c.isnumeric() or c in ('-', '.'):
                return self.number()
            elif c == '_':
                return self.str_function()
            elif c == ';':
                self.advance()
                return self.parse()
            else:  # varname
                self.eat_ws()

                varname = self.eatvarname()
                if varname == 'false' or varname == 'true':
                    return varname == 'true'
                elif varname == 'nil':
                    return None
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
                elif not self.object_depth:
                    # shortcut syntax without `local`
                    self.push_assigned_variable_names([varname])
                else:
                    if self.unknown_variable_lookup is None:
                        se = SyntaxError()
                        se.text = "Use of undefined variable {}".format(varname)
                        se.lineno = self.lineno
                        se.offset = self.pos
                        raise se
                    return self.unknown_variable_lookup(varname)

                self.eat_ws()
                if not self.eob() and self.char() == '=':
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
                    se.text = varname + " '" + self.char() + "'"
                    se.lineno = self.lineno
                    se.offset = self.pos
                    raise se

        def str_function(self) -> str:
            if self.char() != '_':
                se = SyntaxError()
                se.lineno = self.lineno
                se.offset = self.pos
                se.text = "Expected character '_', got '{char}'".format(char=self.char())
                raise se

            if self.advance():
                raise self.eob_exception()

            self.eat_ws()

            if self.char() != '(':
                se = SyntaxError()
                se.lineno = self.lineno
                se.offset = self.pos
                se.text = "Expected character '(', got '{char}'".format(char=self.char())
                raise se

            self.advance()
            self.eat_ws()

            s = self.string()

            self.eat_ws()

            if self.char() != ')':
                se = SyntaxError()
                se.lineno = self.lineno
                se.offset = self.pos
                se.text = "Expected character ')', got '{char}'".format(char=self.char())
                raise se

            self.pos += 1
            return s

        def string(self) -> str:
            if self.char() not in ('"', "'"):
                se = SyntaxError()
                se.lineno = self.lineno
                se.offset = self.pos
                se.text = "Expected character '\"' or \"'\", got '{char}'".format(char=self.char())
                raise se

            terminator = self.char()

            state = 0
            s = ''
            while state != 1:
                if self.advance():
                    raise self.eob_exception()

                c = self.char()
                if state == 0:
                    if c == terminator:
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
            if self.char() == '-':
                sign = -1
                if self.advance():
                    raise self.eob_exception()

            found_exponent, found_exponent_sign, found_separator = False, False, False
            while not self.eob():
                if self.char().isnumeric():
                    pass
                elif self.char() == '.':
                    if not found_separator:
                        found_separator = True
                    else:
                        raise SyntaxError()
                elif self.char().lower() == 'e':
                    if not found_exponent:
                        found_exponent = True
                    else:
                        raise SyntaxError()
                elif self.char() == '-':
                    if not found_exponent_sign:
                        found_exponent_sign = True
                    else:
                        raise SyntaxError()
                else:
                    break

                n += self.char()
                self.pos += 1

            num = float(n) * sign
            if num.is_integer():
                return int(num)
            return num

        def object(self) -> Dict[Union[int, str], Any]:
            self.object_depth += 1
            try:
                return self._object()
            finally:
                self.object_depth -= 1

        def _object(self) -> Dict[Union[int, str], Any]:
            d = {}
            if self.char() != '{':
                se = SyntaxError()
                se.lineno = self.lineno
                se.offset = self.pos
                se.text = "Expected character '{{', got '{char}'".format(char=self.char())
                raise se

            if self.advance():
                raise self.eob_exception()

            self.eat_ws()

            inc_key = 1
            while self.char() != '}':
                self.eat_ws()

                if self.char() == '[':
                    # key given
                    if self.advance():
                        raise self.eob_exception()

                    self.eat_ws()
                    key: Union[int, str]
                    if self.char() == '"':
                        key = self.string()
                    else:
                        number = self.number()
                        if isinstance(number, float):
                            se = SyntaxError()
                            se.lineno = self.lineno
                            se.offset = self.pos
                            se.text = f"Found illegal floating point index {number}"
                            raise se
                        key = number

                    if self.eob():
                        raise self.eob_exception()

                    self.eat_ws()

                    if self.char() != ']':
                        se = SyntaxError()
                        se.lineno = self.lineno
                        se.offset = self.pos
                        se.text = "Expected character ']', got '{char}'".format(char=self.char())
                        raise se

                    if self.advance():
                        raise self.eob_exception()

                    self.eat_ws()

                    if self.char() != '=':
                        se = SyntaxError()
                        se.lineno = self.lineno
                        se.offset = self.pos
                        se.text = "Expected character '=', got '{char}'".format(char=self.char())
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

                c = self.char()
                if c == '}':
                    break
                elif c in {',', ';'}:
                    if self.advance():
                        raise self.eob_exception()
                    self.eat_ws()
                else:
                    se = SyntaxError()
                    se.lineno = self.lineno
                    se.offset = self.pos
                    se.text = "Unexpected character '{char}'".format(char=self.char())
                    raise se

            self.pos += 1

            return d

        def push_assigned_variable_names(self, variable_names: List[str]):
            self._variable_assignment_queue += variable_names

        def assign_local_variable(self, value):
            self.variables[self._variable_assignment_queue.pop(0)] = value

        def eatvarname(self) -> str:
            varname = ''
            while (not self.eob()) and (self.char().isalnum() or self.char() == '_'):
                varname += self.char()
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

        def eat_line(self) -> None:
            while not self.eob() and self.char() != '\n':
                self.pos += 1

        def eat_block_comment(self) -> None:
            while not self.eob() and self.next_n_chars(2) != "]]":
                self.pos += 1
            if not self.eob():
                self.pos += 2

        def eat_ws(self):
            """
            Advances the internal buffer until it reaches a non comment or whitespace.
            :return: None
            """
            while True:
                if self.pos >= self.buflen:
                    return
                c: str = self.char()
                if c == '\n':
                    self.lineno += 1
                if self.next_n_chars(4) == "--[[":
                    self.eat_block_comment()
                    continue
                if self.next_n_chars(2) == "--":
                    self.eat_line()
                    continue
                if not c.isspace():
                    return

                self.pos += 1

        def eob(self) -> bool:
            """
            Checks if we are at the end of buffer.

            :return: True if end of buffer is reached, else False.
            """
            return self.pos >= self.buflen

        def eob_exception(self, lookahead: int = 0) -> SyntaxError:
            offset = self.pos + lookahead
            se = SyntaxError()
            se.lineno = self.lineno
            se.offset = offset
            se.text = "Unexpected end of buffer. Previous 20 characters: {}".format(
                self.buffer[offset - 20:offset]
            )
            return se

        def char(self, lookahead: int = 0) -> str:
            try:
                return self.buffer[self.pos + lookahead]
            except IndexError as ex:
                raise self.eob_exception(lookahead) from ex

        def next_n_chars(self, n: int) -> str:
            return self.buffer[self.pos:self.pos + n]

        def advance(self) -> bool:
            """
            Advances the internal buffer position by 1 and checks if we are at the end of buffer.
            :return: True if end of buffer is reached, else False.
            """
            self.pos += 1
            return self.eob()

    p = Parser(tablestr, _globals, unknown_variable_lookup)
    p.parse()
    return p.variables
