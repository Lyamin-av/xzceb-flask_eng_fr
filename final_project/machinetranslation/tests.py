import unittest

from translator import englishToFrench, frenchToEnglish

class TestForNull(unittest.TestCase):
    def test1(self):
        self.assertIsNotNone(englishToFrench)
    def test2(self):
        self.assertIsNotNone(frenchToEnglish)    

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'),  'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish('Bonjour'),  'Hello')

unittest.main(2222)