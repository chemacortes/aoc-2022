def read(file_input: str):
    with open(file_input) as f:
        data = [int(x.strip("\n")) for x in f if x != "\n"]
    # type: ignore
    return data
