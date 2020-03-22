import requests
import unittest

class UserTest(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:5000'

    #GET查询接口
    def test_get_case1(self):
        r = requests.get(self.base_url+'/todos')
        result = r.json()
        self.assertEqual(result['todo1']['task'],'build an API')

    def test_get_case2(self):
        r = requests.get(self.base_url+'/todos')
        result = r.json()
        self.assertEqual(result['todo2']['task'],'no error')


if __name__ == "__main__":
    unittest.main()
