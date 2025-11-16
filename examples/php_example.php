<?php
/**
 * Malaysia Postcode Usage Examples - PHP
 *
 * This file demonstrates various ways to use the Malaysia postcode data in PHP.
 *
 * To run these examples:
 *   php php_example.php
 */

// Example 1: Load and search JSON data
function exampleJsonSearch() {
    echo str_repeat('=', 60) . "\n";
    echo "Example 1: Search postcodes in JSON format\n";
    echo str_repeat('=', 60) . "\n";

    // Load complete postcode data
    $json = file_get_contents('../data/json/postcodes.json');
    $data = json_decode($json, true);

    // Search for a specific city
    $searchCity = 'Kuala Lumpur';

    foreach ($data['states'] as $state) {
        foreach ($state['cities'] as $city) {
            if (stripos($city['name'], $searchCity) !== false) {
                echo "\nState: {$state['name']} ({$state['code']})\n";
                echo "City: {$city['name']}\n";
                $postcodes = array_slice($city['postcodes'], 0, 10);
                echo "Postcodes: " . implode(', ', $postcodes) . "...\n";
                echo "Total: " . count($city['postcodes']) . " postcodes\n";
            }
        }
    }

    echo "\n";
}

// Example 2: Load state-specific data
function exampleStateData() {
    echo str_repeat('=', 60) . "\n";
    echo "Example 2: Load state-specific data\n";
    echo str_repeat('=', 60) . "\n";

    // Load Johor data
    $json = file_get_contents('../data/json/states/johor.json');
    $johor = json_decode($json, true);

    echo "\nState: {$johor['name']} ({$johor['code']})\n";
    echo "Total cities: " . count($johor['cities']) . "\n";
    echo "\nFirst 5 cities:\n";

    $cities = array_slice($johor['cities'], 0, 5);
    foreach ($cities as $city) {
        $first = $city['postcodes'][0];
        $last = $city['postcodes'][count($city['postcodes']) - 1];
        $count = count($city['postcodes']);
        printf("  - %-30s (%3d postcodes) [%s - %s]\n",
               $city['name'], $count, $first, $last);
    }

    echo "\n";
}

// Example 3: Read CSV data
function exampleCsvRead() {
    echo str_repeat('=', 60) . "\n";
    echo "Example 3: Read and filter CSV data\n";
    echo str_repeat('=', 60) . "\n";

    // Read postcodes CSV
    $postcodes = [];
    if (($handle = fopen('../data/csv/postcodes.csv', 'r')) !== false) {
        $header = fgetcsv($handle);
        while (($row = fgetcsv($handle)) !== false) {
            $postcodes[] = array_combine($header, $row);
        }
        fclose($handle);
    }

    // Filter by state
    $kelantan = array_filter($postcodes, function($p) {
        return $p['state_code'] === 'KTN';
    });

    echo "\nTotal postcodes in Malaysia: " . count($postcodes) . "\n";
    echo "Postcodes in Kelantan: " . count($kelantan) . "\n";
    echo "\nFirst 5 Kelantan postcodes:\n";

    $i = 0;
    foreach ($kelantan as $p) {
        if ($i++ >= 5) break;
        echo "  {$p['postcode']} - {$p['city']}, {$p['state']}\n";
    }

    echo "\n";
}

// Example 4: Validate a postcode
function validatePostcode($postcode) {
    $json = file_get_contents('../data/json/postcodes.json');
    $data = json_decode($json, true);

    foreach ($data['states'] as $state) {
        foreach ($state['cities'] as $city) {
            if (in_array($postcode, $city['postcodes'])) {
                return [
                    'valid' => true,
                    'city' => $city['name'],
                    'state' => $state['name'],
                    'state_code' => $state['code']
                ];
            }
        }
    }

    return ['valid' => false];
}

function exampleValidate() {
    echo str_repeat('=', 60) . "\n";
    echo "Example 4: Validate postcodes\n";
    echo str_repeat('=', 60) . "\n";

    $testPostcodes = ['50000', '10000', '99999', '40100'];

    foreach ($testPostcodes as $pc) {
        $result = validatePostcode($pc);
        if ($result['valid']) {
            echo "\n✓ $pc is valid\n";
            echo "  City: {$result['city']}\n";
            echo "  State: {$result['state']} ({$result['state_code']})\n";
        } else {
            echo "\n✗ $pc is not valid\n";
        }
    }

    echo "\n";
}

// Example 5: Get postcodes by state
function getPostcodesByState($stateCode) {
    $postcodes = [];
    if (($handle = fopen('../data/csv/postcodes.csv', 'r')) !== false) {
        $header = fgetcsv($handle);
        while (($row = fgetcsv($handle)) !== false) {
            $data = array_combine($header, $row);
            if ($data['state_code'] === $stateCode) {
                $postcodes[] = $data;
            }
        }
        fclose($handle);
    }
    return $postcodes;
}

function exampleByState() {
    echo str_repeat('=', 60) . "\n";
    echo "Example 5: Get postcodes by state\n";
    echo str_repeat('=', 60) . "\n";

    $stateCode = 'MLK'; // Melaka
    $postcodes = getPostcodesByState($stateCode);

    echo "\nPostcodes in $stateCode:\n";
    echo "Total: " . count($postcodes) . "\n";

    // Group by city
    $cities = [];
    foreach ($postcodes as $p) {
        $city = $p['city'];
        if (!isset($cities[$city])) {
            $cities[$city] = [];
        }
        $cities[$city][] = $p['postcode'];
    }

    ksort($cities);

    echo "\nCities: " . count($cities) . "\n";
    foreach ($cities as $city => $pcs) {
        printf("  %-30s %3d postcodes\n", $city, count($pcs));
    }

    echo "\n";
}

// Run all examples
if (php_sapi_name() === 'cli') {
    exampleJsonSearch();
    exampleStateData();
    exampleCsvRead();
    exampleValidate();
    exampleByState();

    echo str_repeat('=', 60) . "\n";
    echo "All examples completed!\n";
    echo str_repeat('=', 60) . "\n";
}
