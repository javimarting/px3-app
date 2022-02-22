import datetime
import re
import os
import json
import pandas as pd

from tags import Mifare1k


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
        memory = []
        memory_sectors = {}
        block = 0

        for i in range(64):
            memory.append([i, data['blocks'][str(i)]])

        for n in range(16):
            memory_sectors[f'{n}'] = {}
            for i in range(4):
                memory_sectors[f'{n}'][f'{i}'] = data['blocks'][f'{block}']
                block += 1
        
        memory_string = ""

        for s, b in memory_sectors.items():
            memory_string += f"\nSector {s}:\n"
            for key, value in b.items():
                memory_string += f"\t{key}: {value}\n"


        mem = pd.DataFrame(
            [data['blocks'][str(i)] for i in range(64)],
            columns=["Value"],
            index=[str(i) for i in range(64)],
        )

        json_data = {
            'uid': uid,
            'atqa': atqa,
            'sak': sak,
            'memory': mem,
        }
        # return f"UID: {uid}\nATQA: {atqa}\nSAK: {sak}"
        return json_data