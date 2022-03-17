import unittest
import datetime

from px3_app.utils import json_processor


class TestJsonProcessor(unittest.TestCase):
    def test_date_time_encoder(self):
        dt = datetime.datetime(2022, 3, 17, 18, 20, 0)
        formatted_dt = json_processor.date_time_encoder(dt)
        expected = "17-03-2022 18:20:00"
        self.assertEqual(formatted_dt, expected)

    def test_date_time_decoder(self):
        formatted_dt = "17-03-2022 18:20:00"
        dt = json_processor.date_time_decoder(formatted_dt)
        expected = datetime.datetime(2022, 3, 17, 18, 20, 0)
        self.assertEqual(dt, expected)


if __name__ == '__main__':
    unittest.main()
