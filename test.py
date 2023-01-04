from server import app

import unittest
import json


class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        
    #@unittest.TestCase.order(1)
    def test_1_home(self):
        response = self.app.get('/home')
        self.assertEqual(response.status_code, 200)

   # @unittest.TestCase.order(2)
    def test_2_post_webhook(self):
        data = {"sensor":"abc","ts":"2018-11-14T13:34:49Z","in":3,"out":2}
        headers = {'Content-Type': 'application/json'}
        response = self.app.post('/api/webhook', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)

    #@unittest.TestCase.order(3)
    def test_3_get_sensor(self):
        data = {"sensor":"abc","ts":"2018-11-14T13:34:49Z","in":3,"out":2}
        headers = {'Content-Type': 'application/json'}
        self.app.post('/api/webhook', json=data, headers=headers)

        data = {"sensor":"xyz","ts":"2019-11-14T13:34:49Z","in":5,"out":2}
        headers = {'Content-Type': 'application/json'}
        self.app.post('/api/webhook', json=data, headers=headers)

        response = self.app.get('/api/sensors')
        self.assertEqual(response.status_code, 200)
        dic = json.loads(response.data.decode())
        self.assertEqual(sorted(dic['sensors']), sorted(["abc", "xyz"]))

    #@unittest.TestCase.order(4)
    def test_4_get_occupancy(self):
        for _ in range(5):
            data = {"sensor":"abc","ts":"2018-11-14T13:34:49Z","in":3,"out":2}
            headers = {'Content-Type': 'application/json'}
            self.app.post('/api/webhook', json=data, headers=headers)

            data = {"sensor":"xyz","ts":"2019-11-14T13:34:49Z","in":5,"out":2}
            headers = {'Content-Type': 'application/json'}
            self.app.post('/api/webhook', json=data, headers=headers)
        response = self.app.get('/api/sensors/abc/occupancy')
        self.assertEqual(response.status_code, 200)
        dic = json.loads(response.data.decode())
        self.assertEqual(dic['sensor'],'abc')
        self.assertEqual(dic['inside'],7)

        response = self.app.get('/api/sensors/xyz/occupancy')
        self.assertEqual(response.status_code, 200)
        dic = json.loads(response.data.decode())
        self.assertEqual(dic['sensor'],'xyz')
        self.assertEqual(dic['inside'],18)
        
    #@unittest.TestCase.order(5)
    def test_5_get_occupancy2(self):
        response = self.app.get('/api/occupancy?sensor=abc')
        self.assertEqual(response.status_code, 200)
        dic = json.loads(response.data.decode())
        self.assertEqual(dic['inside'],7)

        response = self.app.get('/api/occupancy?sensor=xyz')
        self.assertEqual(response.status_code, 200)
        dic = json.loads(response.data.decode())
        self.assertEqual(dic['inside'],18)

    def test_6_atInstant(self):
        response = self.app.get('/sensors/abc/occupancy?atInstant=2018-11-14T14:00:00')
        self.assertEqual(response.status_code, 200)
        dic = json.loads(response.data.decode())
        self.assertEqual(dic['inside'],7)

        response = self.app.get('/sensors/abc/occupancy?atInstant=2018-11-14T12:00:00')
        self.assertEqual(response.status_code, 200)
        dic = json.loads(response.data.decode())
        self.assertEqual(dic['inside'],0)
        

if __name__ == '__main__':
    unittest.main()