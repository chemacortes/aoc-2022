def read(file_input: str):
    with open(file_input) as f:
        data = f.read().split("\n")

    return [line for line in data if line]
