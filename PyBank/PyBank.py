# Import necessary modules
import os
import csv

# Create path to read CSV file
pybank_csv = os.path.join('..', 'PyBank', 'PyBank_Resources_budget_data.csv')


# Read using CSV Module
with open(pybank_csv) as csvfile:

    # Specify delimiter and variable to hold contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

        