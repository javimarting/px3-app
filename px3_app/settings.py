import pathlib

current_directory = pathlib.Path(__file__).absolute()
SAVED_MF_TAGS_DIRECTORY_PATH = current_directory.parents[1] / "data" / "mf_tags"
ICONS_PATH = current_directory.parents[1] / "data" / "icons"