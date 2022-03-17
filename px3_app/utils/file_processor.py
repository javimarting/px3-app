import os.path
import re
import datetime
import json
import pathlib


SAVED_TAGS_DIRECTORY_PATH = pathlib.Path(__file__).absolute().parents[2] / "data" / "mf_tags"


def add_date_to_filename(filename):
    dt = datetime.datetime.now()
    formatted_dt = dt.strftime('%Y%m%d-%H%M%S')
    new_filename = f"{formatted_dt}-{filename}"
    return new_filename


def get_tag_files(file_path):
    tag_info = re.search(r'(\d+-){2}(\w+-){3}', file_path.name)


def rename_and_move_tag_file(filename):
    new_filename = add_date_to_filename(filename)
    cwd = pathlib.Path.cwd()
    file_path = cwd / filename
    new_file_path = SAVED_TAGS_DIRECTORY_PATH / new_filename
    try:
        os.rename(file_path, new_file_path)
    except OSError:
        pass
    return new_filename


def get_date_from_filename(filename: str):
    """
    Function that extracts the date from the name of a file.

    Args:
        filename (str): Name of the file.

    Returns:

    """

    pattern = r'(\d{4})(\d{2})(\d{2})-(\d{2})(\d{2})(\d{2})'
    date_time_str = re.search(pattern, filename)

    if date_time_str:
        year = int(date_time_str.group(1))
        month = int(date_time_str.group(2))
        day = int(date_time_str.group(3))
        hour = int(date_time_str.group(4))
        minute = int(date_time_str.group(5))
        second = int(date_time_str.group(6))
        date_time = datetime.datetime(year, month, day, hour, minute, second)

        return date_time


def delete_tag_files(files: dict):
    for file in files.values():
        file_path = os.path.join(SAVED_TAGS_DIRECTORY_PATH, file)
        try:
            os.remove(file_path)
        except OSError:
            pass

