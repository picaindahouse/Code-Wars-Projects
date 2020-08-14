import json
def jsonattr(filepath):
    f = open(filepath, "r")
    data = json.loads(f.read())
    f.close()
    def wrapper(cls):
        for i,x in data.items():
            setattr(cls, i,x)
        return cls
    return wrapper