# Import necessary modules
import os
import csv

# Create path to read provided CSV file
pybank_csv = os.path.join('..', 'PyBank', 'PyBank_Resources_budget_data.csv')


# Read using CSV module
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

# Count the total number of months included in the dataset (be sure not to include header row!)
num_rows = -1
for row in open("pybank_Resources_budget_data.csv"):
        num_rows += 1

# Calculate the net total amount of "Profit/Losses" for entire dataset
with open("pybank_Resources_budget_data.csv") as csv_file:
    reader = csv.DictReader(csv_file)
    total = sum(float(row["Profit/Losses"]) for row in reader)

# Print analysis table
print("")
print('Financial Anlaysis')
print('-----------------------------------')
print('Total Months: ',num_rows) 
print("Total: $" + format(str(total))+"0")


        