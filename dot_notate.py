def dot_notate(obj, res, currentKey):
    for k, v in obj.items():
        newKey = currentKey + "." + k if currentKey else k
        if v and isinstance(v, dict):
            dot_notate(v, res, newKey)
        else:
            res[newKey] = v
    return res


def dict_dot_notate(obj):
    if isinstance(obj, dict):
        return dot_notate(obj, {}, currentKey=None)
    raise TypeError("Function dict_dot_notate expects a dictionary")


data = {
    "obj": "obj",
    "nested_once": {"first": "first"},
    "nested_twice": {
        "twice": {"inner_nest": {"second": "second"}}
    },
    "nested_thrice": {
        "thrice": {"second_nest": {"tripple_nest": {"tripple": "thrice"}, "three": "three"}}
    }
}

