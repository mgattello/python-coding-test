import difflib
import json
from src.utils import line_difference, convert_obj_to_dict, get_property_name

class IDiffLib:
    def __init__(self, object1, object2):
        self.differ = difflib.Differ()
        self.object1 = object1
        self.object2 = object2

    def get_diff(self):
        diff = []
        dict1 = convert_obj_to_dict(self.object1)
        dict2 = convert_obj_to_dict(self.object2)
        

        for key in set(dict1.keys()) | set(dict2.keys()):
            value1 = dict1.get(key)
            value2 = dict2.get(key)

            if value1 != value2:
                str1 = json.dumps({key: value1}, indent=4, sort_keys=True)
                str2 = json.dumps({key: value2}, indent=4, sort_keys=True)

                diff_objects = line_difference(self.differ.compare(str1.splitlines(True), str2.splitlines(True)))
                
                for diff_obj in diff_objects:
                    content = get_property_name(diff_obj.content)
                    diff.append(content)
        return sorted(diff)
