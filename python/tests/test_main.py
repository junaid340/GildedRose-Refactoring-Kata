import unittest
import sys
import io
from contextlib import redirect_stdout
from src.main import main
from approvaltests import verify

class MainTest(unittest.TestCase):
    def test_20_days(self):
        sys.argv = ["main.py", "20"] 
        result = io.StringIO()

        with redirect_stdout(result):
            main()

        verify(result.getvalue())

if __name__ == '__main__':
    unittest.main()