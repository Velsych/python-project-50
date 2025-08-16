import json

import yaml


def file_parser(file_path):
    if file_path.endswith(".json"):
        return json.load(open(file_path))
    if file_path.endswith(".yml") or file_path.endswith(".yaml"):
        return yaml.load(open(file_path), yaml.Loader)


def sort_dict(json_dict):
    final_dict = {}
    half_sorted_dict = sorted(json_dict.items())
    for k, v in half_sorted_dict:
        if str(v) == "True" or str(v) == "False":
            v = str(v).lower()
        final_dict[k] = v
    return final_dict


def look_format(non_format_answer):
    result = "{ \n"
    for k, v in non_format_answer.items():
        result += f"    {k}: {str(v)}\n"
    result += "}"
    return result


def diff_searcher(file1, file2):
    same = {}
    sorted_dict1 = sort_dict(file1)
    sorted_dict2 = sort_dict(file2)
    for key, value in sorted_dict1.items():
        if key in sorted_dict2:
            if sorted_dict1[key] == sorted_dict2[key]:
                same[f"  {key}"] = sorted_dict1[key]
            else:
                same[f'- {key}'] = sorted_dict1[key]
                same[f"+ {key}"] = sorted_dict2[key]
        else:
            same[f"- {key}"] = sorted_dict1[key]
    for key in sorted_dict2.keys():
        if key not in same:
            same[f"+ {key}"] = sorted_dict2[key]
    return look_format(same)


def generate_diff(file1, file2):
    parsed_file1 = file_parser(file1)
    parsed_file2 = file_parser(file2)
    return diff_searcher(parsed_file1, parsed_file2)
    


