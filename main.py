#!/usr/bin/env python3
"""
Generate a head-to-head standings matrix from team matchup data.
"""

import argparse
import json
from typing import Dict, List, Tuple


def load_data(file_path: str) -> Dict:
    """Load JSON data from file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_teams(data: Dict) -> List[str]:
    """Extract and sort teams alphabetically from top-level keys."""
    teams = sorted(data.keys())
    return teams


def get_wins(data: Dict, team: str, opponent: str) -> int:
    """Get wins for team vs opponent, returning 0 if matchup doesn't exist."""
    if team not in data or opponent not in data[team]:
        return 0
    matchup = data[team][opponent]
    return matchup.get('W', 0)


def build_matrix(data: Dict, teams: List[str]) -> List[List[str]]:
    """Build 2D matrix of head-to-head records."""
    matrix = []
    
    # Header row
    header = [''] + teams
    matrix.append(header)
    
    # Data rows
    for team in teams:
        row = [team]
        for opponent in teams:
            if team == opponent:
                row.append('--')
            else:
                wins = get_wins(data, team, opponent)
                row.append(str(wins) if wins > 0 else '')
        matrix.append(row)
    
    return matrix


def format_markdown(matrix: List[List[str]]) -> str:
    """Format matrix as Markdown table."""
    if not matrix:
        return ''
    
    lines = []
    header = matrix[0]
    
    # Header row
    lines.append('| ' + ' | '.join(header) + ' |')
    
    # Separator row
    lines.append('|' + '|'.join([' --- ' for _ in header]) + '|')
    
    # Data rows
    for row in matrix[1:]:
        lines.append('| ' + ' | '.join(row) + ' |')
    
    return '\n'.join(lines)


def format_html(matrix: List[List[str]]) -> str:
    """Format matrix as HTML table."""
    if not matrix:
        return ''
    
    html = ['<table>']
    
    # Header row
    html.append('<thead><tr>')
    for cell in matrix[0]:
        html.append(f'<th>{cell}</th>')
    html.append('</tr></thead>')
    
    # Body rows
    html.append('<tbody>')
    for row in matrix[1:]:
        html.append('<tr>')
        for i, cell in enumerate(row):
            tag = 'th' if i == 0 else 'td'
            html.append(f'<{tag}>{cell}</{tag}>')
        html.append('</tr>')
    html.append('</tbody>')
    
    html.append('</table>')
    return '\n'.join(html)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Generate head-to-head standings matrix from team matchup data.'
    )
    parser.add_argument(
        '--input',
        required=True,
        help='Path to JSON file containing team matchup data'
    )
    parser.add_argument(
        '--format',
        choices=['markdown', 'html'],
        default='markdown',
        help='Output format (default: markdown)'
    )
    
    args = parser.parse_args()
    
    # Load data
    data = load_data(args.input)
    
    # Get teams
    teams = get_teams(data)
    
    # Build matrix
    matrix = build_matrix(data, teams)
    
    # Format and output
    if args.format == 'html':
        output = format_html(matrix)
    else:
        output = format_markdown(matrix)
    
    print(output)


if __name__ == '__main__':
    main()

