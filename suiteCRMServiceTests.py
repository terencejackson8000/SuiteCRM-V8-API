
from suiteCRMService import SuiteCRMService
import unittest

# Tests for the SuiteCRMService class
class SuiteCRMServiceTests(unittest.TestCase):

    # Test if an instance can be created
    # Since a token is fetched in the constructor, this will throw an Exception
    # TODO: Consider not fetching the token in the constructor
    def test_create_service(self):
        #Exception must appear as not connection can be established
        with self.assertRaises((Exception)):
            SuiteCRMService("http://test.suitecrmservice.com/", "xxx", "xxx")

    # Tets for TypeError when the host name is not set
    def test_create_service_host_none(self):
        with self.assertRaises((TypeError)):
            SuiteCRMService(None, "xxx", "xxx")
        with self.assertRaises((TypeError)):
            SuiteCRMService("", "xxx", "xxx")
    
    # Tets for TypeError when the client id is not set
    def test_create_client_id_none(self):
        with self.assertRaises((TypeError)):
            SuiteCRMService("http://test.suitecrmservice.com/", None, "xxx")
        with self.assertRaises((TypeError)):
            SuiteCRMService("http://test.suitecrmservice.com/", "", "xxx")

    # Tets for TypeError when the client secret is not set
    def test_create_client_secret_none(self):
        with self.assertRaises((TypeError)):
            SuiteCRMService("http://test.suitecrmservice.com/", "xxx", None)
        with self.assertRaises((TypeError)):
            SuiteCRMService("http://test.suitecrmservice.com/", "xxx", "")

if __name__ == '__main__':
    unittest.main()