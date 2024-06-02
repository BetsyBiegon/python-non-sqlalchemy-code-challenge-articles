#article_test.py
import unittest
from classes.many_to_many import Author, Magazine, Article

class TestArticle(unittest.TestCase):

    def test_title_is_immutable_str(self):
        """Ensure the title is an immutable string"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = Article(author, magazine, "How to wear a tutu with style")

        # Check the title is correctly set
        self.assertEqual(article.title, "How to wear a tutu with style")

        # Attempting to change the title should raise an error
        with self.assertRaises(AttributeError):
            article.title = "New Title"
