from dot_notate.dot_notate import dot_notate
from test_data import data

def dict_dot_notate(obj):
    if isinstance(obj, dict):
        return dot_notate(obj, {}, currentKey=None)
    raise TypeError("Function dict_dot_notate expects a dictionary")
