# Usage Examples

This directory contains code examples demonstrating how to use the Malaysia Postcode data in different programming languages.

## Available Examples

### Python (`python_example.py`)

```bash
cd examples
python3 python_example.py
```

Demonstrates:
- Loading and searching JSON data
- Reading state-specific data
- Reading and filtering CSV data
- Validating postcodes
- Getting postcodes by state

### JavaScript/Node.js (`javascript_example.js`)

```bash
cd examples
node javascript_example.js
```

Demonstrates:
- Loading and searching JSON data
- Reading state-specific data
- Validating postcodes
- Getting cities by state
- Building fast lookup maps

### PHP (`php_example.php`)

```bash
cd examples
php php_example.php
```

Demonstrates:
- Loading and searching JSON data
- Reading state-specific data
- Reading and filtering CSV data
- Validating postcodes
- Getting postcodes by state

## Quick Usage Patterns

### JSON Format (Recommended for most applications)

```javascript
// Load all data
const data = require('../data/json/postcodes.json');

// Or load specific state
const selangor = require('../data/json/states/selangor.json');
```

### CSV Format (For spreadsheets and database imports)

```python
import csv

with open('../data/csv/postcodes.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['postcode'], row['city'], row['state'])
```

## Common Use Cases

1. **Postcode Validation** - Check if a postcode is valid
2. **Address Autocomplete** - Suggest cities based on postcode
3. **State Lookup** - Find which state a postcode belongs to
4. **City Listing** - Get all cities in a specific state
5. **Postcode Range** - Find all postcodes in a city or state

## Data Structure

### JSON Structure
```json
{
  "metadata": {...},
  "states": [
    {
      "name": "Selangor",
      "code": "SGR",
      "cities": [
        {
          "name": "Petaling Jaya",
          "postcodes": ["46000", "46050", ...]
        }
      ]
    }
  ]
}
```

### CSV Structure
```csv
postcode,city,state,state_code
40100,Shah Alam,Selangor,SGR
```
