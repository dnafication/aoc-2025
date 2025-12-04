# Instructions for AI Agent

## Repository Overview

This repository contains solutions for Advent of Code 2025 challenges implemented in Python 3.12.

## Codebase Structure

### Directory Layout
```
aoc-2025/
├── __template/           # Template directory for new day solutions
│   ├── main.py          # Template solution file
│   ├── input.txt        # Placeholder for actual puzzle input
│   └── test.txt         # Placeholder for test input
├── day01/, day02/, day03/, day04/  # Solution directories for each day
│   ├── main.py          # Solution implementation
│   ├── input.txt        # Actual puzzle input
│   └── test.txt         # Test input (when available)
├── main.py              # Root entry point (basic placeholder)
├── pyproject.toml       # Project configuration and dependencies
├── .python-version      # Python version specification (3.12)
├── uv.lock              # UV package manager lock file
└── README.md            # Project documentation
```

### Code Patterns

#### Solution Structure
Each day's solution follows this pattern:
1. **solve_part1(lines)** - Solves part 1 of the day's challenge
2. **solve_part2(lines)** - Solves part 2 of the day's challenge
3. **main()** - Reads input file and calls both solvers
4. Input files are read relative to the script directory using `os.path.dirname(os.path.abspath(__file__))`

#### Common Conventions
- Input files are read as lines with `readlines()`
- Solutions can switch between `input.txt` (actual puzzle) and `test.txt` (sample data) by changing the filename in the `open()` call
- Each solution is self-contained and can be run independently from its directory
- Comments often indicate when to use `test.txt` for testing with smaller input

### Dependencies
- **Python**: 3.12+
- **Runtime dependencies**: numpy>=2.3.5
- **Dev dependencies**: pytest>=8.0.0
- **Package manager**: UV (but regular Python also works)

## How to Work with This Codebase

### Running Solutions

**Individual Day:**
```bash
cd day01
python3 main.py
```

**Root Entry Point:**
```bash
python3 main.py  # Currently just prints a hello message
```

### Testing
- No automated tests are currently implemented
- Test manually by switching input files from `input.txt` to `test.txt`
- Each day has a `test.txt` file with sample input for verification

### Adding a New Day
1. Copy the `__template/` directory to `dayXX/`
2. Update `main.py` with the solution logic
3. Add the puzzle input to `input.txt`
4. Add test cases to `test.txt` if available
5. Implement `solve_part1()` and `solve_part2()` functions

### Code Style
- Use descriptive variable names
- Include comments explaining complex logic
- Keep helper functions close to where they're used
- Print results clearly with descriptive messages

### Dependencies Management
- Add dependencies to `pyproject.toml` under `dependencies` array
- Dev dependencies go in `[dependency-groups].dev`
- Run `python3 -m pip install <package>` to install individual packages

## Common Tasks

### Reading Input
```python
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(script_dir, "input.txt"), "r", encoding="utf-8") as f:
    lines = f.readlines()
```

### Switching to Test Input
Change `"input.txt"` to `"test.txt"` in the open statement.

### Example Solutions Summary

- **Day01**: Dial rotation problem (modular arithmetic)
- **Day02**: ID validation with pattern matching
- **Day03**: Finding largest numbers from digit sequences
- **Day04**: Grid-based cellular automaton using NumPy

## Important Notes

- Each day's solution is independent and self-contained
- No centralized test runner currently exists
- Solutions are meant to be quick problem-solving scripts, not production code
- File paths are handled relative to each script's location for portability
