import unittest
from src.exoAPI import exoREST


class TestAPI(unittest.TestCase):
    def test_addAPI_URL(self):
        api = exoREST()
     
    # Test for URL_list
        # url_list must be a an empty dict initially
        self.assertEqual(api.url_list, {}, 'Initial url list must be empty')
        
     # Test for URL name
        # Try to add 'abc' url. It should successfully add
        self.assertEqual(api.addAPI_URL('abc', 'abc.com'), True, 'abc url should be added successfully')
        
        #Null URL name
        with self.assertRaises(Exception) as context:
            api.addAPI_URL('', 'abc.com')
        self.assertTrue('null URL name' in context.exception)
        
        #duplicate URL name
        with self.assertRaises(Exception) as context:
            api.addAPI_URL('abc', 'abc.com')
        self.assertTrue('Duplicate URL name' in context.exception)
        
    # Test for URL
        # check for URL formatting is correct
        
        # Raise exception if URL is null
        with self.assertRaises(Exception) as context:
            api.addAPI_URL('abc', '')
        self.assertTrue('Null URL' in context.exception)
        
    def test_socialBot(self):
        self.assertEqual(True, True)
    def test_MotivateU(self):
        self.assertEqual(True, True)
    def test_gui(self):
        self.assertEqual(True, True)
if __name__ == '__main__':
    unittest.main()