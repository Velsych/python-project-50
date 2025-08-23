from difference_calculator.core.modules import parse_module


def choose_styler(data,style):
    match style:
        case "json":
            line = []
            line.append("{")
            line.append(formatter_json(data))
            line.append("}")
            return "\n".join(line)
        case "plain":
            return formatter_plain(data)
        

def formatter_plain(data):
    pass

def dictionary_formatter(dictionary_in,initial_depth):
    line = ["{"]
    for k,v in dictionary_in.items():
        if isinstance(v, dict):
            line.append(f"{get_intend(initial_depth)}{k}: "+ dictionary_formatter(v,initial_depth+1))
        else:
            line.append(f"{get_intend(initial_depth)}{k}: {v}")
    line.append(f'{get_intend(initial_depth-1)}'+"}")
    return "\n".join(line)


def format_value(value, initial_depth=1 ):
    if isinstance(value, dict):
        return dictionary_formatter(value,initial_depth+1)
    elif isinstance(value, str):
        return value
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value)


def get_intend(depth, spaces= 4, symbol = None):
    if not symbol is None:
        ready_spaces = " " *  (depth * spaces - 2)
        return f'{ready_spaces}{symbol} '
    else:
        ready_spaces = " " * depth * spaces
        return f'{ready_spaces}'
def formatter_json(diff = None,initial_depth = 1):
    line = []
    for object in diff:
        match type(object):
            case parse_module.AddChange:
                line.append(f"{get_intend(initial_depth,symbol="+")}{object.key}: {format_value(object.value,initial_depth)}")
            case parse_module.DeleteChange:
                line.append(f"{get_intend(initial_depth,symbol="-")}{object.key}: {format_value(object.value,initial_depth)}")
            case parse_module.Changed:
                line.append(f"{get_intend(initial_depth,symbol="-")}{object.key}: {format_value(object.old_value,initial_depth)}")
                line.append(f"{get_intend(initial_depth,symbol="+")}{object.key}: {format_value(object.value,initial_depth)}")
            case parse_module.Stayed:
                line.append(f"{get_intend(initial_depth)}{object.key}: {format_value(object.value,initial_depth)}")
            case parse_module.Nested:
                line.append(f"{get_intend(initial_depth)}{object.key}: "+"{")
                line.append(formatter_json(object.changes,initial_depth+1))
                line.append(get_intend(initial_depth)+"}")
    return "\n".join(line)

