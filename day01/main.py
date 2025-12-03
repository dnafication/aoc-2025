import os

STARTING_POSITION = 50


# We are rotating a dial which has positions from 0 to 99.
# The dial can be rotated left (L) or right (R).
# Starting position of the dial is given (50). Each line of input is a command
# indicating direction and number of steps to rotate.'
def solve_part1(lines):
    print("Solving Part 1")
    current_position = STARTING_POSITION
    position_list = [current_position]
    for line in lines:
        direction = line[0]
        steps = int(line[1:].strip())

        if direction == "R":
            current_position = (current_position + steps) % 100
        elif direction == "L":
            current_position = (current_position - steps) % 100
        position_list.append(current_position)
        # print(
        #     f"Direction: {direction}, Steps: {steps}, New Position: {current_position}"
        # )

    print(f"Landed on 0: {position_list.count(0)} times")


# Part 2: Count how many times the dial lands on position 0
def solve_part2(lines):
    print("Solving Part 2")
    current_position = STARTING_POSITION
    number_of_zero_landings = 0
    for line in lines:
        direction = line[0]
        steps = int(line[1:].strip())

        # Count how many times we land on 0 during this move
        # We need to check each position from current to final
        if direction == "R":
            for i in range(1, steps + 1):
                pos = (current_position + i) % 100
                if pos == 0:
                    number_of_zero_landings += 1
            current_position = (current_position + steps) % 100
        elif direction == "L":
            for i in range(1, steps + 1):
                pos = (current_position - i) % 100
                if pos == 0:
                    number_of_zero_landings += 1
            current_position = (current_position - steps) % 100

    print(f"Number of times landed on zero: {number_of_zero_landings}")


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_dir, "input.txt"), "r") as f:
        lines = f.readlines()
        solve_part1(lines)
        solve_part2(lines)


if __name__ == "__main__":
    main()
