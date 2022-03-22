import datetime
import pathlib

from px3_app.utils import json_processor


from px3_app.settings import SAVED_MF_TAGS_DIRECTORY_PATH


def add_date_to_filename(filename):
    dt = datetime.datetime.now()
    formatted_dt = dt.strftime('%Y%m%d-%H%M%S')
    new_filename = f"{formatted_dt}-{filename}"
    return new_filename


def get_saved_tags() -> list:
    """
    Function that gets the saved tags in the 'mf_tags' directory.

        Returns:
            tags_list (list): list containing the saved tags.
    """

    if not SAVED_MF_TAGS_DIRECTORY_PATH.exists():
        SAVED_MF_TAGS_DIRECTORY_PATH.mkdir(parents=True, exist_ok=True)

    tags_list = [json_processor.json_to_mf_tag(file) for file in SAVED_MF_TAGS_DIRECTORY_PATH.iterdir()
                 if file.name.endswith(".json")]

    tags_list.sort(key=lambda x: x.date, reverse=True)

    return tags_list


def rename_and_move_tag_file(filename):
    new_filename = add_date_to_filename(filename)
    cwd = pathlib.Path.cwd()
    file_path = cwd / filename
    new_file_path = SAVED_MF_TAGS_DIRECTORY_PATH / new_filename
    try:
        # os.rename(file_path, new_file_path)
        file_path.rename(new_file_path)
    except OSError:
        pass
    return new_filename


def delete_tag_files(files: dict):
    for file in files.values():
        # file_path = os.path.join(SAVED_TAGS_DIRECTORY_PATH, file)
        file_path = SAVED_MF_TAGS_DIRECTORY_PATH / file
        try:
            file_path.unlink()
        except OSError:
            pass

