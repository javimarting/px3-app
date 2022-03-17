import re

from ansi2html import Ansi2HTMLConverter

ANSI_PREFIX = "\x1b["
ANSI_RESET = "\x1b[0m"

ansi_colors = {
    "black": "30m",
    "red": "31m",
    "green": "32m",
    "yellow": "33m",
    "blue": "34m",
    "magenta": "35m",
    "cyan": "36m",
    "white": "37m",
}


def apply_ansi_color(text, color):
    return ANSI_PREFIX + ansi_colors[color] + text + ANSI_RESET


def escape_ansi(text):
    ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)


def ansi_to_html(text):
    conv = Ansi2HTMLConverter()
    return conv.convert(text)
