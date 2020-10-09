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

    # Calculate the average change of the "Profit/Losses" column
    avg_pl = round((total/num_rows),2)

# Determine the greatest increase in profits (date and amount) over the entire period
with open("pybank_Resources_budget_data.csv") as csv_file:
    reader = csv.DictReader(csv_file)
    max_pl = max(float(row["Profit/Losses"]) for row in reader)

# Determine the greatest decrease in losses (date and amount) over the entire period
with open("pybank_Resources_budget_data.csv") as csv_file:
    reader = csv.DictReader(csv_file)
    min_pl = min(float(row["Profit/Losses"]) for row in reader)

# Print analysis table (with all calculate varaibles from above)
print("")
print('Financial Anlaysis')
print('-----------------------------------')
print('Total Months: ',num_rows) 
print("Total: $" + format(str(total))+"0")
print("Average Change: $" + str(avg_pl))
print("Greatest Increase in Profits: $" + str(max_pl) + "0")
print("Greatest Decrease in Losses: $" + str(min_pl) + "0")
