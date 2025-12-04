# Copilot Instructions for AoC 2025

## Project Overview

This is an Advent of Code 2025 solutions repository using Python 3.12. Each day's puzzle is a self-contained solution with its own directory.

## Code Structure & Patterns

### Standard Solution Template

Every day follows this exact pattern (see `__template/main.py`):

```python
def solve_part1(lines):
    print("Solving Part 1")
    # Implementation here

def solve_part2(lines):
    print("Solving Part 2")
    # Implementation here

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_dir, "input.txt"), "r", encoding="utf-8") as f:
        lines = f.readlines()
        solve_part1(lines)
        solve_part2(lines)
```

**Key patterns:**

- Always use `os.path.dirname(os.path.abspath(__file__))` for file paths (not hardcoded paths)
- Read input with `encoding="utf-8"` parameter
- Input comes as `lines = f.readlines()` - array of strings with newlines
- Each solution has both `solve_part1()` and `solve_part2()` functions

### File Organization

```
dayXX/
├── main.py      # Solution code
├── input.txt    # Actual puzzle input from AoC website
└── test.txt     # Sample input from puzzle description for testing
```

## Working with Solutions

### Testing Workflow

1. **Always start with test.txt**: Change `"input.txt"` to `"test.txt"` in the open() statement
2. Verify output matches expected result from puzzle description
3. Switch back to `"input.txt"` for final answer
4. Include comment: `# Replace with test.txt for testing with smaller input`

### Running Solutions

```bash
cd dayXX && python3 main.py  # Run from day directory
# OR
python3 dayXX/main.py        # Run from repo root
```

### Creating New Day Solutions

```bash
cp -r __template/ dayXX  # Copy template
cd dayXX
# Add puzzle input to input.txt
# Add example from puzzle to test.txt
# Implement solve_part1() and solve_part2()
```

## Dependencies & Environment

**Runtime:** numpy>=2.3.5 (used for grid/matrix problems like day04)
**Dev:** pytest>=8.0.0 (installed but no tests implemented yet)
**Python:** 3.12+

**Installation:**

```bash
uv sync                    # Preferred

# OR add new packages
uv add <package-name>     # Adds to pyproject.toml and installs
```

## Common Techniques & Examples

### Grid/Matrix Problems (see day04)

```python
import numpy as np

# Read grid from file
lines = f.read().strip().split('\n')
grid = np.array([list(line.strip()) for line in lines])

# Iterate with positions
for (row, col), value in np.ndenumerate(grid):
    # process each cell

# Get 8 neighbors (including diagonals)
directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
for dr, dc in directions:
    r, c = row + dr, col + dc
    if 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]:
        # valid neighbor at grid[r, c]

# Modify grid (always use .copy() when passing to functions)
solve_part1(grid.copy())  # Prevents mutation
```

### Parsing Patterns (see day01, day02, day03)

```python
# Single line with ranges: "1-10,50-100"
ranges = lines[0].strip().split(",")
for r in ranges:
    start, end = map(int, r.split("-"))

# Command parsing: "R25" or "L10"
direction = line[0]
steps = int(line[1:].strip())

# Digit extraction from string
digits = [int(d) for d in line.strip()]
```

### Modulo Arithmetic (see day01 - circular dial)

```python
# Circular position (0-99)
current_position = (current_position + steps) % 100  # Right
current_position = (current_position - steps) % 100  # Left
```

## Project-Specific Conventions

- **No shared utilities**: Each day is completely independent
- **No automated tests**: Manual testing with test.txt only
- **Print statements**: Use descriptive prints for results (e.g., `print(f"Total invalid IDs: {len(invalid_ids)}")`)
- **Comments**: Explain problem context at top of functions (see day01, day02)
- **Variable naming**: Use descriptive names (`invalid_ids`, `largest_number_list`, `position_list`)

## What NOT to Do

- Don't create shared helper files or utilities
- Don't add type hints (not used in this project)
- Don't create automated test files (manual testing only)
- Don't use relative imports between days
- Don't hardcode file paths - always use `os.path` relative to script
