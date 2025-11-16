#!/usr/bin/env python3
"""
Malaysia Postcode Data Processor
Converts JSON data to CSV and organizes by state
"""

import json
import csv
import os
from pathlib import Path

# State code mappings
STATE_CODES = {
    "Johor": "JHR",
    "Kedah": "KDH",
    "Kelantan": "KTN",
    "Wp Kuala Lumpur": "KUL",
    "Wp Labuan": "LBN",
    "Melaka": "MLK",
    "Negeri Sembilan": "NSN",
    "Pahang": "PHG",
    "Wp Putrajaya": "PJY",
    "Perlis": "PLS",
    "Pulau Pinang": "PNG",
    "Perak": "PRK",
    "Sabah": "SBH",
    "Selangor": "SGR",
    "Sarawak": "SRW",
    "Terengganu": "TRG"
}

def load_json_data(json_file):
    """Load JSON data from file"""
    with open(json_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_postcode_csv(data, output_file):
    """Create main postcodes CSV file"""
    print(f"Creating {output_file}...")

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['postcode', 'city', 'state', 'state_code'])

        for state_data in sorted(data['state'], key=lambda x: x['name']):
            state_name = state_data['name']
            state_code = STATE_CODES.get(state_name, '')

            for city_data in sorted(state_data['city'], key=lambda x: x['name']):
                city_name = city_data['name']

                for postcode in sorted(city_data['postcode']):
                    writer.writerow([postcode, city_name, state_name, state_code])

    print(f"✓ Created {output_file}")

def create_states_csv(output_file):
    """Create states mapping CSV file"""
    print(f"Creating {output_file}...")

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['state_code', 'state_name'])

        for state_name, state_code in sorted(STATE_CODES.items(), key=lambda x: x[1]):
            writer.writerow([state_code, state_name])

    print(f"✓ Created {output_file}")

def create_state_files(data, output_dir):
    """Create individual CSV files for each state"""
    print(f"Creating state-specific files in {output_dir}...")

    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(exist_ok=True)

    for state_data in sorted(data['state'], key=lambda x: x['name']):
        state_name = state_data['name']
        state_code = STATE_CODES.get(state_name, '')

        # Create filename
        filename = f"{state_name.replace(' ', '_')}.csv"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['postcode', 'city', 'state', 'state_code'])

            for city_data in sorted(state_data['city'], key=lambda x: x['name']):
                city_name = city_data['name']

                for postcode in sorted(city_data['postcode']):
                    writer.writerow([postcode, city_name, state_name, state_code])

        print(f"  ✓ Created {filename}")

def create_state_json_files(data, output_dir):
    """Create individual JSON files for each state"""
    print(f"Creating state-specific JSON files in {output_dir}...")

    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(exist_ok=True)

    for state_data in sorted(data['state'], key=lambda x: x['name']):
        state_name = state_data['name']

        # Create filename
        filename = f"{state_name.replace(' ', '_').lower()}.json"
        filepath = os.path.join(output_dir, filename)

        # Prepare state data
        state_output = {
            "name": state_name,
            "code": STATE_CODES.get(state_name, ''),
            "cities": []
        }

        for city_data in sorted(state_data['city'], key=lambda x: x['name']):
            city_output = {
                "name": city_data['name'],
                "postcodes": sorted(city_data['postcode'])
            }
            state_output['cities'].append(city_output)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(state_output, f, indent=2, ensure_ascii=False)

        print(f"  ✓ Created {filename}")

def create_complete_json(data, output_file):
    """Create complete JSON file with all data"""
    print(f"Creating {output_file}...")

    complete_data = {
        "metadata": {
            "version": "2025.1",
            "description": "Complete Malaysia postcode database",
            "total_states": len(data['state']),
            "source": "Community maintained - https://github.com/AsyrafHussin/malaysia-postcodes"
        },
        "states": []
    }

    for state_data in sorted(data['state'], key=lambda x: x['name']):
        state_name = state_data['name']

        state_output = {
            "name": state_name,
            "code": STATE_CODES.get(state_name, ''),
            "cities": []
        }

        for city_data in sorted(state_data['city'], key=lambda x: x['name']):
            city_output = {
                "name": city_data['name'],
                "postcodes": sorted(city_data['postcode'])
            }
            state_output['cities'].append(city_output)

        complete_data['states'].append(state_output)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(complete_data, f, indent=2, ensure_ascii=False)

    print(f"✓ Created {output_file}")

def print_statistics(data):
    """Print data statistics"""
    print("\n" + "="*60)
    print("DATA STATISTICS")
    print("="*60)

    total_states = len(data['state'])
    total_cities = sum(len(state['city']) for state in data['state'])
    total_postcodes = sum(len(city['postcode']) for state in data['state'] for city in state['city'])

    print(f"Total States/Territories: {total_states}")
    print(f"Total Cities/Areas: {total_cities}")
    print(f"Total Postcodes: {total_postcodes}")
    print("\nBy State:")

    for state_data in sorted(data['state'], key=lambda x: x['name']):
        state_name = state_data['name']
        state_code = STATE_CODES.get(state_name, '')
        cities_count = len(state_data['city'])
        postcodes_count = sum(len(city['postcode']) for city in state_data['city'])

        print(f"  {state_code:3} - {state_name:30} {cities_count:3} cities, {postcodes_count:5} postcodes")

    print("="*60 + "\n")

def main():
    """Main processing function"""
    print("\n" + "="*60)
    print("MALAYSIA POSTCODE DATA PROCESSOR")
    print("="*60 + "\n")

    # Load JSON data
    json_file = '/tmp/malaysia-postcodes-new.json'
    print(f"Loading data from {json_file}...")
    data = load_json_data(json_file)
    print(f"✓ Data loaded successfully\n")

    # Print statistics
    print_statistics(data)

    # Create output directories
    Path('data').mkdir(exist_ok=True)
    Path('data/csv').mkdir(exist_ok=True)
    Path('data/json').mkdir(exist_ok=True)

    # Create CSV files
    print("Generating CSV files...")
    create_postcode_csv(data, 'data/csv/postcodes.csv')
    create_states_csv('data/csv/states.csv')
    create_state_files(data, 'data/csv/states')

    # Create JSON files
    print("\nGenerating JSON files...")
    create_complete_json(data, 'data/json/postcodes.json')
    create_state_json_files(data, 'data/json/states')

    print("\n" + "="*60)
    print("✓ ALL FILES GENERATED SUCCESSFULLY!")
    print("="*60)
    print("\nOutput structure:")
    print("  data/")
    print("    csv/")
    print("      postcodes.csv          - All postcodes")
    print("      states.csv             - State mappings")
    print("      states/                - Individual state CSV files")
    print("    json/")
    print("      postcodes.json         - All postcodes (JSON)")
    print("      states/                - Individual state JSON files")
    print()

if __name__ == '__main__':
    main()
