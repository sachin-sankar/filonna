"""
Script to recreate the main movies dir structure for tests.
For internal use.
"""

from pathlib import Path

test_base = Path("/videos/test/")
mirror_base = Path("/videos/Movies/")


def replace_in_path(path: Path):
    parts = list(path.parts)
    parts[2] = "test"
    newPath = Path().joinpath(*parts)
    return newPath


def walk_dir(dir: Path):
    for i in dir.walk():
        new_dir = replace_in_path(i[0])
        new_dir.mkdir(parents=True)
        for file in i[-1]:
            path = new_dir.joinpath(file)
            path.touch()


walk_dir(mirror_base)
