def get_input(file):
    obstacles = []
    guard = {}
    with open(file) as f:
        for line_idx, line in enumerate(f.readlines()):
            for char_idx, char in enumerate(line):
                if char == "#":
                    obstacles[line_idx, char_idx] = True
                elif char == ".":
                    obstacles[line_idx, char_idx] = False
                elif char == "^":
                    guard["x"] = char_idx
                    guard["y"] = line_idx
                    guard["direction"] = (0, -1)
    return obstacles, guard

print(get_input("test.txt"))