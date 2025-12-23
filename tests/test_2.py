import unittest, sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from main.main import is_word_valid


class TestWordChecker(unittest.TestCase):
    
    def test_sample_of_words(self):
        with open("src/dictionary.txt", "r") as r:
            all_lines = r.readlines()
            for i in range(15643, 25643):
                self.assertTrue(is_word_valid(all_lines[i].strip()))

if __name__ == '__main__':
    unittest.main()