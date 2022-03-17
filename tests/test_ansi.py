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


if __name__ == '__main__':
    unittest.main()
