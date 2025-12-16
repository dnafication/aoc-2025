import os


def find_all_paths(network, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in network:
        return []
    paths = []
    for node in network[start]:
        if node not in path:
            newpaths = find_all_paths(network, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def solve_part1(lines):
    print("Solving Part 1")
    network = {}
    for line in lines:
        name, output = line.strip().split(":")
        output = output.strip().split(" ")
        # print(f"Device Name: {name}, Output: {output}")
        network[name] = output
    # print(network)

    all_paths = find_all_paths(network, "you", "out")
    print(f"Count of all paths from 'you' to 'out': {len(all_paths)}")


def solve_part2(lines):
    print("Solving Part 2")
    network = {}
    for line in lines:
        name, output = line.strip().split(":")
        output = output.strip().split(" ")
        # print(f"Device Name: {name}, Output: {output}")
        network[name] = output
    # print(network)

    # def bfs


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Replace with test.txt for testing with smaller input
    with open(os.path.join(script_dir, "input.txt"), "r", encoding="utf-8") as f:
        lines = f.readlines()
        solve_part1(lines)
        solve_part2(lines)


if __name__ == "__main__":
    main()
