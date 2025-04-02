import requests
import re
from bs4 import BeautifulSoup

def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    table_rows = soup.find_all('tr')[1:] 
    
    data = []
    for row in table_rows:
        cols = row.find_all('td')
        if len(cols) == 3:
            x = int(cols[0].text.strip())
            char = cols[1].text.strip()
            y = int(cols[2].text.strip())
            data.append((x, y, char))
    
    return data

def parse_data(data):
    return {(x, y): char for x, y, char in data}

def build_grid(grid):
    if not grid:
        return []
    max_x = max(x for x, _ in grid)
    max_y = max(y for _, y in grid)
    grid_representation = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for (x, y), char in grid.items():
        grid_representation[y][x] = char

    return grid_representation

def print_grid(grid):
    for row in grid:
        print(''.join(row))


def decode_secret_message(url):
    data = fetch_data(url)
    grid_data = parse_data(data)
    grid_rep = build_grid(grid_data)
    print_grid(grid_rep)

    return grid_rep



def run_tests():
    url = "https://docs.google.com/document/d/e/2PACX-1vSZ1vDD85PCR1d5QC2XwbXClC1Kuh3a4u0y3VbTvTFQI53erafhUkGot24ulET8ZRqFSzYoi3pLTGwM/pub"
    print("\nTest Case: Data from Google Doc")
    result = decode_secret_message(url)
    assert isinstance(result, list) and all(isinstance(row, list) for row in result), "Failed"
    print("Passed\n")


run_tests()
