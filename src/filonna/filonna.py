from json import dump
from os import getenv, listdir, rename
from os.path import isdir
from pathlib import Path
from typing import List

import tmdbsimple as tmdb
from dotenv import load_dotenv
from helpers import is_video_file, sanitise_folder_title

load_dotenv()
tmdb.API_KEY = getenv("TMDB_API_KEY")


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


def identify_movie_dir(movie_dir: str, retries: int = 7) -> dict | None:
    """
    Identify movie from the folder name using TMDB Api and write the metadata to the folder in json format.
    """

    folder_title = movie_dir.rstrip("/").split("/")[-1]
    folder_title = sanitise_folder_title(folder_title)
    result = {}

    # Indentify using TMDB API
    search = tmdb.Search()
    for _ in range(retries):
        try:
            result = search.movie(query=folder_title)["results"][0]
            break
        except Exception:
            print(f"Retrying for {folder_title}")

    if result == {}:
        print(f"Failed for {folder_title} after {retries} retries")
        return None

    # Write metadata file
    with open(f"{movie_dir}/filonna-meta.json", "w") as file:
        dump(result, file)

    # Rename folder to the movie title
    parent = Path(movie_dir).parent.absolute()
    rename(movie_dir, f"{parent}/{result["title"]}")
    return result


def handle_strays(movie_dir: str):
    """
    Make folders for movie files with folders
    """

    # Identify Strays
    strays: List[Path] = []
    for i in listdir(movie_dir):
        i = Path(f"{movie_dir}/{i}")
        if i.is_file() and is_video_file(i):
            strays.append(i)

    # Create Folders
    base_path = Path(movie_dir)
    for stray in strays:
        folder_title = sanitise_folder_title(stray.name)
        folder_path = base_path.joinpath(folder_title)
        folder_path.mkdir()
        stray.rename(base_path.joinpath(folder_path).joinpath(stray.name))
