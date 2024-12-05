def get_input():
    input = []
    with open("input.txt") as file:
        for line in file.readlines():
            input.append(list(line))
    return input

def part1(puzzle):
    word = "XMAS"
    word_len = len(word)
    directions = [
        (0, 1),   # right
        (1, 0),   # down
        (1, 1),   # diagonal down-right
        (1, -1),  # diagonal down-left
        (0, -1),  # left
        (-1, 0),  # up
        (-1, -1), # diagonal up-left
        (-1, 1)   # diagonal up-right
    ]
    rows = len(puzzle)
    cols = len(puzzle[0])
    count = 0

    def check_direction(r, c, dr, dc):
        for i in range(word_len):
            nr, nc = r + i * dr, c + i * dc
            if not (0 <= nr < rows and 0 <= nc < cols):  # Out of bounds
                return False
            try:
                if puzzle[nr][nc] != word[i]:
                    return False
            except:
                return False  # Out of bounds
        return True
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if check_direction(r, c, dr, dc):
                    count += 1

    print("Part 1 Solution: ", count)

def part2(puzzle):
    words = ["SAM","MAS"]
    word_len = 3
    directions = [
        (1, 1),   # diagonal down-right
        (1, -1),  # diagonal down-left
        (-1, -1), # diagonal up-left
        (-1, 1)   # diagonal up-right
    ]
    rows = len(puzzle)
    cols = len(puzzle[0])
    count = 0

    def check_direction(r, c, dr, dc):
        for word in words:
            for i in range(word_len):
                nr, nc = r + i * dr, c + i * dc
                if not (0 <= nr < rows and 0 <= nc < cols):  # Out of bounds
                    return False
                try:
                    if puzzle[nr][nc] != word[i]:
                        return False
                except:
                    return False  # Out of bounds
            return True
        
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if check_direction(r, c, dr, dc):
                    #found one direction
                    if check_direction(r, c+2, dr, -dc):
                        count += 1

    print("WIP Part 2 Solution: ", count)

part1(get_input())
part2(get_input())