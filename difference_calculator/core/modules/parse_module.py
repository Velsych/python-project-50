import json


def file_parser(file_path):
    a = json.load(open(file_path))
    return a


def diff_searcher(file1, file2):
    same = {}
    for key in file1.keys():
        if key in file2:
            if file1[key] == file2[key]:
                same[f"  {key}"] = file1[key]
            else:
                same[f'- {key}'] = file1[key]
                same[f"+ {key}"] = file2[key]
        else:
            same[f"- {key}"] = file1[key]
    for key in file2.keys():
        if key not in same:
            same[f"+ {key}"] = file2[key]
    return same


def generate_diff(file1, file2):
    parsed_file1 = file_parser(file1)
    parsed_file2 = file_parser(file2)
    def sort_dict(json_dict):
        final_dict = {}
        half_sorted_dict = sorted(json_dict.items())
        for k, v in half_sorted_dict:
            final_dict[k] = v
        return final_dict
    file1_sorted = sort_dict(parsed_file1)
    file2_sorted = sort_dict(parsed_file2)
    done_diffs = diff_searcher(file1_sorted, file2_sorted)
    result = "{ \n"
    for k, v in done_diffs.items():
        result += f"    {k}: {str(v)}\n"
    result += "}"
    return result