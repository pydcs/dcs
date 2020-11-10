def dumps(value, varname=None, indent=None):
    nl = "\n" if indent else ""
    s = varname + '=' + nl if varname else ''
    indentcount = 0 if indent is None else indent

    if isinstance(value, dict):
        e = []
        for key in sorted(value.keys(), key=str):
            child = value[key]
            KNL = "\n" if indent and isinstance(child, (dict, list)) else ""
            selem = '\t' * indentcount
            skey = key if isinstance(key, int) else '"{key}"'.format(key=key)
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
        v = value.replace('\\', '\\\\')
        v = v.replace('"', '\\"')
        v = v.replace('\n', '\\\n')
        s += '"{val}"'.format(val=v)
    elif isinstance(value, bool):
        s += "true" if value else "false"
    else:
        s += str(value)

    return s
