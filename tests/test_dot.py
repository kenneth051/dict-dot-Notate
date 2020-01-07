from unittest import TestCase
from dot_notate.dot import dict_dot_notate
from tests.test_data import test_data1,test_data1_results, test_data_with_array,test_data_with_array_result



class DotTest(TestCase):
    def test_convert_dictionary_to_dot_notation_succeds(self):
        """Test that the a nested dictionary produces a dot notation format in a new dictionary"""
        results=dict_dot_notate(test_data1)
        self.assertEqual(results,test_data1_results)
        
    def test_converts_dictionary_with_array_type_on_one_key(self):
        results=dict_dot_notate(test_data_with_array)
        self.assertEqual(results,test_data_with_array_result)
        
        