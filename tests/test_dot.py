from unittest import TestCase
from dot_notate.dot import dict_dot_notate
from tests.test_data import test_data1,test_data1_results



class DotTest(TestCase):
    def test_convert_dictionary_to_dot_notation_succeds(self):
        """Test that the a nested dictionary produces a dot notation format in a new dictionary"""
        results=dict_dot_notate(test_data1)
        self.assertEqual(results,test_data1_results)
        
    
        