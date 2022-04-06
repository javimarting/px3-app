import unittest

from px3_app.utils import ansi_processor


class TestAnsi(unittest.TestCase):
    def test_apply_ansi_color(self):
        text = "My test string"
        colored_text = ansi_processor.apply_ansi_color(text, "red")
        expected = "\x1b[31mMy test string\x1b[0m"
        self.assertEqual(colored_text, expected)

    def test_escape_ansi(self):
        text = "\x1b[31mMy test string\x1b[0m"
        esc_text = ansi_processor.escape_ansi(text)
        expected = "My test string"
        self.assertEqual(esc_text, expected)

    def test_replace_with_ansi_color(self):
        text = "Tag 1:\n    Date: 05-04-2022 20:25:09\n    UID: AD43EE01"
        replacements = {
            "Tag 1": "yellow",
            "Date": "green",
            "UID": "green",
        }
        modified_text = ansi_processor.replace_with_ansi_color(text, replacements)
        expected = "\x1b[33mTag 1\x1b[0m:\n    \x1b[32mDate\x1b[0m: 05-04-2022 20:25:09\n" \
                   "    \x1b[32mUID\x1b[0m: AD43EE01"
        self.assertEqual(modified_text, expected)


if __name__ == '__main__':
    unittest.main()
