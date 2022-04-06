import datetime
import re
import json

from px3_app.tags import MifareClassic1k


def date_time_encoder(dt: datetime.datetime) -> str:
    """Takes a datetime object and returns a formatted date string.

    Args:
        dt (datetime.datetime): Datetime object

    Returns:
        formatted_dt (str): Formatted date string

    """
    formatted_dt = dt.strftime('%d-%m-%Y %H:%M:%S')
    return formatted_dt


def date_time_decoder(formatted_dt: str) -> datetime.datetime:
    """Takes a formatted date string and returns a datetime object.

    Args:
        formatted_dt (str): Formatted date string.

    Returns:
        dt (datetime.datetime): Datetime object

    """

    date_time = re.search(r'(\d{2})-(\d{2})-(\d{4}) (\d{2}):(\d{2}):(\d{2})', formatted_dt)

    if date_time:
        day = int(date_time.group(1))
        month = int(date_time.group(2))
        year = int(date_time.group(3))
        hour = int(date_time.group(4))
        minute = int(date_time.group(5))
        second = int(date_time.group(6))
        dt = datetime.datetime(year, month, day, hour, minute, second)

        return dt


def add_data_to_json_file(data: dict, json_file):
    """Adds or updates fields to a json file.

    Args:
        data (dict): Dictionary containing the data.
        json_file (str): Path of the json file.

    """

    with open(json_file, 'r+') as f:
        file_data = json.load(f)
        for k, v in data.items():
            file_data[k] = v
        f.seek(0)
        json.dump(file_data, f, indent=2)


def add_date_time_to_json_file(json_file):
    dt = datetime.datetime.now()
    formatted_dt = date_time_encoder(dt)
    data = {"Date": formatted_dt}
    add_data_to_json_file(data, json_file)


def json_to_mf_tag(json_file) -> MifareClassic1k:
    """Creates a MifareClassic1k tag from a json file.

    Params:
        json_file (str): The json file path.

    Returns:
        mf_1k_tag (MifareClassic1k): MifareClassic1k object.

    """

    common = re.search(r'(\d+-){2}(\w+-){3}', json_file.name).group()
    with json_file.open() as f:
        data = json.load(f)
        date = date_time_decoder(data["Date"])
        uid = data["Card"]["UID"]
        atqa = data["Card"]["ATQA"]
        sak = data["Card"]["SAK"]
        blocks = data["blocks"]
        sector_keys = data["SectorKeys"]
        files = {
                'dump_json_file': f"{common}dump.json",
                'dump_bin_file': f"{common}dump.bin",
                'dump_eml_file': f"{common}dump.eml",
                'key_bin_file': f"{common}key.bin",
            }
        name = ""
        if "Name" in data:
            name = data["Name"]
        mf_1k_tag = MifareClassic1k(uid=uid, atqa=atqa, sak=sak, blocks=blocks, sector_keys=sector_keys,
                                        date=date, files=files, name=name)

        return mf_1k_tag
