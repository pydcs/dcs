import math


def _quote(value: str) -> str:
    v = value.replace('\\', '\\\\')
    v = v.replace('"', '\\"')
    v = v.replace('\n', '\\\n')
    # a raw carriage return inside a quoted string is a syntax error in lua
    v = v.replace('\r', '\\r')
    return '"{val}"'.format(val=v)


def dumps(value, varname=None, indent=None):
    nl = "\n" if indent else ""
    s = varname + '=' + nl if varname else ''
    indentcount = 0 if indent is None else indent

    if isinstance(value, dict):
        e = []
        areAllKeysInts = all(isinstance(k, int) for k in value.keys())
        dictionaryKeys = value.keys() if areAllKeysInts else sorted(value.keys(), key=str)
        for key in dictionaryKeys:
            child = value[key]
            KNL = "\n" if indent and isinstance(child, (dict, list)) else ""
            selem = '\t' * indentcount
            skey = key if isinstance(key, int) else _quote(str(key))
            selem += '[{key}]={nl}'.format(key=skey, nl=KNL)
            selem += dumps(value[key], indent=indent + 1 if indent else None)
            e.append(selem)
        s += '\t' * (indent - 1) if nl else ""
        s += "{"
        if e:
            s += nl + ",{nl}".format(nl=nl).join(e)
        s += nl + '\t' * (indentcount - 1) + "}"
    elif isinstance(value, list):
        e = []
        i = 1
        for v in value:
            selem = '\t' * indentcount + "[{i}]=".format(i=i)
            selem += dumps(v, indent=indent + 1 if indent else None)
            e.append(selem)
            i += 1
        s += '\t' * (indent - 1) if nl else ""
        s += "{"
        if e:
            s += nl + ",{nl}".format(nl=nl).join(e)
        s += nl + '\t' * (indentcount - 1) + "}"
    elif isinstance(value, str):
        s += _quote(value)
    elif isinstance(value, bool):
        s += "true" if value else "false"
    elif value is None:
        s += "nil"
    elif isinstance(value, float) and not math.isfinite(value):
        # Lua has no literal for these: an overflowing number reads back as infinity, nan can't be expressed
        if math.isnan(value):
            raise ValueError("NaN can not be serialized to lua")
        s += "1e309" if value > 0 else "-1e309"
    else:
        s += str(value)

    return s
