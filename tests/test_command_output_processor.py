import unittest

from px3_app import command_output_processor


class TestCommandOutputProcessor(unittest.TestCase):
    def test_get_protocol_type(self):
        text = 'hf search\r\n\x1b[?2004l\r\r 🕐                                           \r\r 🕑  ' \
               'Searching for ThinFilm tag...\r 🕒                                           \r\r 🕓  ' \
               'Searching for LTO-CM tag...\r 🕔                                           \r\r 🕕  ' \
               'Searching for ISO14443-A tag...\r\n[\x1b[32m+\x1b[0m]  UID: \x1b[32mAD 43 EE 01 \x1b[0m\r\n' \
               '[\x1b[32m+\x1b[0m] ATQA: \x1b[32m00 04\x1b[0m\r\n[\x1b[32m+\x1b[0m]  SAK: \x1b[32m08 [2]\x1b[0m\r\n' \
               '[\x1b[32m+\x1b[0m] Possible types:\r\n[\x1b[32m+\x1b[0m]    \x1b[33mMIFARE Classic 1K\x1b[0m\r\n' \
               '[\x1b[33m=\x1b[0m] proprietary non iso14443-4 card found, RATS not supported\r\n' \
               '[\x1b[32m+\x1b[0m] Magic capabilities : \x1b[32mGen 1a\x1b[0m\r\n[\x1b[34m#\x1b[0m] 1 static nonce ' \
               '01200145\r\n[\x1b[32m+\x1b[0m] Static nonce: \x1b[33myes\x1b[0m\r\n[\x1b[34m#\x1b[0m] ' \
               'Auth error\r\n[\x1b[33m?\x1b[0m] Hint: try \x1b[33m`hf mf`\x1b[0m commands\r\n\r\n\r\n' \
               '[\x1b[32m+\x1b[0m] Valid \x1b[32mISO 14443-A tag\x1b[0m found\r\n\r\n\r ' \
               '🕖                                           \r\r 🕗  Searching for ISO15693 tag...\r ' \
               '🕘                                           \r\r 🕙  Searching for iCLASS / PicoPass tag...\r ' \
               '🕚                                           \r\r 🕛  Searching for LEGIC tag...\r ' \
               '🕐                                           \r\r 🕑  Searching for Topaz tag...\r ' \
               '🕒                                           \r\r 🕓  Searching for ISO14443-B tag...\r ' \
               '🕔                                           \r\r 🕕  Searching for FeliCa tag...\r ' \
               '🕖                                           \r\x1b[?2004h[\x1b[1;32musb\x1b[0m] '

        protocol_type = command_output_processor.get_protocol_type(text)
        expected = "ISO 14443-A tag"
        self.assertEqual(protocol_type, expected)

    def test_remove_lines(self):
        text = 'hf search\r\n\r 🕔                                           \r\r 🕕  ' \
               'Searching for ISO14443-A tag...\r\n[\x1b[32m+\x1b[0m]  UID: \x1b[32mAD 43 EE 01 \x1b[0m\r\n'
        result = command_output_processor.remove_lines(text)
        expected = ' 🕕  Searching for ISO14443-A tag...\n[\x1b[32m+\x1b[0m]  UID: \x1b[32mAD 43 EE 01 \x1b[0m\n'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
