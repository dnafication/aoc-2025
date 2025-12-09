import os
from pprint import pprint


def area(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2 + 1) * abs(y1 - y2 + 1)


def solve_part1(points: list[list[int]]):
    print("Solving Part 1")
    # pprint(points)
    areas = []
    for i in range(len(points)):
        for j in range(len(points)):
            if i != j:
                a = area(points[i], points[j])
                areas.append((a, i, j))

    max_area = max(areas, key=lambda x: x[0])
    print("Answer Part 1:", max_area)


def solve_part2(points: list[list[int]]):
    print("Solving Part 2")
    # Attempt1 We need to create triplets of points that form rectangles, due to the constraints of the problem
    areas = []
    points_by_x = {}
    points_by_y = {}
    for point in points:
        x, y = point
        if x not in points_by_x:
            points_by_x[x] = []
        if y not in points_by_y:
            points_by_y[y] = []
        points_by_x[x].append(point)
        points_by_y[y].append(point)

    max_area = 0
    for point in points:
        x, y = point

        vertical_neighbors = [p for p in points_by_x[x] if p != point]
        horizontal_neighbors = [p for p in points_by_y[y] if p != point]

        for v in vertical_neighbors:
            for h in horizontal_neighbors:
                x_distance = abs(h[0] - x + 1)
                y_distance = abs(v[1] - y + 1)

    # for triplet in triplets:
    #     point, v, h = triplet
    #     area = abs(point[1] - v[1] + 1) * abs(point[0] - h[0] + 1)
    #     areas.append((area, triplet))

    # max_area = max(areas, key=lambda x: x[0])

    ## Attempt2: build the grid and fill it with red and green tiles
    # min_x = min(point[0] for point in points)
    # max_x = max(point[0] for point in points)
    # min_y = min(point[1] for point in points)
    # max_y = max(point[1] for point in points)
    # width = max_x - min_x + 1
    # height = max_y - min_y + 1
    # grid = [["." for _ in range(width)] for _ in range(height)]
    # for point in points:
    #     x, y = point
    #     grid[y - min_y][x - min_x] = "#"  # Place the red tiles

    # print("\n".join("".join(row) for row in grid))


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Replace with test.txt for testing with smaller input
    with open(os.path.join(script_dir, "test.txt"), "r", encoding="utf-8") as f:
        points = f.readlines()
        points = [[int(x) for x in line.strip().split(",")] for line in points]
        solve_part1(points)
        solve_part2(points)


if __name__ == "__main__":
    main()
