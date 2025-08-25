from difference_calculator.core.modules import (
    json_formatter,
    parse_module,
    plain,
)


def choose_styler(data, style):   # мне лениво переносить его 
    match style:                  # в отдельный модуль пусть тут лежит :Р
        case "stylish":
            line = []
            line.append("{")
            line.append(formatter_stylish(data))
            line.append("}")
            return "\n".join(line)
        case "plain":
            return plain.formatter_plain(data)
        case "json":
            return json_formatter.formatter_json(data)
        

def dictionary_formatter(dictionary_in, initial_depth):
    line = ["{"]
    for k, v in dictionary_in.items():
        if isinstance(v, dict):
            line.append(f"{get_intend(
                initial_depth)}{k}: " +
                         dictionary_formatter(v, initial_depth + 1))
        else:
            line.append(f"{get_intend(initial_depth)}{k}: {v}")
    line.append(f'{get_intend(initial_depth - 1)}' + "}")
    return "\n".join(line)


def format_value(value, initial_depth=1):
    if isinstance(value, dict):
        return dictionary_formatter(value, initial_depth + 1)
    elif isinstance(value, str):
        return value
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value)


def get_intend(depth, spaces=4, symbol=None):
    if symbol is not None:
        ready_spaces = " " * (depth * spaces - 2)
        return f'{ready_spaces}{symbol} '
    else:
        ready_spaces = " " * depth * spaces
        return f'{ready_spaces}'


def formatter_stylish(diffs, initial_depth=1):
    line = []
    for diff in diffs:
        match type(diff):
            case parse_module.AddChange:
                line.append(f"{get_intend(
                    initial_depth, symbol="+")}{diff.key}: {format_value(
                    diff.value, initial_depth)}")
            case parse_module.DeleteChange:
                line.append(f"{get_intend(
                    initial_depth, symbol="-")}{diff.key}: {format_value(
                    diff.value, initial_depth)}")
            case parse_module.Changed:
                line.append(f"{get_intend(
                    initial_depth, symbol="-")}{diff.key}: {format_value(
                    diff.old_value, initial_depth)}")
                line.append(f"{get_intend(
                    initial_depth, symbol="+")}{diff.key}: {format_value(
                    diff.value, initial_depth)}")
            case parse_module.Stayed:
                line.append(f"{get_intend(
                    initial_depth)}{diff.key}: {format_value(
                    diff.value, initial_depth)}")
            case parse_module.Nested:
                line.append(f"{get_intend(initial_depth)}{diff.key}: " + "{")
                line.append(formatter_stylish(diff.changes,
                                               initial_depth + 1))
                line.append(get_intend(initial_depth) + "}")
    return "\n".join(line)

