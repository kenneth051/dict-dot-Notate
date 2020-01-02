def dot_notate(obj, res, currentKey):
    for k, v in obj.items():
        newKey = currentKey + "." + k if currentKey else k
        if v and isinstance(v, dict):
            objToStringDotNnotation(v,res,newKey)
        else:
            res[newKey] = v
    return res

def dict_dot_notate(obj):
    if isinstance(obj, dict):
        return dot_notate(obj, {}, currentKey=None)
    raise TypeError("function dict_dot_notate expects a dictionary")
    
