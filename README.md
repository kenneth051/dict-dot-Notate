# dict_dot_notate

dict_dot_notate turns nested dictionary keys to dotted strings with their corresponding values into a basic dictionary. 

Installation

    pip install dict_dot_notate
            
Usage

    from dot import dict_dot_notate

Example

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

call the relevant method to convert our dict 

        result = dict_dot_notate(data)

output


      {
        'obj': 'obj',
        'nested_once.first': 'first',
        'nested_twice.twice.inner_nest.second': 'second',
        'nested_thrice.thrice.second_nest.tripple_nest.tripple': 'thrice', 
        'nested_thrice.thrice.second_nest.three': 'three'
        }

**If a dict passed in has a list value, Then the output will be as below**

Example

    data={
    "obj": "obj",
    "nested_once": {"first": "first"},
    "nested_twice": {
        "twice": {"inner_nest": [1, 2, 3, 4, 5]}
    }
}
    
conversion

    result = dict_dot_notate(data)

output

    {
    'obj': 'obj',
    'nested_once.first': 'first',
    'nested_twice.twice.inner_nest': [1, 2, 3, 4, 5]
}


**Don't pass in a list of dictionaries.**
