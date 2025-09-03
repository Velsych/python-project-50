from gendiff.core import diff_generator


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
            case diff_generator.AddChange:
                line.append(f"{get_intend(
                    initial_depth, symbol="+")}{diff.key}: {format_value(
                    diff.value, initial_depth)}")
            case diff_generator.DeleteChange:
                line.append(f"{get_intend(
                    initial_depth, symbol="-")}{diff.key}: {format_value(
                    diff.value, initial_depth)}")
            case diff_generator.Changed:
                line.append(f"{get_intend(
                    initial_depth, symbol="-")}{diff.key}: {format_value(
                    diff.old_value, initial_depth)}")
                line.append(f"{get_intend(
                    initial_depth, symbol="+")}{diff.key}: {format_value(
                    diff.value, initial_depth)}")
            case diff_generator.Stayed:
                line.append(f"{get_intend(
                    initial_depth)}{diff.key}: {format_value(
                    diff.value, initial_depth)}")
            case diff_generator.Nested:
                line.append(f"{get_intend(initial_depth)}{diff.key}: " + "{")
                line.append(formatter_stylish(diff.changes,
                                               initial_depth + 1))
                line.append(get_intend(initial_depth) + "}")
    return "\n".join(line)

