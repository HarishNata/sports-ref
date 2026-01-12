#!/usr/bin/env python3
import json
import sys

# Load JSON data
with open(sys.argv[1], 'r') as f:
    data = json.load(f)

# Get sorted team names
teams = sorted(data.keys())

# Build matrix
matrix = []
# Header row
matrix.append([''] + teams)

# Data rows
for team in teams:
    row = [team]
    for opponent in teams:
        if team == opponent:
            row.append('--')
        else:
            wins = data[team].get(opponent, {}).get('W', 0)
            row.append(str(wins) if wins else '')
    matrix.append(row)

# Print markdown table
print('| ' + ' | '.join(matrix[0]) + ' |')
print('|' + '|'.join([' --- ' for _ in matrix[0]]) + '|')
for row in matrix[1:]:
    print('| ' + ' | '.join(row) + ' |')
