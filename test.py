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
        self.assertEqual(api.addAPI_URL('abc', 'example.com'), None, 'Function should return nothing on success.\
        Exception on failure')
        
        #Null URL name should throw exception
        with self.assertRaises(Exception) as context:
            api.addAPI_URL('', 'example.com')
        self.assertTrue('null URL name' in context.exception)
        
        #duplicate URL name should throw exception
        with self.assertRaises(Exception) as context:
            api.addAPI_URL('abc', 'google.com')
        self.assertTrue('Duplicate URL name' in context.exception)        
        
    # Test for URL
        api2 = exoREST()
        api2.addAPI_URL('abc', 'example.com')
        
        # check for URL formatting is correct
        with self.assertRaises(Exception) as context:
            api2.addAPI_URL('def', 'example/com')
        
        # Raise exception if URL is null
        with self.assertRaises(Exception) as context:
            api2.addAPI_URL('abc', '')
        self.assertTrue('Null URL' in context.exception)
        
        # Raise warning if same URL has been added already
        with self.assertRaises(Warning) as context:
            api2.addAPI_URL('def', 'example.com')
        self.assertTrue('duplicate URL' in context.warning)

class TestSocialBot(unittest.TestCase):                
    def test_socialBot(self):
        pass
class TestMotivateU(unittest.TestCase):
    def test_MotivateU(self):
        pass
class TestMotivateU_GUI(unittest.TestCase):
    def test_gui(self):
        pass
        
if __name__ == '__main__':
    unittest.main()