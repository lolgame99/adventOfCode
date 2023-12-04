input_data = [str.strip(line) for line in open("input.txt", "r").readlines()]


def puzzle1(input):
    output = []
    for line in input:
        n1 = None
        n2 = None
        for char in line:
            if char.isdigit():
                n1 = char
                break
        for char in reversed(line):
            if char.isdigit():
                n2 = char
                break
        output.append(int(n1 + n2))
        print(output)
    return sum(output)


def puzzle2():
    # Clean data
    DIGITS_ENCODING = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    encoded_inputs = []
    output = []
    for idx, line in enumerate(input_data):
        found = False
        for length in range(0, len(line)):
            for word, initial in DIGITS_ENCODING.items():
                new_substring = line[:length].replace(word, initial)
                if new_substring != line[:length]:
                    encoded_inputs.append(input_data[idx].replace(line[:length], new_substring))
                    found = True
                    break
            if found:
                break

    for idx, line in enumerate(encoded_inputs):
        found = False
        for length in range(0,len(line)):
            for word, initial in DIGITS_ENCODING.items():
                new_substring = line[length:].replace(word, initial)
                if new_substring != line[length:]:
                    output.append(encoded_inputs[idx].replace(line[length:], new_substring))
                    found = True
                    break
            if found:
                break
        if not found:
            output.append(encoded_inputs[idx])
    return puzzle1(output)

print(puzzle2())