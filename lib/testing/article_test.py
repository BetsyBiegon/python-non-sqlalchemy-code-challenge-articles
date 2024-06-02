import unittest
from classes.many_to_many import Author, Magazine, Article

class TestArticle(unittest.TestCase):

    def test_title_is_immutable_str(self):
        """title is an immutable string"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")

        assert isinstance(article_1.title, str)

        # comment out the next line because title is immutable
        # article_1.title = 500

if __name__ == '__main__':
    unittest.main()
