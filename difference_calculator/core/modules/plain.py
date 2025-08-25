from difference_calculator.core.modules import parse_module


def format_value(value):
    if isinstance(value, dict):
        return f"[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return f"'{str(value)}'"


def formatter_plain(diffs,diff_path=""):
    line = []
    for diff in diffs:
        match type(diff):
            case parse_module.AddChange: #ОБРАБОТЧИК И НА СЛОВАРИ ДУБИНА   #алсо, формирование строки можно запихнуть в какую нить функцию позабористее по преколу
                line.append(f"Property '{diff_path+diff.key}' was added with value: {format_value(diff.value)}")  # сюда и сюда вставить обработчик данных, что бы переводил форматы
            case parse_module.DeleteChange:
                line.append(f"Property '{diff_path+diff.key}' was removed")
            case parse_module.Changed:
                line.append(f"Property '{diff_path+diff.key}' was updated. From {format_value(diff.old_value)} to {format_value(diff.value)}")
            case parse_module.Stayed:
                pass
            case parse_module.Nested:
                line.append(formatter_plain(diff.changes, diff_path+diff.key+"."))
    return "\n".join(line)



