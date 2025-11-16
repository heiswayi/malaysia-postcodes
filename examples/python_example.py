#!/usr/bin/env python3
"""
Malaysia Postcode Usage Examples - Python

This file demonstrates various ways to use the Malaysia postcode data in Python.
"""

import json
import csv
from pathlib import Path

# Example 1: Load and search JSON data
def example_json_search():
    """Load JSON data and search for postcodes in a specific city"""
    print("="*60)
    print("Example 1: Search postcodes in JSON format")
    print("="*60)

    # Load complete postcode data
    with open('../data/json/postcodes.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Search for a specific city
    search_city = "Petaling Jaya"

    for state in data['states']:
        for city in state['cities']:
            if search_city.lower() in city['name'].lower():
                print(f"\nState: {state['name']} ({state['code']})")
                print(f"City: {city['name']}")
                print(f"Postcodes: {', '.join(city['postcodes'][:10])}...")
                print(f"Total: {len(city['postcodes'])} postcodes")

    print()

# Example 2: Load state-specific data
def example_state_data():
    """Load data for a specific state"""
    print("="*60)
    print("Example 2: Load state-specific data")
    print("="*60)

    # Load Selangor data
    with open('../data/json/states/selangor.json', 'r', encoding='utf-8') as f:
        selangor = json.load(f)

    print(f"\nState: {selangor['name']} ({selangor['code']})")
    print(f"Total cities: {len(selangor['cities'])}")
    print(f"\nFirst 5 cities:")

    for city in selangor['cities'][:5]:
        postcode_range = f"{city['postcodes'][0]} - {city['postcodes'][-1]}"
        print(f"  - {city['name']:30} ({len(city['postcodes']):3} postcodes) [{postcode_range}]")

    print()

# Example 3: Read CSV data
def example_csv_read():
    """Read and filter CSV data"""
    print("="*60)
    print("Example 3: Read and filter CSV data")
    print("="*60)

    # Read postcodes CSV
    postcodes = []
    with open('../data/csv/postcodes.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        postcodes = list(reader)

    # Filter by state
    johor_postcodes = [p for p in postcodes if p['state_code'] == 'JHR']

    print(f"\nTotal postcodes in Malaysia: {len(postcodes)}")
    print(f"Postcodes in Johor: {len(johor_postcodes)}")
    print(f"\nFirst 5 Johor postcodes:")

    for p in johor_postcodes[:5]:
        print(f"  {p['postcode']} - {p['city']}, {p['state']}")

    print()

# Example 4: Validate a postcode
def validate_postcode(postcode):
    """Validate if a postcode exists and return its location"""
    with open('../data/csv/postcodes.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['postcode'] == postcode:
                return {
                    'valid': True,
                    'city': row['city'],
                    'state': row['state'],
                    'state_code': row['state_code']
                }

    return {'valid': False}

def example_validate():
    """Example of postcode validation"""
    print("="*60)
    print("Example 4: Validate postcodes")
    print("="*60)

    test_postcodes = ['50000', '10000', '99999', '40100']

    for pc in test_postcodes:
        result = validate_postcode(pc)
        if result['valid']:
            print(f"\n✓ {pc} is valid")
            print(f"  City: {result['city']}")
            print(f"  State: {result['state']} ({result['state_code']})")
        else:
            print(f"\n✗ {pc} is not valid")

    print()

# Example 5: Get all postcodes for a state
def get_postcodes_by_state(state_code):
    """Get all postcodes for a given state"""
    postcodes = []
    with open('../data/csv/postcodes.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['state_code'] == state_code:
                postcodes.append(row)
    return postcodes

def example_by_state():
    """Example of getting postcodes by state"""
    print("="*60)
    print("Example 5: Get postcodes by state")
    print("="*60)

    state_code = 'PLS'  # Perlis
    postcodes = get_postcodes_by_state(state_code)

    print(f"\nPostcodes in {state_code}:")
    print(f"Total: {len(postcodes)}")

    # Group by city
    cities = {}
    for p in postcodes:
        city = p['city']
        if city not in cities:
            cities[city] = []
        cities[city].append(p['postcode'])

    print(f"\nCities: {len(cities)}")
    for city, pcs in sorted(cities.items()):
        print(f"  {city:30} {len(pcs):3} postcodes")

    print()

if __name__ == '__main__':
    # Run all examples
    example_json_search()
    example_state_data()
    example_csv_read()
    example_validate()
    example_by_state()

    print("="*60)
    print("All examples completed!")
    print("="*60)
