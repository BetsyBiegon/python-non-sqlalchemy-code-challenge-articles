import unittest
from classes.many_to_many import Author, Magazine

class TestAuthor(unittest.TestCase):

    def test_name_is_immutable_string(self):
        """author name is of type str and cannot change"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")

        assert isinstance(author_1.name, str)
        assert isinstance(author_2.name, str)

        # comment out the next line because name is immutable
        # author_1.name = "ActuallyTopher"

    def test_topic_areas_are_unique(self):
        """topic areas are unique"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Giorgio Faletti")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        author_1.add_article(magazine_1, "How to wear a tutu with style")
        author_1.add_article(magazine_1, "Dating life in NYC")
        author_1.add_article(magazine_2, "2023 Eccentric Design Trends")

        assert len(set(author_1.topic_areas())) == len(author_1.topic_areas())
        assert len(author_1.topic_areas()) == 2
        assert "Fashion" in author_1.topic_areas()
        assert "Architecture" in author_1.topic_areas()
        assert author_2.topic_areas() == []

if __name__ == '__main__':
    unittest.main()
