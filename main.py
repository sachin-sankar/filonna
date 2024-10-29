from os import listdir
from os.path import isdir


def check_subs_folder(base_path):
    """
    Check if subtitles folder exists in the movie folder if not found return the same

    Returns:
        no_subs(list): List of movie folders without subtitles folder
    """
    movie_dirs = []
    for i in listdir(base_path):
        i = f"{base_path}/{i}"
        if isdir(i):
            movie_dirs.append(i)

    no_subs = []
    for movie_dir in movie_dirs:
        if "subs" not in listdir(movie_dir):
            no_subs.append(movie_dir)
    return no_subs


def check_subs(movie_dir):
    """
    Check if subtitles exits in the given movie folder

    Returns:
        sub_paths(list): List of path to each subtitle file
    """
    subs_paths = []
    for i in listdir(movie_dir):
        if i.lower().endswith(".srt"):
            subs_paths.append(i)
    return subs_paths
