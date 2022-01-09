import questionary
from pathlib import Path
import csv

def save_qualified_loans_to_new_csv(list):
    csvpath_new = questionary.text("Enter a file path to save the qualified loans (.csv):").ask()
    csv_path = Path(csvpath_new)
    with open(csv_path, 'w', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        for row in list:
            writer.writerow(row)