
from gendiff.core.formatters import format_json, format_plain, format_stylish


def choose(data, style):   
    match style:                  
        case "stylish":
            line = []
            line.append("{")
            line.append(format_stylish.formatter_stylish(data))
            line.append("}")
            return "\n".join(line)
        case "plain":
            return format_plain.formatter_plain(data)
        case "json":
            return format_json.formatter_json(data)