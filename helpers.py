import re
from mimetypes import guess_type
from os import listdir


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
    if mime[0] == None:
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
