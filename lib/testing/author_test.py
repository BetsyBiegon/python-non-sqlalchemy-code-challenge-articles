#author_test.py
import unittest
from classes.many_to_many import Author, Magazine

class TestAuthor(unittest.TestCase):

    def test_name_is_immutable_string(self):
        """Ensure author's name is an immutable string"""
        author = Author("Carry Bradshaw")

        # Check the name is a string
        self.assertIsInstance(author.name, str)
        
        # Attempting to change the name should raise an error
        with self.assertRaises(AttributeError):
            author.name = "ActuallyTopher"

    def test_topic_areas_are_unique(self):
        """Ensure topic areas are unique"""
        author = Author("Carry Bradshaw")
        magazine1 = Magazine("Vogue", "Fashion")
        magazine2 = Magazine("AD", "Architecture")

        # Adding articles to the author
        author.add_article(magazine1, "How to wear a tutu with style")
        author.add_article(magazine1, "Dating life in NYC")
        author.add_article(magazine2, "2023 Eccentric Design Trends")

        # Check unique topic areas
        self.assertEqual(len(set(author.topic_areas())), len(author.topic_areas()))
        self.assertEqual(len(author.topic_areas()), 2)
        self.assertIn("Fashion", author.topic_areas())
        self.assertIn("Architecture", author.topic_areas())

        # Ensure an author with no articles has no topic areas
        author2 = Author("Giorgio Faletti")
        self.assertEqual(author2.topic_areas(), [])
