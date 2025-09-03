
from gendiff.core.formatters import format_stylish, json_formatter, plain


def choose(data, style):   
    match style:                  
        case "stylish":
            line = []
            line.append("{")
            line.append(format_stylish.formatter_stylish(data))
            line.append("}")
            return "\n".join(line)
        case "plain":
            return plain.formatter_plain(data)
        case "json":
            return json_formatter.formatter_json(data)