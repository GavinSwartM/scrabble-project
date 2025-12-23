import unittest, sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from main.main import is_word_valid


class TestWordChecker(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertTrue(is_word_valid("APPLE"))
        self.assertTrue(is_word_valid("FENCEROWS"))
        self.assertTrue(is_word_valid("HAEMIC"))
        self.assertTrue(is_word_valid("GIARDIA"))
        self.assertTrue(is_word_valid("COLLEGE"))
    
    def test_invalid_inputs(self):
        self.assertFalse(is_word_valid("QWERTZ"))
        self.assertFalse(is_word_valid("PORKAZ"))
        self.assertFalse(is_word_valid("ZOOMER"))
        self.assertFalse(is_word_valid("MIDDYS"))
        self.assertFalse(is_word_valid("ANTORA"))

    def test_invalid_input_types(self):
        self.assertFalse(is_word_valid(1))
        self.assertFalse(is_word_valid([]))
        self.assertFalse(is_word_valid(str))
        self.assertFalse(is_word_valid(unittest))
        self.assertFalse(is_word_valid(None))

    def test_auto_fails(self):
        self.assertFalse(is_word_valid(""))
        self.assertFalse(is_word_valid("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
        self.assertFalse(is_word_valid("QWERTY567"))
        self.assertFalse(is_word_valid("APPLÜE"))
        self.assertFalse(is_word_valid(str()))

    def test_capitalization(self):
        self.assertTrue(is_word_valid("turbidities"))
        self.assertTrue(is_word_valid("Carloads"))
        self.assertTrue(is_word_valid("fe"))
        self.assertFalse(is_word_valid("agyu"))
        self.assertFalse(is_word_valid("qiCkly"))

    def test_shortest_words(self):
        self.assertTrue(is_word_valid("AY"))
        self.assertTrue(is_word_valid("WO"))
        self.assertTrue(is_word_valid("AA"))
        self.assertTrue(is_word_valid("TO"))
        self.assertTrue(is_word_valid("WE"))

    def test_longest_words(self):
        self.assertTrue(is_word_valid("NEUROANATOMIES"))
        self.assertTrue(is_word_valid("GASTIGHTNESSES"))
        self.assertTrue(is_word_valid("COLLABORATIVES"))
        self.assertTrue(is_word_valid("IMPERIOUSNESSES"))
        self.assertTrue(is_word_valid("RECRYSTALLIZED"))
    
    # def test_every_valid_word(self):
    #     with open("src/dictionary.txt", "r") as r:
    #         for w in r.readlines():
    #             self.assertTrue(is_word_valid(w.strip()))

if __name__ == '__main__':
    unittest.main()