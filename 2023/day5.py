from itertools import pairwise

def parse_input():
    input_data = [str.strip(line) for line in open("input.txt", "r").readlines()]
    while "" in input_data:
        input_data.remove("")

    seeds = [int(number) for number in input_data[0].replace("seeds: ","").split(" ")]
    mapping_dict = {}
    current_map_index = -1
    for line in input_data[1:]:
        if "map" in line:
            current_map_index += 1
            mapping_dict[current_map_index] = []
            continue
        destination_range_start, source_range_start, range_length = [int(number) for number in line.split(" ")]
        difference = destination_range_start - source_range_start
        mapping_dict[current_map_index].append([source_range_start, destination_range_start, range_length, difference])
    print("Successfully parsed input data!")
    return seeds, mapping_dict


def apply_mapping(current_mapping_index, mapping_dict, sources):
    if current_mapping_index not in mapping_dict:
        return sources
    mapped_sources = []
    for source in sources:
        found = False
        for mapping in mapping_dict[current_mapping_index]:
            source_range_start, destination_range_start, range_length, difference = mapping
            if source in range(source_range_start, source_range_start + range_length):
                mapped_sources.append(source + difference)
                found = True
                continue
        if not found:
            mapped_sources.append(source)
    print(f"Finished mapping {current_mapping_index}!")
    return apply_mapping(current_mapping_index + 1, mapping_dict, mapped_sources)


def explode_initial_seeds(seeds):
    exploded_seeds = []
    skip = True
    for start_seed, length in pairwise(seeds):
        skip = not skip
        if skip:
            continue
        for new_seed in range(start_seed, start_seed + length):
            exploded_seeds.append(new_seed)
    return exploded_seeds

if __name__ == "__main__":
    starting_seeds, mappings = parse_input()
    #print(f"Part 1 Solution: {min(apply_mapping(0, mappings, starting_seeds))}")
    exploded_seeds = explode_initial_seeds(starting_seeds)
    print(f"Part 2 Solution: {min(apply_mapping(0, mappings, exploded_seeds))}")
