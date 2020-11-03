import unittest
import check_if_uppercase
from unittest.mock import patch
from io import StringIO

class TestIsUppercase(unittest.TestCase):
    def test_is_uppercase(self):
        valid = check_if_uppercase.is_uppercase("off")
        self.assertEqual(valid, False)
    
    @patch("sys.stdin", StringIO("JUMP\nhelp"))  
    def test_for_upper_using_patch(self):
        valid = check_if_uppercase.is_uppercase("off")
        self.assertEqual(valid, False)

