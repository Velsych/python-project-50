import json

import yaml

from collections import namedtuple

from difference_calculator.core.modules import stylish

def file_parser(file_path):
    if file_path.endswith(".json"):
        return json.load(open(file_path))
    if file_path.endswith(".yml") or file_path.endswith(".yaml"):
        return yaml.load(open(file_path), yaml.Loader)


AddChange = namedtuple("AddChange", ["key", "value" ])  # + timeout: 20
Changed = namedtuple("Changed", ["key", "value", "old_value" ])
DeleteChange = namedtuple("Deleted", ["key","value"])
Nested = namedtuple("Nested", ["key", "changes"])
Stayed = namedtuple("Stayed",["key","value"])


    
def good_diff_searcher(old_file, new_file):
    keys = old_file.keys() | new_file.keys()  # (1,2,3)(2,3,4) = (1,2,3,4)
    
    diff_result = []
    
    for key in sorted(keys):
        if key not in old_file.keys(): # added
            added = AddChange(key, new_file[key])
            diff_result.append(added)
        elif key not in new_file.keys(): # deleted
            deleted = DeleteChange(key, old_file[key])
            diff_result.append(deleted)
        elif isinstance(old_file[key], dict) and isinstance(new_file[key], dict):
            nested_dicts = good_diff_searcher(old_file[key], new_file[key])
            nested = Nested(key, nested_dicts)
            diff_result.append(nested)
        elif old_file[key] == new_file[key]: # stayed
            stayed = Stayed(key, new_file[key])
            diff_result.append(stayed)
        else: # changed
            changed = Changed(key, new_file[key], old_file[key])
            diff_result.append(changed)
    return diff_result

def generate_diff(file1, file2,format = "plain"):
    parsed_file1 = file_parser(file1)
    parsed_file2 = file_parser(file2)
    diffs_list = good_diff_searcher(parsed_file1,parsed_file2)
    return stylish.choose_styler(diffs_list,format)
    


