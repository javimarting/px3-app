import datetime
import re
import os


def rename_and_move_files(filenames, new_folder):
    dt = datetime.datetime.now()
    formatted_dt = dt.strftime('%Y%m%d-%H%M%S')
    eml_file = ""
    for filename in filenames:
        new_filename = re.sub(r'hf-mf', f"hf-mf-{formatted_dt}", filename)
        os.rename(filename, os.path.join(new_folder, new_filename))
        if new_filename.endswith('eml'):
            eml_file = os.path.join(new_folder, new_filename)
    
    return eml_file
    


def analyze_result_files(string):
    if re.search(r'hf-mf-', string):
        filenames = []
        keys_file = re.search(r'hf-mf-.*-key\.bin', string).group()
        filenames.append(keys_file)
        binary_file = re.search(r'hf-mf-.*-dump\.bin', string).group()
        filenames.append(binary_file)
        text_file = re.search(r'hf-mf-.*-dump\.eml', string).group()
        filenames.append(text_file)
        json_file = re.search(r'hf-mf-.*-dump\.json', string).group()
        filenames.append(json_file)

        return rename_and_move_files(filenames, "files")
        

