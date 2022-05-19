import unittest
import datetime
import json
import pathlib

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

    def test_add_data_to_json_file(self):
        original_data = {
            "Card": {
                "UID": "AD34DD12",
                "ATQA": "0400",
                "SAK": "08"
            }
        }
        json_file = pathlib.Path("data/simple-data.json")
        with open(json_file, "w") as f:
            json.dump(original_data, f, indent=2)
        new_data = {"Name": "Test"}
        modified_data = json_processor.add_data_to_json_file(new_data, json_file)
        expected_data = {
            "Card": {
                "UID": "AD34DD12",
                "ATQA": "0400",
                "SAK": "08"
            },
            "Name": "Test"
        }
        self.assertEqual(modified_data, expected_data)
        extra_data = {"Name": "Joe"}
        modified_extra_data = json_processor.add_data_to_json_file(extra_data, json_file)
        print(modified_extra_data)
        # json_file.unlink(missing_ok=True)


if __name__ == '__main__':
    unittest.main()
