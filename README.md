# Malaysia Postcodes

A comprehensive, up-to-date database of Malaysian postcodes, cities, and states. Available in both JSON and CSV formats for easy integration into your applications.

## Features

- **2,932 unique postcodes** covering all Malaysian states and federal territories
- **443 cities/areas** across 16 states and territories
- **Multiple formats**: JSON and CSV
- **State-specific files** for optimized loading
- **Well-structured** and easy to use
- **Code examples** in Python, JavaScript, and PHP
- **Free and open source** under CC BY 4.0 license

## Quick Start

### Option 1: Use JSON (Recommended)

```javascript
// Node.js
const postcodes = require('./data/json/postcodes.json');

// Find postcodes for a city
postcodes.states.forEach(state => {
  state.cities.forEach(city => {
    if (city.name === 'Petaling Jaya') {
      console.log(city.postcodes); // ['46000', '46050', ...]
    }
  });
});
```

```python
# Python
import json

with open('data/json/postcodes.json', 'r') as f:
    data = json.load(f)

# Find postcodes for a city
for state in data['states']:
    for city in state['cities']:
        if city['name'] == 'Shah Alam':
            print(city['postcodes'])  # ['40000', '40100', ...]
```

### Option 2: Use CSV

```python
import csv

with open('data/csv/postcodes.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['postcode']} - {row['city']}, {row['state']}")
```

## Data Structure

### Directory Layout

```
malaysia-postcodes/
├── data/
│   ├── csv/
│   │   ├── postcodes.csv              # All postcodes in CSV format
│   │   ├── states.csv                 # State code mappings
│   │   └── states/                    # Individual state CSV files
│   │       ├── Johor.csv
│   │       ├── Selangor.csv
│   │       └── ...
│   └── json/
│       ├── postcodes.json             # All postcodes in JSON format
│       └── states/                    # Individual state JSON files
│           ├── johor.json
│           ├── selangor.json
│           └── ...
├── examples/                          # Code examples
│   ├── python_example.py
│   ├── javascript_example.js
│   └── php_example.php
└── process_data.py                    # Data processing script
```

### JSON Format

```json
{
  "metadata": {
    "version": "2025.1",
    "description": "Complete Malaysia postcode database",
    "total_states": 16
  },
  "states": [
    {
      "name": "Selangor",
      "code": "SGR",
      "cities": [
        {
          "name": "Shah Alam",
          "postcodes": ["40000", "40100", "40150", ...]
        }
      ]
    }
  ]
}
```

### CSV Format

```csv
postcode,city,state,state_code
40000,Shah Alam,Selangor,SGR
40100,Shah Alam,Selangor,SGR
50000,Kuala Lumpur,Wp Kuala Lumpur,KUL
```

## State Codes

| Code | State/Territory |
|------|----------------|
| JHR  | Johor |
| KDH  | Kedah |
| KTN  | Kelantan |
| MLK  | Melaka |
| NSN  | Negeri Sembilan |
| PHG  | Pahang |
| PRK  | Perak |
| PLS  | Perlis |
| PNG  | Pulau Pinang |
| SBH  | Sabah |
| SGR  | Selangor |
| SRW  | Sarawak |
| TRG  | Terengganu |
| KUL  | Wilayah Persekutuan Kuala Lumpur |
| LBN  | Wilayah Persekutuan Labuan |
| PJY  | Wilayah Persekutuan Putrajaya |

## Statistics by State

| State | Code | Cities | Postcodes | Range |
|-------|------|--------|-----------|-------|
| Johor | JHR | 53 | 236 | 79000 - 86900 |
| Kedah | KDH | 34 | 149 | 05000 - 09810 |
| Kelantan | KTN | 22 | 145 | 15000 - 19800 |
| Melaka | MLK | 16 | 37 | 75000 - 78309 |
| Negeri Sembilan | NSN | 25 | 157 | 70000 - 73509 |
| Pahang | PHG | 38 | 204 | 25000 - 28800 |
| Perak | PRK | 71 | 239 | 30000 - 36810 |
| Perlis | PLS | 6 | 77 | 01000 - 02800 |
| Pulau Pinang | PNG | 22 | 142 | 10000 - 14400 |
| Sabah | SBH | 33 | 410 | 87000 - 91309 |
| Sarawak | SRW | 49 | 228 | 93000 - 98859 |
| Selangor | SGR | 48 | 339 | 40000 - 68100 |
| Terengganu | TRG | 22 | 169 | 20000 - 24300 |
| WP Kuala Lumpur | KUL | 2 | 299 | 50000 - 60000 |
| WP Labuan | LBN | 1 | 27 | 87000 - 87033 |
| WP Putrajaya | PJY | 1 | 74 | 62000 - 62988 |

## Common Use Cases

### 1. Validate a Postcode

```python
def validate_postcode(postcode):
    with open('data/csv/postcodes.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['postcode'] == postcode:
                return {
                    'valid': True,
                    'city': row['city'],
                    'state': row['state']
                }
    return {'valid': False}

result = validate_postcode('50000')
# {'valid': True, 'city': 'Kuala Lumpur', 'state': 'Wp Kuala Lumpur'}
```

### 2. Get All Cities in a State

```javascript
const data = require('./data/json/postcodes.json');

function getCitiesByState(stateCode) {
  const state = data.states.find(s => s.code === stateCode);
  return state ? state.cities : [];
}

const selangorCities = getCitiesByState('SGR');
// Returns array of cities in Selangor
```

### 3. Address Autocomplete

```python
import json

with open('data/json/postcodes.json', 'r') as f:
    data = json.load(f)

def get_city_by_postcode(postcode):
    for state in data['states']:
        for city in state['cities']:
            if postcode in city['postcodes']:
                return {
                    'city': city['name'],
                    'state': state['name'],
                    'state_code': state['code']
                }
    return None

info = get_city_by_postcode('40100')
# {'city': 'Shah Alam', 'state': 'Selangor', 'state_code': 'SGR'}
```

### 4. Load State-Specific Data

For applications that only need data for specific states, use the individual state files:

```javascript
// Smaller file size, faster loading
const selangor = require('./data/json/states/selangor.json');

console.log(`${selangor.name} (${selangor.code})`);
console.log(`Cities: ${selangor.cities.length}`);
```

## Code Examples

Check the [`examples/`](examples/) directory for complete working examples:

- **Python**: [`examples/python_example.py`](examples/python_example.py)
- **JavaScript/Node.js**: [`examples/javascript_example.js`](examples/javascript_example.js)
- **PHP**: [`examples/php_example.php`](examples/php_example.php)

Run them to see various usage patterns:

```bash
# Python
cd examples && python3 python_example.py

# Node.js
cd examples && node javascript_example.js

# PHP
cd examples && php php_example.php
```

## Data Source

This database is compiled from community-maintained sources:
- Primary source: [AsyrafHussin/malaysia-postcodes](https://github.com/AsyrafHussin/malaysia-postcodes)
- Last updated: 2025

The data is regularly updated to ensure accuracy. If you find any errors or missing postcodes, please [open an issue](https://github.com/heiswayi/malaysia-postcodes/issues).

## Updating the Data

To regenerate all data files from the latest source:

```bash
# Download latest data
curl -o /tmp/malaysia-postcodes-new.json \
  https://raw.githubusercontent.com/AsyrafHussin/malaysia-postcodes/main/all.json

# Process and generate files
python3 process_data.py
```

This will regenerate:
- All CSV files in `data/csv/`
- All JSON files in `data/json/`
- State-specific files in both formats

## API Integration Ideas

This dataset is perfect for building:

1. **Address Validation APIs** - Validate Malaysian addresses
2. **Postcode Lookup Services** - RESTful API for postcode queries
3. **E-commerce Platforms** - Shipping and delivery zone calculations
4. **Form Autocomplete** - Dynamic city/state selection based on postcode
5. **Logistics Systems** - Route planning and zone management
6. **Mobile Apps** - Offline postcode lookup

### Example REST API Endpoint

```javascript
// Express.js example
const express = require('express');
const postcodes = require('./data/json/postcodes.json');

const app = express();

app.get('/api/postcode/:code', (req, res) => {
  const code = req.params.code;

  for (const state of postcodes.states) {
    for (const city of state.cities) {
      if (city.postcodes.includes(code)) {
        return res.json({
          postcode: code,
          city: city.name,
          state: state.name,
          state_code: state.code
        });
      }
    }
  }

  res.status(404).json({ error: 'Postcode not found' });
});

app.listen(3000);
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions:

1. Check existing [issues](https://github.com/heiswayi/malaysia-postcodes/issues)
2. Open a new issue with details
3. Submit a pull request with fixes or improvements

## License

This repository and its data are licensed under [CC BY 4.0 DEED](https://creativecommons.org/licenses/by/4.0/deed.en).

You are free to:
- **Share** — copy and redistribute the material
- **Adapt** — remix, transform, and build upon the material for any purpose

Under the following terms:
- **Attribution** — You must give appropriate credit and link back to this repository

## Acknowledgments

- Original data compilation: [MalaysiaPostcode.com](https://malaysiapostcode.com/)
- Community updates: [AsyrafHussin/malaysia-postcodes](https://github.com/AsyrafHussin/malaysia-postcodes)
- Maintained with contributions from the developer community

---

**Made with ❤️ for Malaysian developers**

If this repository helped you, please give it a ⭐️ star!
