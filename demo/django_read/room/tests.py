from django.test import TestCase, override_settings


# Create your tests here.
class TestRoom(TestCase):
    # 这里存在一些疑惑，为什么运行测试的时候，debug默认为False
    @override_settings(DEBUG=True)
    def test_index(self):
        resp = self.client.get("/room/")
        self.assertEqual(resp.content, b"Hello")
