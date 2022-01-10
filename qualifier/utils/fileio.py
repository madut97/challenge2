# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
import questionary
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(list):
    """Asks the user to enter a file path to a .csv file to store the list of qualified loans.

    Args:
        qualifying_loans: List of qualified loaners for the user, if any exists.
    
    Returns:
        A list of qualifying bank loans.
    """
    csvpath_new = questionary.text("Enter a file path to save the qualified loans (.csv):").ask()
    csv_path = Path(csvpath_new)
    with open(csv_path, 'w', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        for row in list:
            writer.writerow(row)