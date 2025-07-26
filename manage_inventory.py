import csv
import os

threshold = 39

with open("inventory.csv", "r") as file:
    reader = csv.DictReader(file)
    data = list(reader)

item_types = {}
for row in data:
    item_type = row['ItemType']
    if item_type not in item_types:
        item_types[item_type] = []
    item_types[item_type].append(row)

for item_type, items in item_types.items():
    os.makedirs(item_type, exist_ok=True)

    report_path = f"{item_type}/{item_type}_report.csv"
    below_path = f"{item_type}/below_threshold.csv"
    above_path = f"{item_type}/above_threshold.csv"

    fieldnames = ['ItemID', 'ItemType', 'ItemName', 'Quantity', 'Price']

    report_file = open(report_path, 'w', newline='')
    below_file = open(below_path, 'w', newline='')
    above_file = open(above_path, 'w', newline='')

    report_writer = csv.DictWriter(report_file, fieldnames=fieldnames)
    below_writer = csv.DictWriter(below_file, fieldnames=fieldnames)
    above_writer = csv.DictWriter(above_file, fieldnames=fieldnames)

    report_writer.writeheader()
    below_writer.writeheader()
    above_writer.writeheader()

    for item in items:
        report_writer.writerow(item)
        qty = int(item['Quantity'])
        if qty < threshold:
            below_writer.writerow(item)
        else:
            above_writer.writerow(item)

    report_file.close()
    below_file.close()
    above_file.close()

print("Inventory processed successfully.")
