# -*- coding: utf-8 -*-
"""Ansi processor.

Attributes:
    ANSI_PREFIX (str): String containing the ansi prefix characters.
    ANSI_RESET (str): String containing the ansi reset characters.

Functions:
    apply_ansi_color(text, color)
    replace_with_ansi_color(text, repl)
    escape_ansi(text)
    ansi_to_html(text)

"""


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
    """Applies an ansi color to the string received as a parameter.

    Args:
        text (str): String to modify.
        color (color): Color from the global variable 'ansi_colors' to be applied.

    Returns:
        mod_text (str): String containing the modified version of the text.

    """

    mod_text = ANSI_PREFIX + ansi_colors[color] + text + ANSI_RESET
    return mod_text


def replace_with_ansi_color(text: str, repl: dict) -> str:
    """Applies ansi colors to words in a string.

    It receives a dictionary as a parameter containing words as keys and colors as values and applies
    the colors to the words in the text specified.

    Args:
        text (str): String to modify.
        repl (dict): Dictionary containing the words and their corresponding ansi color.

    Returns:
        mod_text (str): String containing the modified version of the text.

    """

    mod_text = text
    for k, v in repl.items():
        ansi_word = apply_ansi_color(k, v)
        mod_text = re.sub(k, ansi_word, mod_text)
    return mod_text


def escape_ansi(text: str) -> str:
    """Removes ansi characters from a string.

    Args:
        text (str): String to modify.

    Returns:
        mod_text (str): String containing the modified version of the text.

    """

    ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -/]*[@-~]')
    mod_text = ansi_escape.sub('', text)
    return mod_text


def ansi_to_html(text: str) -> str:
    """Converts a string that contains ansi characters to HTML.

    Args:
        text (str): String to modify.

    Returns:
        mod_text (str): String containing the HTML code.

    """

    conv = Ansi2HTMLConverter()
    mod_text = conv.convert(text)
    return mod_text
