test_data1 = {
    "obj": "obj",
    "nested_once": {"first": "first"},
    "nested_twice": {
        "twice": {"inner_nest": {"second": "second"}}
    },
    "nested_thrice": {
        "thrice": {"second_nest": {"tripple_nest": {"tripple": "thrice"}, "three": "three"}}
    }
}

test_data1_results = {'obj': 'obj', 'nested_once.first': 'first', 'nested_twice.twice.inner_nest.second': 'second',
                      'nested_thrice.thrice.second_nest.tripple_nest.tripple': 'thrice', 'nested_thrice.thrice.second_nest.three': 'three'}


array_value = {
    "obj": "obj",
    "nested_once": {"first": "first"},
    "nested_twice": {
        "twice": {"inner_nest": [1, 2, 3, 4, 5]}
    }
}
array_value_result = {
    'obj': 'obj',
    'nested_once.first': 'first',
    'nested_twice.twice.inner_nest': [1, 2, 3, 4, 5]
}
