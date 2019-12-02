import unittest
import gkeepapi
from QueryParser import *

class TestParseMethods(unittest.TestCase):

    def test_query_phrase_one(self):
        phrase = "TITLE Test Title TEXT The yellow bird meets the red bee BLUE TRUE"
        parser = Parser(phrase)
        self.assertEqual(parser.k.mandatoryPhrase.textPhrase, "The yellow bird meets the red bee")
        self.assertEqual(parser.k.mandatoryPhrase.titlePhrase, "Test Title")
        self.assertEqual(parser.k.optionalPhrase.pinned, True)
        self.assertEqual(parser.k.optionalPhrase.color, gkeepapi._node.ColorValue.Blue)
    
    def test_query_phrase_two(self):
        phrase = "TEXT The yellow bird meets the red bee TITLE Test Title BLUE TRUE"
        parser = Parser(phrase)
        self.assertEqual(parser.k.mandatoryPhrase.textPhrase, "The yellow bird meets the red bee")
        self.assertEqual(parser.k.mandatoryPhrase.titlePhrase, "Test Title")
        self.assertEqual(parser.k.optionalPhrase.pinned, True)
        self.assertEqual(parser.k.optionalPhrase.color, gkeepapi._node.ColorValue.Blue)        
    
    def test_query_phrase_three(self):
        phrase = "TITLE Test Title BLUE TRUE TEXT The yellow bird meets the red bee"
        parser = Parser(phrase)
        self.assertEqual(parser.k.mandatoryPhrase.textPhrase, "The yellow bird meets the red bee")
        self.assertEqual(parser.k.mandatoryPhrase.titlePhrase, "Test Title")
        self.assertEqual(parser.k.optionalPhrase.pinned, True)
        self.assertEqual(parser.k.optionalPhrase.color, gkeepapi._node.ColorValue.Blue)

    def test_query_phrase_four(self):
        phrase = "BLUE TITLE Test Title TRUE TEXT The yellow bird meets the red bee"
        parser = Parser(phrase)
        self.assertEqual(parser.k.mandatoryPhrase.textPhrase, "The yellow bird meets the red bee")
        self.assertEqual(parser.k.mandatoryPhrase.titlePhrase, "Test Title")
        self.assertEqual(parser.k.optionalPhrase.pinned, True)
        self.assertEqual(parser.k.optionalPhrase.color, gkeepapi._node.ColorValue.Blue)
        
    def test_query_phrase_five(self):
        phrase = "TRUE BLUE TITLE Test Title TEXT The yellow bird meets the red bee"
        parser = Parser(phrase)
        self.assertEqual(parser.k.mandatoryPhrase.textPhrase, "The yellow bird meets the red bee")
        self.assertEqual(parser.k.mandatoryPhrase.titlePhrase, "Test Title")
        self.assertEqual(parser.k.optionalPhrase.pinned, True)
        self.assertEqual(parser.k.optionalPhrase.color, gkeepapi._node.ColorValue.Blue)
        
    def test_query_phrase_six(self):
        phrase = "TEXT The yellow bird meets the red bee TRUE BLUE TITLE Test Title"
        parser = Parser(phrase)
        self.assertEqual(parser.k.mandatoryPhrase.textPhrase, "The yellow bird meets the red bee")
        self.assertEqual(parser.k.mandatoryPhrase.titlePhrase, "Test Title")
        self.assertEqual(parser.k.optionalPhrase.pinned, True)
        self.assertEqual(parser.k.optionalPhrase.color, gkeepapi._node.ColorValue.Blue)
        
    def test_query_phrase_seven(self):
        phrase = "BLUE TEXT The yellow bird meets the red bee TRUE TITLE Test Title"
        parser = Parser(phrase)
        self.assertEqual(parser.k.mandatoryPhrase.textPhrase, "The yellow bird meets the red bee")
        self.assertEqual(parser.k.mandatoryPhrase.titlePhrase, "Test Title")
        self.assertEqual(parser.k.optionalPhrase.pinned, True)
        self.assertEqual(parser.k.optionalPhrase.color, gkeepapi._node.ColorValue.Blue)
    
    def test_query_phrase_eight(self):
        phrase = "BLUE TEXT The yellow bird meets the red bee TITLE Test Title"
        parser = Parser(phrase)
        self.assertEqual(parser.k.mandatoryPhrase.textPhrase, "The yellow bird meets the red bee")
        self.assertEqual(parser.k.mandatoryPhrase.titlePhrase, "Test Title")
        self.assertEqual(parser.k.optionalPhrase.pinned, False)
        self.assertEqual(parser.k.optionalPhrase.color, gkeepapi._node.ColorValue.Blue)

    def test_query_phrase_nine(self):
        phrase = "TEXT The yellow bird meets the red bee TITLE Test Title"
        parser = Parser(phrase)
        self.assertEqual(parser.k.mandatoryPhrase.textPhrase, "The yellow bird meets the red bee")
        self.assertEqual(parser.k.mandatoryPhrase.titlePhrase, "Test Title")
        self.assertEqual(parser.k.optionalPhrase.pinned, False)
        self.assertEqual(parser.k.optionalPhrase.color, gkeepapi._node.ColorValue.White)

if __name__ == '__main__':
    unittest.main()