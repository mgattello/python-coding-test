class Utils:
    def __init__(self, status, content):
        self.status = status
        self.content = content

def line_difference(diff):
    diff_objects = []

    for line in diff:
        status = line[:2]
        content = line[2:].strip()
        
        if status in ('- '):
            diff_objects.append(Utils(status, content))

    return diff_objects

def convert_obj_to_dict(obj):
        return obj.__dict__ if hasattr(obj, '__dict__') else obj

def prepare_key(value):
    removeParenthesis = value.replace("(", "").replace(")", "")
    removeSlash = removeParenthesis.replace("/", "_")
    return removeSlash.replace(" ", "_")
    
def values_to_string(data):
    for k,v in list(data.items()):
        key = prepare_key(k)
        data[key] = str(v)
        del data[k]
    return data

def get_property_name(value):
    return value.split(":")[0].replace('"', '').replace('\\', '')
     