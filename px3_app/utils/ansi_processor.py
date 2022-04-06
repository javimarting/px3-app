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


def apply_ansi_color(text: str, color: str) -> str:
    return ANSI_PREFIX + ansi_colors[color] + text + ANSI_RESET


def replace_with_ansi_color(text: str, repl: dict):
    """Applies ansi colors to words in a string.

    It receives a dictionary containing words as keys and colors as values and applies the colors to the words in
    the text specified.

    Args:
        text (str): String to be evaluated.
        repl (dict): Dictionary containing the words and their corresponding ansi color.

    Returns:

    """

    mod_text = text

    for k, v in repl.items():
        ansi_word = apply_ansi_color(k, v)
        mod_text = re.sub(k, ansi_word, mod_text)

    return mod_text


def escape_ansi(text: str) -> str:
    ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)


def ansi_to_html(text: str) -> str:
    conv = Ansi2HTMLConverter()
    return conv.convert(text)
