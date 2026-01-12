# Head-to-Head Standings Matrix Generator

Generates a head-to-head wins matrix from team matchup data stored in JSON format. This solution demonstrates working with data structures, loops, and logic to build a matrix table.

## Input Format

The input JSON file should have the following structure:

```json
{
  "TEAM1": {
    "TEAM2": { "W": 10, "L": 12 },
    "TEAM3": { "W": 15, "L": 7 }
  },
  "TEAM2": {
    "TEAM1": { "W": 12, "L": 10 },
    "TEAM3": { "W": 13, "L": 9 }
  }
}
```

- Top-level keys are team names
- Each team maps to a dictionary of opponents
- Each opponent has `"W"` (wins) and `"L"` (losses) for that matchup

## What the Matrix Represents

The output matrix displays:
- **Rows**: Each team's wins against opponents (row by row)
- **Columns**: Opponent teams
- **Cell (i, j)**: Number of wins by team_i against team_j
- **Diagonal**: Shows `"--"` (teams don't play themselves)
- **Missing matchups**: Shown as blank cells (if a matchup doesn't exist in the data)

## Solution Approach

The solution uses:
1. **Data structures**: Dictionaries to store team records, lists for the matrix
2. **Loops**: Nested loops to iterate through teams and build the matrix
3. **Logic**: Conditional checks for diagonal cells and handling missing matchups

## How to Run

```bash
python main.py sample.json
```

Example output:
```
|  | BRO | BSN | CHC | CIN | NYG | PHI | PIT | STL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BRO | -- | 10 | 15 | 15 | 14 | 14 | 15 | 11 |
| BSN | 12 | -- | 13 | 13 | 13 | 14 | 12 | 9 |
| CHC | 7 | 9 | -- | 12 | 7 | 16 | 8 | 10 |
| CIN | 7 | 9 | 10 | -- | 13 | 13 | 13 | 8 |
| NYG | 8 | 9 | 15 | 9 | -- | 12 | 15 | 13 |
| PHI | 8 | 8 | 6 | 9 | 10 | -- | 13 | 8 |
| PIT | 7 | 10 | 14 | 9 | 7 | 9 | -- | 6 |
| STL | 11 | 13 | 12 | 14 | 9 | 14 | 16 | -- |
```

## Requirements

- Python 3.6+
- No external dependencies (uses only Python standard library)
