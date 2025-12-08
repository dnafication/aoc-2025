from collections import defaultdict
import os
from pprint import pprint


def euclidean_distance(point1, point2):
    return (
        (point1[0] - point2[0]) ** 2
        + (point1[1] - point2[1]) ** 2
        + (point1[2] - point2[2]) ** 2
    ) ** 0.5


def solve_part1(points, pairs_to_collect):
    print("Solving Part 1")
    point_distances = []
    for i, (x1, y1, z1) in enumerate(points):
        for j, (x2, y2, z2) in enumerate(points):
            if i > j:
                distance = euclidean_distance((x1, y1, z1), (x2, y2, z2))
                point_distances.append((distance, i, j))

    union_find = {i: i for i in range(len(points))}

    def find(x):
        if union_find[x] != x:
            union_find[x] = find(union_find[x])
        return union_find[x]

    def mix(x, y):
        union_find[find(x)] = find(y)

    point_distances = sorted(point_distances)
    pprint(point_distances[:5])

    for _d, i, j in point_distances[:pairs_to_collect]:
        mix(i, j)

    pprint(union_find)

    merged_circuits = defaultdict(int)  # stores the count of merged points
    for x in range(len(points)):
        root = find(x)
        merged_circuits[root] += 1
    counts = sorted(merged_circuits.values(), reverse=True)
    print("Answer Part 1:", counts[0] * counts[1] * counts[2])


def solve_part2(points):
    print("Solving Part 2")
    point_distances = []
    for i, (x1, y1, z1) in enumerate(points):
        for j, (x2, y2, z2) in enumerate(points):
            if i > j:
                distance = euclidean_distance((x1, y1, z1), (x2, y2, z2))
                point_distances.append((distance, i, j))

    union_find = {i: i for i in range(len(points))}

    def find(x):
        if union_find[x] != x:
            union_find[x] = find(union_find[x])
        return union_find[x]

    def mix(x, y):
        union_find[find(x)] = find(y)

    point_distances = sorted(point_distances)
    pprint(point_distances[:5])

    connections = 0
    for _d, i, j in point_distances:
        if find(i) != find(j):
            connections += 1
            mix(i, j)
        if connections == len(points) - 1:
            print("Last two points connected:", points[i], points[j])
            print("Answer Part 2:", points[i][0] * points[j][0])
            break


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Replace with test.txt for testing with smaller input
    input_file = "input.txt"
    with open(
        os.path.join(
            script_dir,
            input_file,
        ),
        "r",
        encoding="utf-8",
    ) as f:
        lines = f.readlines()
        lines = [tuple(map(int, line.strip().split(","))) for line in lines]
        pairs_to_collect = 1000 if input_file == "input.txt" else 10
        solve_part1(lines, pairs_to_collect)
        solve_part2(lines)


if __name__ == "__main__":
    main()
