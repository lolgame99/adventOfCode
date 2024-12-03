def get_input(file):
    values = []
    with open(file) as f:
        for line in f.readlines():
            values.append([int(x) for x in line.split(" ")])
    return values