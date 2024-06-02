import unittest
from classes.many_to_many import Magazine

class TestMagazine(unittest.TestCase):

    def test_name_is_mutable_string(self):
        """magazine name is of type str and can change"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")

        assert isinstance(magazine_1.name, str)
        assert isinstance(magazine_2.name, str)

        magazine_1.name = "New Yorker"
        assert magazine_1.name == "New Yorker"

        # comment out the next line because name must be a string between 2 and 16 characters
        # magazine_2.name = 2

    def test_name_len(self):
        """magazine name is between 2 and 16 characters, inclusive"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")

        assert 2 <= len(magazine_1.name) <= 16
        assert 2 <= len(magazine_2.name) <= 16

        # comment out the next line because name must be between 2 and 16 characters
        # magazine_1.name = "New Yorker Plus X"

    def test_category_is_mutable_string(self):
        """magazine category is of type str and can change"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")

        assert isinstance(magazine_1.category, str)
        assert isinstance(magazine_2.category, str)

        magazine_1.category = "Life Style"
        assert magazine_1.category == "Life Style"

        assert isinstance(magazine_1.category, str)

        # comment out the next line because category must be a non-empty string
        # magazine_2.category = 2

    def test_category_len(self):
        """magazine category has length greater than 0"""
        magazine_1 = Magazine("Vogue", "Fashion")

        assert magazine_1.category != ""

        # comment out the next line because category must be a non-empty string
        # magazine_1.category = ""

if __name__ == '__main__':
    unittest.main()
