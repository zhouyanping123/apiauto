import json
import unittest
import time
import requests
#from common import tool

class test_login(unittest.TestCase):

    def setUp(self):
        self.baseapi = "http://ihr-sit.yst.com.cn/backend/"
        self.headers = {"Content-Type": "application/json"}
        globals()["token"] = None
        time.sleep(1)

    def test_1_PublicKey(self):

        self.url = self.baseapi + "public-access/getPublicKey?t=1657441924565"
        response = requests.get(self.url, headers=self.headers,verify = False)
        self.assertIn("sid",response.text)

    def test_2_postLoginSecurity(self):

        self.url = self.baseapi + "security/login?t=1657441924646"
        paramdict = {
            "username": "jliu142",
            "password": "123",
            "t":"1657441924646"
        }
        param = json.dumps(paramdict)
        response = requests.post(self.url,data=param,headers=self.headers,verify = False)
        globals()["token"] = response.text
        self.assertIsNotNone(response.text)

    def test_3_getMenus(self):
        self.url = self.baseapi + "public-access/menu/menus"
        self.headers["ihrAdminAuthorization"] = globals()["token"]
        response = requests.get(self.url, headers=self.headers,verify = False)
        self.assertIn("menuId",response.text)

















