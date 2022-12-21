import os
from pathlib import Path

from util import read

if __name__ == "__main__":

    os.chdir(Path(__file__).parent)

    TRAINING = True
    data = read("data-training.txt" if TRAINING else "data.txt")
