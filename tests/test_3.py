import unittest, sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from main.main import is_word_valid


class TestWordChecker(unittest.TestCase):
    
    def test_every_valid_word(self):
        with open("src/dictionary.txt", "r") as r:
            for w in r.readlines():
                self.assertTrue(is_word_valid(w.strip()))

if __name__ == '__main__':
    unittest.main()