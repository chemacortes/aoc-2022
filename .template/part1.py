from util import read

if __name__ == "__main__":

    TRAINING = True
    data = read("data-training.txt" if TRAINING else "data.txt")
