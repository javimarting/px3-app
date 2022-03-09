import datetime
import re
import os
import json

from ansi2html import Ansi2HTMLConverter


def rename_and_move_files(filenames, new_folder):
    dt = datetime.datetime.now()
    formatted_dt = dt.strftime('%Y%m%d-%H%M%S')
    eml_file = ""
    json_file = ""
    for filename in filenames:
        new_filename = re.sub(r'hf-mf', f"hf-mf-{formatted_dt}", filename)
        os.rename(filename, os.path.join(new_folder, new_filename))
        if new_filename.endswith('eml'):
            eml_file = os.path.join(new_folder, new_filename)
        elif new_filename.endswith('json'):
            json_file = os.path.join(new_folder, new_filename)
    
    return {'eml_file': eml_file, 'json_file': json_file}


def analyze_result_files(string):
    if re.search(r'hf-mf-', string):
        filenames = []
        keys_file = re.search(r'hf-mf-.*-key.*\.bin', string).group()
        filenames.append(keys_file)
        binary_file = re.search(r'hf-mf-.*-dump.*\.bin', string).group()
        filenames.append(binary_file)
        text_file = re.search(r'hf-mf-.*-dump.*\.eml', string).group()
        filenames.append(text_file)
        json_file = re.search(r'hf-mf-.*-dump.*\.json', string).group()
        filenames.append(json_file)

        return rename_and_move_files(filenames, "files")
        

def parse_json_file(json_file):
    with open(json_file, "r") as f:
        data = json.load(f)
        uid = data['Card']['UID']
        atqa = data['Card']['ATQA']
        sak = data['Card']['SAK']
        memory_sectors = {}
        block = 0

        for n in range(16):
            memory_sectors[f'{n}'] = {}
            for i in range(4):
                memory_sectors[f'{n}'][f'{i}'] = data['blocks'][f'{block}']
                block += 1

        json_data = {
            'uid': uid,
            'atqa': atqa,
            'sak': sak,
            'memory': memory_sectors,
        }

        return json_data


def parse_result(string):
    mod_string = string

    rep = {
        "\r\r": r"\r",
        "\r\n": r"\r",
        "\x1b[?2004l": "",
        "\x1b[?2004h": "",
        "[\x1b[1;32musb\x1b[0m]": "",
    }

    rep = {re.escape(k): v for k, v in rep.items()}

    for k, v in rep.items():
        mod_string = re.sub(k, v, mod_string)

    mod_string = f"\x1b[33mCommand\x1b[0m\r {mod_string}"

    print(repr(mod_string))

    conv = Ansi2HTMLConverter()
    data = conv.convert(mod_string)
    return data


def parse_search_result(string):
    mod_string = string
    valid_tag_pattern = re.escape("Valid \x1b[32m") + r".*" + re.escape("\x1b[0m found")
    tag_found = re.search(valid_tag_pattern, mod_string)
    pm3_file_pattern = r'lf_unknown.*\.pm3'
    pm3_file_found = re.search(pm3_file_pattern, mod_string)

    if tag_found:
        mod_string = mod_string[:tag_found.end()+1]
    elif pm3_file_found:
        filename = pm3_file_found.group()
        pat1 = re.escape('[\x1b[32m+\x1b[0m] saved \x1b[33m40000\x1b[0m bytes to PM3 file \x1b[33m')
        pat2 = re.escape('\x1b[0m\r')
        pattern = pat1 + f"'{filename}'" + pat2
        mod_string = re.sub(pattern, "", mod_string)
        try:
            os.remove(filename)
        except:
            pass

    return parse_result(mod_string)

