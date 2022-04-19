import pathlib

current_directory = pathlib.Path(__file__).absolute()

ROOT_DIRECTORY = current_directory.parents[1]

SAVED_MF_TAGS_DIRECTORY_PATH = ROOT_DIRECTORY / "data" / "mf_tags"

# Icons
ICONS_DIRECTORY_PATH = ROOT_DIRECTORY / "data" / "icons"

