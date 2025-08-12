import csv
import json

# Read CSV file
with open("data.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)  # DictReader har row ko dict me convert karta hai
    data_list = list(csv_reader)  # saari rows ek list me daal di

# Save as JSON
with open("data.json", "w") as json_file:
    json.dump(data_list, json_file, indent=4)

print("CSV to JSON conversion complete. data.json file is made.")