import pathlib
import re
import os
import datetime
import json

from ansi2html import Ansi2HTMLConverter

from px3_app.tags import MifareClassic1k
from px3_app.utils import file_processor, json_processor, ansi_processor


SAVED_TAGS_DIRECTORY_PATH = pathlib.Path(__file__).absolute().parents[2] / "data" / "mf_tags"

conv = Ansi2HTMLConverter()

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

mf_tags_path = "data/mf_tags/"


def apply_ansi_color(text, color):
    ansi_pref = "\x1b["
    ansi_reset = "\x1b[0m"
    return ansi_pref + ansi_colors[color] + text + ansi_reset


def generate_error_message(message):
    output = apply_ansi_color(message, "red")
    return conv.convert(output)


def get_saved_tags() -> list:
    """
    Function that gets the saved tags in the 'mf_tags' directory.

        Returns:
            tags_list (list): list that contains the saved tags.
    """

    # dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../data/mf_tags")

    if not SAVED_TAGS_DIRECTORY_PATH.exists():
        SAVED_TAGS_DIRECTORY_PATH.mkdir(parents=True, exist_ok=True)
    json_files = [file.name for file in SAVED_TAGS_DIRECTORY_PATH.iterdir() if file.name.endswith(".json")]
    tags_list = []
    if json_files:
        for dump_json_file in json_files:
            json_file_path = SAVED_TAGS_DIRECTORY_PATH / dump_json_file
            tags_list.append(json_processor.json_to_mf_tag(json_file_path))
        tags_list.sort(key=lambda x: x.date, reverse=True)

    return tags_list


def process_command_output(command_output: str) -> str:
    """
    Function that removes and replaces unwanted characters in the output string of a proxmark command and
    converts it into HTML code.

        Parameters:
            command_output (str): the output string of the proxmark command.

        Returns:
            mod_command_output (str): string containing the HTML code of the modified command output string.
    """

    command = re.search(r'\A[^\r]*', command_output).group().strip()

    if command == "auto":
        command_output = process_auto_output(command_output)
    elif command == "hf mf autopwn":
        command_output = process_autopwn_output(command_output)

    replacements = {
        r'\r\n': r'\n',
        f'\A{command}': f"\x1b[33mCommand\x1b[0m: {command}\n\n",
        re.escape("[\x1b[1;32musb\x1b[0m]"): "",
        r'[\r]+ [🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚🕛🕜🕝🕞🕟🕠🕡🕢🕣🕤🕥🕦🕧][^\r\n]*': "",
    }
    for k, v in replacements.items():
        command_output = re.sub(k, v, command_output)

    mod_command_output = ansi_processor.ansi_to_html(command_output)

    return mod_command_output


def process_auto_output(command_output: str) -> str:
    """
    Function that checks if a pm3 file has been created and deletes it.

        Params:
            command_output (str): Output string of the auto command.

        Returns:
            mod_command_output (str): Modified command output string.
    """

    mod_command_output = command_output
    pm3_file_found = re.search(r'lf_unknown.*\.pm3', command_output)

    if pm3_file_found:
        filename = pm3_file_found.group()
        pat1 = re.escape('[\x1b[32m+\x1b[0m] saved \x1b[33m40000\x1b[0m bytes to PM3 file \x1b[33m')
        pat2 = re.escape('\x1b[0m\r')
        pattern = pat1 + f"'{filename}'" + pat2
        mod_command_output = re.sub(pattern, "", command_output)
        try:
            os.remove(filename)
        except OSError:
            pass

    return mod_command_output


def process_autopwn_output(command_output: str) -> str:
    """
    Function that checks the names of the created mf_tags and moves them to the mf_tags folder.

    Args:
        command_output (str): Output string of the autopwn command.

    Returns:
        mod_command_output (str): Modified command output string.
    """

    mod_command_output = command_output
    if re.search(r'hf-mf-', command_output):
        filenames = []
        keys_file = re.search(r'hf-mf-[^\r]*-key[^\r]*\.bin', command_output).group()
        filenames.append(keys_file)
        binary_file = re.search(r'hf-mf-[^\r]*-dump[^\r]*\.bin', command_output).group()
        filenames.append(binary_file)
        eml_file = re.search(r'hf-mf-[^\r]*-dump[^\r]*\.eml', command_output).group()
        filenames.append(eml_file)
        json_file = re.search(r'hf-mf-[^\r]*-dump[^\r]*\.json', command_output).group()
        filenames.append(json_file)

        json_processor.add_date_time_to_json_file(json_file)
        # files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../data/mf_tags")
        f = {file: file_processor.rename_and_move_tag_file(file) for file in filenames}

        # files = rename_and_move_files(filenames)
        for k, v in f.items():
            mod_command_output = re.sub(re.escape(k), v, mod_command_output)
        # mf_tag = create_mf_1k_tag_from_file(files[eml_file])
        json_file_path = SAVED_TAGS_DIRECTORY_PATH / f[json_file]
        mf_tag = json_processor.json_to_mf_tag(json_file_path)
        # mf_tag = file_processor.json_to_mf_tag(f[json_file])
        mf_tags.append(mf_tag)
        mf_tags.sort(key=lambda x: x.date, reverse=True)

    return mod_command_output


mf_tags = get_saved_tags()
