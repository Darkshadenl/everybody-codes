import unittest
from unittest.mock import MagicMock
from 

class TestCLI(unittest.TestCase):
     
    @classmethod
    def setUpClass(cls): 
        print('setup once')
     
    def setUp(self) -> None:        
        print('setup always')
        
    def test_for_valid_arguments(self):
        self.assertEqual(1, 1)

    
if __name__ == '__main__':
    unittest.main()