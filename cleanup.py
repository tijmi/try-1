import os
from os.path import exists
import shutil


def cleanup(title):
    print("cleaning up ...")
    directory = f"./assets/temp/{title}/"
    if exists(directory):
        shutil.rmtree(directory)