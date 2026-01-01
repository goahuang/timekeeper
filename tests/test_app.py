import unittest
from app import app

class FlaskTimeAppTestCase(unittest.TestCase):
    def setUp(self):
        # 設定 Flask 測試客端
        self.app = app.test_client()
        self.app.testing = True

    def test_get_time(self):
        """測試根路徑是否正確回傳日期時間"""
        response = self.app.get('/')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'success')
        self.assertIn('datetime', data)
        self.assertIn('timestamp', data)

    def test_404_error(self):
        """測試無效路徑的 404 錯誤處理"""
        response = self.app.get('/invalid-path')
        data = response.get_json()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], 'error')
        self.assertEqual(data['code'], 404)

if __name__ == '__main__':
    unittest.main()
