import unittest
import gkeepapi
from QueryParser import *

class TestParseMethods(unittest.TestCase):

    def test_query_phrase_one(self):
        phrase = "DESC: Test Title TEXT: The yellow bird meets the red bee BLUE PINNED"
        parser = Parser(phrase)
        self.assertEqual(parser.k.mandatoryPhrase.textPhrase, "The yellow bird meets the red bee")
        self.assertEqual(parser.k.mandatoryPhrase.titlePhrase, "Test Title")
    
    def test_query_phrase_two(self):
        phrase = "TEXT: The yellow bird meets the red bee DESC: Test Title BLUE TRUE"
        parser = Parser(phrase)
        self.assertEqual(parser.k.mandatoryPhrase.textPhrase, "The yellow bird meets the red bee")
        self.assertEqual(parser.k.mandatoryPhrase.titlePhrase, "Test Title")
    
    def test_query_phrase_three(self):
        phrase = "DESC: Test Title BLUE TRUE TEXT: The yellow bird meets the red bee"
        parser = Parser(phrase)
        self.assertEqual(parser.k.mandatoryPhrase.textPhrase, "The yellow bird meets the red bee")
        self.assertEqual(parser.k.mandatoryPhrase.titlePhrase, "Test Title")

    def test_query_phrase_four(self):
        phrase = "BLUE DESC: Test Title TRUE TEXT: The yellow bird meets the red bee"
        parser = Parser(phrase)
        self.assertEqual(parser.k.mandatoryPhrase.textPhrase, "The yellow bird meets the red bee")
        self.assertEqual(parser.k.mandatoryPhrase.titlePhrase, "Test Title")
        
    def test_query_phrase_five(self):
        phrase = "TRUE BLUE DESC: Test Title TEXT: The yellow bird meets the red bee"
        parser = Parser(phrase)
        self.assertEqual(parser.k.mandatoryPhrase.textPhrase, "The yellow bird meets the red bee")
        self.assertEqual(parser.k.mandatoryPhrase.titlePhrase, "Test Title")
        
    def test_query_phrase_six(self):
        phrase = "TEXT: The yellow bird meets the red bee TRUE BLUE DESC: Test Title"
        parser = Parser(phrase)
        self.assertEqual(parser.k.mandatoryPhrase.textPhrase, "The yellow bird meets the red bee")
        self.assertEqual(parser.k.mandatoryPhrase.titlePhrase, "Test Title")
        
    def test_query_phrase_seven(self):
        phrase = "BLUE TEXT: The yellow bird meets the red bee TRUE DESC: Test Title"
        parser = Parser(phrase)
        self.assertEqual(parser.k.mandatoryPhrase.textPhrase, "The yellow bird meets the red bee")
        self.assertEqual(parser.k.mandatoryPhrase.titlePhrase, "Test Title")
        
if __name__ == '__main__':
    unittest.main()