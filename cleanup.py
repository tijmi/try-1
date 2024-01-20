import os
from os.path import exists
import shutil


def cleanup(title):
    directory = f"./assets/temp/{title}/"
    if exists(directory):
        shutil.rmtree(directory)