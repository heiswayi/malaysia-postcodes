/**
 * Malaysia Postcode Usage Examples - JavaScript/Node.js
 *
 * This file demonstrates various ways to use the Malaysia postcode data in JavaScript.
 *
 * To run these examples:
 *   node javascript_example.js
 */

const fs = require('fs');
const path = require('path');

// Example 1: Load and search JSON data
function exampleJsonSearch() {
    console.log('='.repeat(60));
    console.log('Example 1: Search postcodes in JSON format');
    console.log('='.repeat(60));

    // Load complete postcode data
    const data = JSON.parse(
        fs.readFileSync('../data/json/postcodes.json', 'utf-8')
    );

    // Search for a specific city
    const searchCity = 'Shah Alam';

    data.states.forEach(state => {
        state.cities.forEach(city => {
            if (city.name.toLowerCase().includes(searchCity.toLowerCase())) {
                console.log(`\nState: ${state.name} (${state.code})`);
                console.log(`City: ${city.name}`);
                console.log(`Postcodes: ${city.postcodes.slice(0, 10).join(', ')}...`);
                console.log(`Total: ${city.postcodes.length} postcodes`);
            }
        });
    });

    console.log();
}

// Example 2: Load state-specific data
function exampleStateData() {
    console.log('='.repeat(60));
    console.log('Example 2: Load state-specific data');
    console.log('='.repeat(60));

    // Load Selangor data
    const selangor = JSON.parse(
        fs.readFileSync('../data/json/states/selangor.json', 'utf-8')
    );

    console.log(`\nState: ${selangor.name} (${selangor.code})`);
    console.log(`Total cities: ${selangor.cities.length}`);
    console.log('\nFirst 5 cities:');

    selangor.cities.slice(0, 5).forEach(city => {
        const postcodeRange = `${city.postcodes[0]} - ${city.postcodes[city.postcodes.length - 1]}`;
        console.log(`  - ${city.name.padEnd(30)} (${String(city.postcodes.length).padStart(3)} postcodes) [${postcodeRange}]`);
    });

    console.log();
}

// Example 3: Validate a postcode
function validatePostcode(postcode, data) {
    for (const state of data.states) {
        for (const city of state.cities) {
            if (city.postcodes.includes(postcode)) {
                return {
                    valid: true,
                    city: city.name,
                    state: state.name,
                    stateCode: state.code
                };
            }
        }
    }

    return { valid: false };
}

function exampleValidate() {
    console.log('='.repeat(60));
    console.log('Example 3: Validate postcodes');
    console.log('='.repeat(60));

    const data = JSON.parse(
        fs.readFileSync('../data/json/postcodes.json', 'utf-8')
    );

    const testPostcodes = ['50000', '10000', '99999', '40100'];

    testPostcodes.forEach(pc => {
        const result = validatePostcode(pc, data);
        if (result.valid) {
            console.log(`\n✓ ${pc} is valid`);
            console.log(`  City: ${result.city}`);
            console.log(`  State: ${result.state} (${result.stateCode})`);
        } else {
            console.log(`\n✗ ${pc} is not valid`);
        }
    });

    console.log();
}

// Example 4: Get all cities in a state
function getCitiesByState(stateCode, data) {
    const state = data.states.find(s => s.code === stateCode);
    return state ? state.cities : [];
}

function exampleByState() {
    console.log('='.repeat(60));
    console.log('Example 4: Get cities by state');
    console.log('='.repeat(60));

    const data = JSON.parse(
        fs.readFileSync('../data/json/postcodes.json', 'utf-8')
    );

    const stateCode = 'PNG'; // Pulau Pinang
    const cities = getCitiesByState(stateCode, data);

    if (cities.length > 0) {
        const state = data.states.find(s => s.code === stateCode);
        console.log(`\nState: ${state.name} (${stateCode})`);
        console.log(`Total cities: ${cities.length}`);
        console.log('\nCities:');

        cities.forEach(city => {
            console.log(`  ${city.name.padEnd(30)} ${String(city.postcodes.length).padStart(3)} postcodes`);
        });
    }

    console.log();
}

// Example 5: Build a lookup map for fast searches
function buildPostcodeLookup(data) {
    const lookup = new Map();

    data.states.forEach(state => {
        state.cities.forEach(city => {
            city.postcodes.forEach(postcode => {
                lookup.set(postcode, {
                    city: city.name,
                    state: state.name,
                    stateCode: state.code
                });
            });
        });
    });

    return lookup;
}

function exampleLookupMap() {
    console.log('='.repeat(60));
    console.log('Example 5: Fast postcode lookup using Map');
    console.log('='.repeat(60));

    const data = JSON.parse(
        fs.readFileSync('../data/json/postcodes.json', 'utf-8')
    );

    console.log('\nBuilding lookup map...');
    const lookup = buildPostcodeLookup(data);
    console.log(`✓ Lookup map built with ${lookup.size} postcodes`);

    // Fast lookups
    const testPostcodes = ['50000', '40100', '10000'];

    console.log('\nFast lookups:');
    testPostcodes.forEach(pc => {
        const info = lookup.get(pc);
        if (info) {
            console.log(`  ${pc} -> ${info.city}, ${info.state} (${info.stateCode})`);
        } else {
            console.log(`  ${pc} -> Not found`);
        }
    });

    console.log();
}

// Run all examples
if (require.main === module) {
    exampleJsonSearch();
    exampleStateData();
    exampleValidate();
    exampleByState();
    exampleLookupMap();

    console.log('='.repeat(60));
    console.log('All examples completed!');
    console.log('='.repeat(60));
}

// Export functions for use as a module
module.exports = {
    validatePostcode,
    getCitiesByState,
    buildPostcodeLookup
};
