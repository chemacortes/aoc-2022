from util import read

if __name__ == "__main__":

    TRAINING = True
    sensors = read("data-training.txt" if TRAINING else "data.txt")


    print(sensors)