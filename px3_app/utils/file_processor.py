# -*- coding: utf-8 -*-

import datetime
import pathlib

from px3_app.utils import json_processor
from px3_app.globals import SAVED_MF_TAGS_DIRECTORY_PATH


def add_date_to_filename(filename: str) -> str:
    """Adds date to the beginning of a filename.

    Args:
        filename (str): Filename.

    Returns:
        new_filename (str): Filename with current date added to the beginning.

    """

    dt = datetime.datetime.now()
    formatted_dt = dt.strftime('%Y%m%d-%H%M%S')
    new_filename = f"{formatted_dt}-{filename}"
    return new_filename


def get_saved_mf_tags() -> list:
    """Returns the saved Mifare1k tags in the 'mf_tags' directory.

    Returns:
        tags_list (list): List containing the saved Mifare1k tags.

    """

    if not SAVED_MF_TAGS_DIRECTORY_PATH.exists():
        SAVED_MF_TAGS_DIRECTORY_PATH.mkdir(parents=True, exist_ok=True)

    tags_list = [json_processor.json_to_mf_tag(file) for file in SAVED_MF_TAGS_DIRECTORY_PATH.iterdir()
                 if file.name.endswith(".json")]

    tags_list.sort(key=lambda x: x.date, reverse=True)

    return tags_list


def rename_and_move_tag_file(filename: str):
    """Renames a file generated by the autopwn command and moves it to the mf_tags directory.

    Args:
        filename (str): Filename string.

    Returns:
        new_filename (str): Filename with the current date added to the beginning.

    """

    new_filename = add_date_to_filename(filename)
    cwd = pathlib.Path.cwd()
    file_path = cwd / filename
    new_file_path = SAVED_MF_TAGS_DIRECTORY_PATH / new_filename
    try:
        file_path.rename(new_file_path)
    except OSError:
        pass
    return new_filename


def delete_tag_files(files: dict):
    """Deletes the files of a Mifare1k saved tag.

    Args:
        files (dict): Dictionary containing the filenames.

    """

    for file in files.values():
        file_path = SAVED_MF_TAGS_DIRECTORY_PATH / file
        try:
            file_path.unlink()
        except OSError:
            pass

