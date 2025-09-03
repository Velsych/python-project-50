import json

from gendiff.core import diff_generator


def format_value(value):  
    if isinstance(value, dict):
        return value
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
                case diff_generator.AddChange: 
                    line.append({"key": diff.key,
                                "status": "added",
                                "value": format_value(diff.value)
                                })
                case diff_generator.DeleteChange:
                    line.append({"key": diff.key,
                                "status": "deleted",
                                "value": format_value(diff.value)
                                })
                case diff_generator.Changed:
                    line.append({"key": diff.key,
                                "status": "changed",
                                "old_value": format_value(diff.old_value),
                                "new_value": format_value(diff.value)
                                })
                case diff_generator.Stayed:
                    line.append({"key": diff.key,
                                "status": "stayed",
                                "value": format_value(diff.value)
                                })
                case diff_generator.Nested:
                    line.append({"key": diff.key,
                                "status": "nested",
                                "child":  actual_formatter_json(diff.changes)
                                })

        return line

    return json.dumps(actual_formatter_json(actual_diffs), indent=4) 


# Я ЭТО ТЕСТИТЬ НЕ БУДУ, Я ЗНАЮ ЧТО ОНО РАБОТАЕТ
# UPD Меня кент всё таки заставил это тестить