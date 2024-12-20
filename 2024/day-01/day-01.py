def get_input(file):
    a = []
    b = []
    with open(file) as f:
        for line in f.readlines():
            values = line.split("   ")
            a.append(int(values[0]))
            b.append(int(values[1]))

    return a, b

a,b = get_input("input.txt")

def part1(a, b):
    print("Part 1 Solution:", sum(abs(a.pop(a.index(min(a))) - b.pop(b.index(min(b)))) for _ in range(len(a))))

def part2(a, b):
    print("Part 2 Solution:", sum(i * b.count(i) for i in a))

part1(a.copy(), b.copy())
part2(a, b)