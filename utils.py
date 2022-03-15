import re
import os
import datetime
import json

from ansi2html import Ansi2HTMLConverter

from tags import MifareClassic1k


def get_saved_tags() -> list:
    """Function that gets the saved tags in the 'files' directory.

        Returns:
            tags_list (list): list that contains the saved tags.
    """

    dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    eml_files = [file for file in os.listdir(dir_path) if file.endswith(".eml")]
    tags_list = []
    if eml_files:
        for dump_eml_file in eml_files:
            tags_list.append(get_mf_tag(dump_eml_file))
        tags_list.sort(key=lambda x: x.date, reverse=True)

    return tags_list


def get_mf_tag(eml_file: str) -> MifareClassic1k:
    """Function that creates a MifareClassic1k tag from an eml file.

        Params:
            dump_eml_file (str): the eml file path.

        Returns:
            mf_1k_tag (MifareClassic1k): MifareClassic1k object.
    """

    pattern = r'\d+-\d+-\w+'
    file_info = re.search(pattern, eml_file).group()
    dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
    dump_eml_file = os.path.join(dir_path, eml_file)
    dump_bin_file = os.path.join(dir_path, f"hf-mf-{file_info}-dump.bin")
    dump_json_file = os.path.join(dir_path, f"hf-mf-{file_info}-dump.json")
    key_bin_file = os.path.join(dir_path, f"hf-mf-{file_info}-key.bin")
    files = {
        'dump_bin_file': dump_bin_file,
        'dump_eml_file': dump_eml_file,
        'dump_json_file': dump_json_file,
        'key_bin_file': key_bin_file,
    }
    year = int(file_info[:4])
    month = int(file_info[4:6])
    day = int(file_info[6:8])
    hour = int(file_info[9:11])
    minute = int(file_info[11:13])
    second = int(file_info[13:15])
    date = datetime.datetime(year, month, day, hour, minute, second)
    uid = ""
    atqa = ""
    sak = ""
    blocks = {}
    sector_keys = {}
    with open(dump_json_file, "r") as f:
        data = json.load(f)
        uid = data["Card"]["UID"]
        atqa = data["Card"]["ATQA"]
        sak = data["Card"]["SAK"]
        blocks = data["blocks"]
        sector_keys = data["SectorKeys"]

    mf_1k_tag = MifareClassic1k(uid=uid, atqa=atqa, sak=sak, blocks=blocks, sector_keys=sector_keys,
                                date=date, files=files)

    return mf_1k_tag


def rename_and_move_files(filenames, new_folder):
    dt = datetime.datetime.now()
    formatted_dt = dt.strftime('%Y%m%d-%H%M%S')
    files = {}
    for filename in filenames:
        new_filename = re.sub(r'hf-mf', f"hf-mf-{formatted_dt}", filename)
        os.rename(filename, os.path.join(new_folder, new_filename))
        files[filename] = new_filename
    return files


def clean_search_output(command_output: str):
    pattern = r' [🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚🕛🕜🕝🕞🕟🕠🕡🕢🕣🕤🕥🕦🕧][^\r]*[\r]'
    mod_output = re.sub(pattern, "", command_output)
    mod_output = re.sub(r"\r+", r"\r", mod_output)
    mod_output = re.sub(r"\r\n", r"\r", mod_output)

    return mod_output


def parse_command_output(command_output: str) -> str:
    """Function that removes and replaces unwanted characters in the output string of a proxmark command.

        Parameters:
            command_output (str): the output string of the proxmark command.

        Returns:
            mod_command_output (str): string containing the HTML code of the modified command output.
    """

    replacements = {
        "\x1b[?2004l": "",
        "\x1b[?2004h": "",
        "[\x1b[1;32musb\x1b[0m]": "",
    }
    for k, v in replacements.items():
        command_output = re.sub(re.escape(k), v, command_output)
    command_output = f"\x1b[33mCommand\x1b[0m: {command_output}"
    conv = Ansi2HTMLConverter()
    mod_command_output = conv.convert(command_output)
    return mod_command_output


def parse_result(command_output):
    mod_string = clean_search_output(command_output)
    mod_string = parse_command_output(mod_string)
    return mod_string


def parse_search_result(command_output: str) -> str:
    """Function that checks if a valid tag has been found by searching for a pattern in the
    output string of the proxmark search command (auto, lf search and hf search).

    """

    mod_string = clean_search_output(command_output)
    pm3_file_pattern = r'lf_unknown.*\.pm3'
    pm3_file_found = re.search(pm3_file_pattern, mod_string)

    if pm3_file_found:
        filename = pm3_file_found.group()
        pat1 = re.escape('[\x1b[32m+\x1b[0m] saved \x1b[33m40000\x1b[0m bytes to PM3 file \x1b[33m')
        pat2 = re.escape('\x1b[0m\r')
        pattern = pat1 + f"'{filename}'" + pat2
        mod_string = re.sub(pattern, "", mod_string)
        try:
            os.remove(filename)
        except:
            pass

    return parse_command_output(mod_string)


def parse_autopwn_result(command_output):
    mod_string = clean_search_output(command_output)
    if re.search(r'hf-mf-', mod_string):
        filenames = []
        keys_file = re.search(r'hf-mf-[^\r]*-key[^\r]*\.bin', mod_string).group()
        filenames.append(keys_file)
        binary_file = re.search(r'hf-mf-[^\r]*-dump[^\r]*\.bin', mod_string).group()
        filenames.append(binary_file)
        eml_file = re.search(r'hf-mf-[^\r]*-dump[^\r]*\.eml', mod_string).group()
        filenames.append(eml_file)
        json_file = re.search(r'hf-mf-[^\r]*-dump[^\r]*\.json', mod_string).group()
        filenames.append(json_file)
        files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
        files = rename_and_move_files(filenames, files_path)
        for k, v in files.items():
            mod_string = re.sub(k, v, mod_string)
        mf_tag = get_mf_tag(files[eml_file])
        mf_tags.append(mf_tag)
        mf_tags.sort(key=lambda x: x.date, reverse=True)

    return parse_command_output(mod_string)


mf_tags = get_saved_tags()
