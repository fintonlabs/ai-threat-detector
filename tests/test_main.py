import unittest
from main import app, db, Analysis, Threat

class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_start_analysis(self):
        response = self.client.post('/start')
        self.assertEqual(response.status_code, 200)

    def test_stop_analysis(self):
        response = self.client.post('/stop')
        self.assertEqual(response.status_code, 200)

    def test_get_status(self):
        response = self.client.get('/status')
        self.assertEqual(response.status_code, 200)

    def test_get_results(self):
        response = self.client.get('/results')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()