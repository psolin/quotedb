import unittest
from quote import random_quote, lookup_by_quote_text, lookup_by_quote_number


class TestQuoteDB(unittest.TestCase):

    def test_random_quote(self):
        result = random_quote()
        self.assertIsInstance(result, str)
        self.assertIn("(", result)
        self.assertIn(")", result)

    def test_lookup_by_quote_text(self):
        result = lookup_by_quote_text("inspire")
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("Relevant quotes: ") or result == "No relevant quotes.")

    def test_lookup_by_quote_number(self):
        result = lookup_by_quote_number(1)
        self.assertIsInstance(result, str)
        self.assertIn("(", result)
        self.assertIn(")", result)


if __name__ == '__main__':
    unittest.main()
