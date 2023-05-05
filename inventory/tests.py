from django.test import TestCase ,Client

class LoginTestCase(TestCase):
      def test_login(self):
        c = self.client
        response = c.post("/", {"username": "naitik", "password": "2002"})
        response = c.get("/index/")
        assert(response.status_code==302)
class LoginFailTestCase(TestCase):
      def test_login(self):
        c = self.client
        response = c.post("/", {"username": "naitik", "password": "999"})
        response = c.get("/index/")
        assert(response.status_code==302)