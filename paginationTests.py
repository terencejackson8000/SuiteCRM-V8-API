from typing import Type
import unittest
from pagination import Pagination

# Tests for the Pagination class
class PaginationTests(unittest.TestCase):

    # Test if a default instance can be created
    def test_defaul(self):
        pagination = Pagination()
        self.assertEqual(pagination.page_number, None, "Should be None")
        self.assertEqual(pagination.page_size, 50, "Should be 50")

    # Test if only the page size is set an instance can be created
    def test_page_size_only(self):
        pagination = Pagination(100)
        self.assertEqual(pagination.page_number, None, "Should be None")
        self.assertEqual(pagination.page_size, 100, "Should be 100")
    
    # Tets for TypeError when the page size is not an int
    def test_page_size_no_int(self):
        with self.assertRaises((TypeError)):
            Pagination("-1")  
    
    # Tets for TypeError when the page number is not an int
    def test_page_number_no_int(self):
        with self.assertRaises((TypeError)):
            Pagination(99, "-1")  
    
if __name__ == '__main__':
    unittest.main()