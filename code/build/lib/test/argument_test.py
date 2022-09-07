import unittest
from unittest.mock import MagicMock
from app.main import *

class TestCLI(unittest.TestCase):
     
    @classmethod
    def setUpClass(cls): 
        print('setup once')
     
    def setUp(self) -> None:        
        print('setup always')
        
    # test faalt omdat ik doorlink binnen de code... 
    # tests schrijven dus erg lastig.
    def test_for_valid_arguments(self):
        op1, arg1 = extractOperationArgument([
            '', '--name', 'Beuningen'
        ])
        
        self.assertEqual(op1, '--name')
        self.assertEqual(arg1, 'Beuningen')

    
if __name__ == '__main__':
    unittest.main()