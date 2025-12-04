# Advent of Code 2025

This repository contains my solutions to the [Advent of Code 2025](https://adventofcode.com/2025) challenges, implemented in Python 3.12.

## Quick Start

### Prerequisites
- Python 3.12 or higher
- Optional: [uv](https://docs.astral.sh/uv/) package manager

### Installation

**Using UV (recommended):**
```bash
# Install dependencies
uv sync
```

**Using standard Python:**
```bash
# Install dependencies
python3 -m pip install numpy
# Or install all dependencies including dev tools
python3 -m pip install numpy pytest
```

## Running Solutions

### Run a Specific Day's Solution

Each day's solution is self-contained and can be run independently:

```bash
# Navigate to the day's directory and run
cd day01
python3 main.py

# Or from the repository root
python3 day01/main.py
```

### Using Test Input

Each day has both `input.txt` (actual puzzle input) and `test.txt` (sample input for testing). To use test input:

1. Open the day's `main.py` file
2. Change `"input.txt"` to `"test.txt"` in the `open()` statement
3. Run the solution

Example:
```python
# In dayXX/main.py, change:
with open(os.path.join(script_dir, "input.txt"), "r") as f:
# To:
with open(os.path.join(script_dir, "test.txt"), "r") as f:
```

## Project Structure

```
aoc-2025/
├── __template/           # Template for new day solutions
│   ├── main.py          # Solution template
│   ├── input.txt        # Placeholder for puzzle input
│   └── test.txt         # Placeholder for test input
├── day01/               # Day 1 solution
│   ├── main.py          # Solution code
│   ├── input.txt        # Actual puzzle input
│   └── test.txt         # Sample test input
├── day02/               # Day 2 solution
├── day03/               # Day 3 solution
├── day04/               # Day 4 solution
├── main.py              # Root entry point (placeholder)
├── pyproject.toml       # Project configuration
├── .python-version      # Python version (3.12)
├── INSTRUCTIONS.md      # Detailed instructions for AI agents
└── README.md            # This file
```

## Code Structure

Each day's solution follows a consistent pattern:

```python
def solve_part1(lines):
    """Solve part 1 of the challenge"""
    # Implementation here

def solve_part2(lines):
    """Solve part 2 of the challenge"""
    # Implementation here

def main():
    """Read input and run both parts"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_dir, "input.txt"), "r") as f:
        lines = f.readlines()
        solve_part1(lines)
        solve_part2(lines)
```

## Adding a New Day

1. **Copy the template:**
   ```bash
   cp -r __template/ dayXX  # Replace XX with day number
   cd dayXX
   ```

2. **Add your puzzle input:**
   - Copy the puzzle input from Advent of Code to `input.txt`
   - Copy any sample input to `test.txt`

3. **Implement the solution:**
   - Edit `main.py`
   - Implement `solve_part1()` function
   - Test with `test.txt` first. Add the example from the question description so that you can verify correctness.
   - Implement `solve_part2()` function

4. **Run and verify:**
   ```bash
   python3 main.py
   ```

## Dependencies

- **numpy** (>=2.3.5): Used for grid-based problems (Day 4)
- **pytest** (>=8.0.0): For testing (dev dependency)

## Tips

- Start by reading the problem on [Advent of Code](https://adventofcode.com/2025)
- Use the test input to verify your solution logic before running on actual input
- Each solution is independent - no shared code between days
- Solutions prioritize clarity and correctness over optimization

## Contributing

This is a personal learning repository. Feel free to fork and create your own solutions!

## License

This project is open source and available for educational purposes.