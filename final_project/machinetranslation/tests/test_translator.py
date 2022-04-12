import unittest
from translator import translator

class TestTranslatorMethods(unittest.TestCase):

    def test_english_to_french(self):

        to_frensh = translator.english_to_french('Hello')
        translation = to_frensh['translations'][0]['translation']

        self.assertIsNotNone(translation)
        self.assertEqual(translation, 'Bonjour')

    def test_french_to_english(self):

        to_english = translator.french_to_english('Bonjour')
        translation = to_english['translations'][0]['translation']

        self.assertIsNotNone(translation)
        self.assertEqual(translation, 'Hello')


if __name__ == '__main__':
    unittest.main()
