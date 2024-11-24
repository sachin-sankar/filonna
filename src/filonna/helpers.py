import re
from configparser import ConfigParser, NoSectionError
from mimetypes import guess_type
from os import listdir

from platformdirs import user_config_path
from rich import print


def sanitise_folder_title(folder_title: str) -> str:
    """Clean the folder name to only return the movie name"""

    dirty_chars = [".", "-", "(", ")", "[", "]", "{", "}", "|"]
    regex_patterns = ["(\\d+p)", "(\\d{4})"]

    for char in dirty_chars:
        folder_title = folder_title.replace(char, " ")

    for pattern in regex_patterns:
        folder_title = re.sub(pattern, "-", folder_title)

    folder_title = folder_title.split("-")[0].strip()
    return folder_title


def is_video_file(path):
    mime = guess_type(path)
    if mime[0] is None:
        return False
    if mime[0].startswith("video"):
        return True
    else:
        return False


def check_metadata_file(dir):
    """
    Check if filonna-meta.json file exists in the given dir
    """
    if "filonna-meta.json" in listdir(dir):
        return True
    else:
        return False


def get_config_file_path():
    return user_config_path(appname="Filonna", ensure_exists=True).joinpath(
        "filonna.ini"
    )


def get_config_value(section: str, key: str):
    config_file_path = get_config_file_path()
    config = ConfigParser()
    try:
        config.read(config_file_path)
        return config.get(section, key)
    except NoSectionError:
        with open(config_file_path, "w") as file:
            print(f"[green]Created config file at [blue bold]{config_file_path}[/]")
            config.add_section(section)
            config.set(section, key, "none")
            config.write(file)
        return "none"


def set_config_value(section: str, key: str, value):
    config_file_path = get_config_file_path()
    config = ConfigParser()
    config.read(config_file_path)
    config.set(section, key, value)
    with open(config_file_path, "w") as file:
        config.write(file)
