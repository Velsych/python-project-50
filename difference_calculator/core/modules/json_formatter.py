import json

from difference_calculator.core.modules import parse_module


def format_value(value):  
    if isinstance(value, dict):
        pass
    elif isinstance(value, str):
        return value
    elif value is None:
        return None
    elif isinstance(value, bool):
        return value
    else:
        return str(value)


def formatter_json(actual_diffs): 

    def actual_formatter_json(diffs): 
        line = []
        for diff in diffs:
            match type(diff):
                case parse_module.AddChange: 
                    line.append({"key": diff.key,
                                "status": "added",
                                "value": format_value(diff.value)
                                })
                case parse_module.DeleteChange:
                    line.append({"key": diff.key,
                                "status": "deleted",
                                "value": format_value(diff.value)
                                })
                case parse_module.Changed:
                    line.append({"key": diff.key,
                                "status": "changed",
                                "old_value": format_value(diff.old_value),
                                "new_value": format_value(diff.value)
                                })
                case parse_module.Stayed:
                    line.append({"key": diff.key,
                                "status": "stayed",
                                "value": format_value(diff.value)
                                })
                case parse_module.Nested:
                    line.append({"key": diff.key,
                                "status": "nested",
                                "child":  actual_formatter_json(diff.changes)
                                })

        return line

    return json.dumps(actual_formatter_json(actual_diffs), indent=4) 


# Я ЭТО ТЕСТИТЬ НЕ БУДУ, Я ЗНАЮ ЧТО ОНО РАБОТАЕТ
# UPD Меня кент всё таки заставил это тестить