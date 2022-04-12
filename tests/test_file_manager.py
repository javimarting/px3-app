import unittest
import datetime
import pathlib

from px3_app.utils import file_manager


class TestFileProcessor(unittest.TestCase):
    def test_add_date_to_filename(self):
        file_path = "data/hf-mf-AD34DD12-dump.json"
        pathlib.Path(file_path).touch()
        dt = datetime.datetime(2022, 4, 12, 13, 57, 24)
        new_file_path = file_manager.add_date_to_filename(pathlib.Path(file_path), dt)
        expected = pathlib.Path("data/20220412-135724-hf-mf-AD34DD12-dump.json")
        self.assertEqual(new_file_path, expected)
        new_file_path.unlink(missing_ok=True)


if __name__ == '__main__':
    unittest.main()
