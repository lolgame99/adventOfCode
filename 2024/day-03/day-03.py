import re
def get_input(file):
    with open(file) as f:
        return f.read()

memory = get_input("input.txt")
#memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))mul(8,5))don't()mul(811,5)do()test"

def part1(memory):
    print("Part 1 Solution: ", sum([int(values.split(",")[0]) * int(values.split(",")[1]) for values in [op.replace("mul(","").replace(")","") for op in re.findall("mul\(\d{1,3},\d{1,3}\)", memory)]]))

def part2(memory):
    print("Part 2 Solution: ", sum([int(values.split(",")[0]) * int(values.split(",")[1]) for values in [op.replace("mul(","").replace(")","") for op in re.findall("mul\(\d{1,3},\d{1,3}\)", re.sub("don't\(\).*?do\(\)","", memory, flags=re.DOTALL))]]))

part1(memory)
part2(memory)