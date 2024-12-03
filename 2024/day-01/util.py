def get_input(file):
    a = []
    b = []
    with open(file) as f:
        for line in f.readlines():
            values = line.split("   ")
            a.append(int(values[0]))
            b.append(int(values[1]))

    return a, b