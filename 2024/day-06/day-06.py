def get_input(file):
    obstacles = []
    guard = {}
    with open(file) as f:
        lines = f.readlines()
        obstacles = [[False for _ in range(len(lines[0])-1)] for _ in range(len(lines))]
        for line_idx, line in enumerate(lines):
            for char_idx, char in enumerate(line.strip()):
                if char == "#":
                    obstacles[char_idx][line_idx] = True
                elif char == "^":
                    guard["position"] = (char_idx, line_idx)
                    guard["direction"] = (0, -1)
    return obstacles, guard

def next_direction(current_direction):
        return (-current_direction[1], current_direction[0])

def part1(obstacles, guard):
    print("Size:", len(obstacles[0]), len(obstacles[1]))
    visited = [[0 for _ in range(len(obstacles[0]))] for _ in range(len(obstacles))]
    next_position = (guard["position"][0] + guard["direction"][0], guard["position"][1] + guard["direction"][1])
    while 0 <= next_position[0] < len(obstacles[0]) and 0 <= next_position[1] < len(obstacles):
        visited[guard["position"][0]][guard["position"][1]] = 1
        
        if obstacles[next_position[0]][next_position[1]]:
            guard["direction"] = next_direction(guard["direction"])
        else:
            guard["position"] = next_position
        next_position = (guard["position"][0] + guard["direction"][0], guard["position"][1] + guard["direction"][1])

    print("Part 1 Solution:", sum([sum(row) for row in visited])+1)

def part2(obstacles_reset, guard_reset):
    # add single obstacle
    loops = 0

    for obstacle_x in range(len(obstacles_reset[0])):
        for obstacle_y in range(len(obstacles_reset)):
            obstacles = obstacles_reset.copy()
            guard = guard_reset.copy()
            state_history = []
            
            if obstacles[obstacle_x][obstacle_y]:
                continue
            
            obstacles[obstacle_x][obstacle_y] = True

            next_position = (guard["position"][0] + guard["direction"][0], guard["position"][1] + guard["direction"][1])
            while 0 <= next_position[0] < len(obstacles[0]) and 0 <= next_position[1] < len(obstacles):
                if (guard["position"], guard["direction"]) in state_history:
                    loops += 1
                    break

                state_history.append((guard["position"], guard["direction"]))

                if obstacles[next_position[0]][next_position[1]]:
                    guard["direction"] = next_direction(guard["direction"])
                else:
                    guard["position"] = next_position
                next_position = (guard["position"][0] + guard["direction"][0], guard["position"][1] + guard["direction"][1])


    print("Part 2 Solution:", loops)
     
part2(*get_input("test.txt"))