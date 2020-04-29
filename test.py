import unittest
from src.exoAPI import exoREST


class TestAPI(unittest.TestCase):
    def test_addAPI_URL(self):
        api = exoREST()
        
        # FUNCTION SIGNATURE : addAPI_URL(self, url_name, url)
        
    # Test for URL_list
        # url_list must be a an empty dict initially
        self.assertEqual(api.url_list, {}, 'Initial url list must be empty')
        
     # Test for URL name
        # Try to add 'abc' url. It should successfully add
        self.assertEqual(api.addAPI_URL('abc', 'http://dummy.restapiexample.com/api/v1/employees'), None, 'Function should return nothing on success.\
        Exception on failure')
        
        #Null URL name should throw exception
        with self.assertRaises(Exception) as context:
            api.addAPI_URL('', 'http://dummy.restapiexample.com/api/v1/employees')
        self.assertTrue('null URL name' in context.exception)
        
        #duplicate URL name should throw exception
        with self.assertRaises(Exception) as context:
            api.addAPI_URL('abc', 'google.com')
        self.assertTrue('Duplicate URL name' in context.exception)        
        
    # Test for URL
        api2 = exoREST()
        api2.addAPI_URL('abc', 'http://dummy.restapiexample.com/api/v1/employees')
        
        # check for URL formatting is correct
        with self.assertRaises(Exception) as context:
            api2.addAPI_URL('def', 'example/com')
        
        # Raise exception if URL is null
        with self.assertRaises(Exception) as context:
            api2.addAPI_URL('abc', '')
        self.assertTrue('Null URL' in context.exception)
        
        # Raise warning if same URL has been added already
        with self.assertRaises(Warning) as context:
            api2.addAPI_URL('def', 'http://dummy.restapiexample.com/api/v1/employees')
        self.assertTrue('duplicate URL' in context.warning)
        
    def test_getURL_LIST(self):
        api = exoREST()
        
        # FUNCTION SIGNATURE : getURL_LIST(self)
        
        self.assertEqual(api.getURL_LIST(), {}, 'returns a null url_list on initial call')
        api.addAPI_URL('abc', 'http://dummy.restapiexample.com/api/v1/employees')
        self.assertEqual(api.getURL_LIST(), {'abc': 'http://dummy.restapiexample.com/api/v1/employees'},'returns proper dictionay on call')
    
    def test_getDataAsJSON(self):
        api = exoREST()
        
        # FUNCTION SIGNATURE : getDataAsJSON(self, url_name, method = 'get', outputformat = 'json')
        api.addAPI_URL('abc', 'http://dummy.restapiexample.com/api/v1/employees')
        # test with a normal url_name
        self.assertEqual( getDataAsJSON(url_name = 'abc'), None, 'Should run properly')
        self.
        # test with a non existing url_name
        
        
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