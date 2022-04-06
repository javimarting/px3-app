import re
import os

from ansi2html import Ansi2HTMLConverter

from px3_app.utils import file_processor, json_processor, ansi_processor
from px3_app.settings import SAVED_MF_TAGS_DIRECTORY_PATH


conv = Ansi2HTMLConverter()


def process_command_output(command: str, command_output: str) -> str:
    """Removes and replaces unwanted characters in the output string of a proxmark command and
    converts it into HTML code.

     Parameters:
         command (str): Command executed
         command_output (str): The output string of the proxmark command.

    Returns:
        mod_command_output (str): String containing the HTML code of the modified command output string.

    """

    c = re.search(r'\A.+', command_output).group().strip()

    if command == "auto":
        command_output = process_auto_output(command_output)
    elif command == "hf mf autopwn":
        command_output = process_autopwn_output(command_output)

    replacements = {
        r'\r\n': r'\n',
        re.escape(c): f"\x1b[33mCommand\x1b[0m: {command}\n\n",
        re.escape("[\x1b[1;32musb\x1b[0m]"): "",
        r'[\r]+ [🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚🕛🕜🕝🕞🕟🕠🕡🕢🕣🕤🕥🕦🕧][^\r\n]*': "",
    }
    for k, v in replacements.items():
        command_output = re.sub(k, v, command_output)

    mod_command_output = ansi_processor.ansi_to_html(command_output)

    return mod_command_output


def process_auto_output(command_output: str) -> str:
    """Checks if a pm3 file has been created and deletes it.

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
    """Checks the names of the created mf_tags and moves them to the mf_tags folder.

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
        f = {file: file_processor.rename_and_move_tag_file(file) for file in filenames}

        for k, v in f.items():
            mod_command_output = re.sub(re.escape(k), v, mod_command_output)

        json_file_path = SAVED_MF_TAGS_DIRECTORY_PATH / f[json_file]
        mf_tag = json_processor.json_to_mf_tag(json_file_path)
        mf_tags.append(mf_tag)
        mf_tags.sort(key=lambda x: x.date, reverse=True)

    return mod_command_output


mf_tags = file_processor.get_saved_mf_tags()
