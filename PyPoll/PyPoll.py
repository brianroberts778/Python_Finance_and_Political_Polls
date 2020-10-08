# Import necessary modules
import os
import csv

# Create path to read provided CSV file
pypoll_csv = os.path.join('..','PyPoll', 'PyPoll_election_data.csv')

# Read using the CSV module
with open(pypoll_csv) as csvfile:

    # Specify delimiter and variable to hold contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)
        