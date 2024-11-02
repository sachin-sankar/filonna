import re


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
