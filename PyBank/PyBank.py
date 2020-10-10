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

    # Variables for Months and Profit/Losses
    pl_change = []
    pl_new = []
    months = []
    num_rows = 0
    
    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        
        # Count the number of months in the dataset
        num_rows += 1

        # Appending columns from the dataset
        months.append(row[0])
        pl_change.append(int(row[1]))

    # Calculate the net total of Profit/Losses for the entire period
    total = sum(pl_change)
    
    # Determine the month-to-month change in Profit/Losses column to help calculate later objectives
    for row in range(1,len(pl_change)):
        pl_new.append(int(pl_change[row])-(int(pl_change[row-1]))) 
        
    # Calculate the average change of the "Profit/Losses" column
    avg_pl = sum(pl_new)/len(pl_new)

    # Determine the greatest increase and greatest loss from the entire dataset for a single month
    max_pl = max(pl_new)
    min_pl = min(pl_new)
    # Determine which month these maximum and minimum values occured during and print together
    max_month = months[pl_new.index(max_pl) + 1]
    min_month = months[pl_new.index(min_pl) + 1]

# Print analysis table (with all calculate varaibles from above)
print("")
print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {num_rows}") 
print(f"Total: ${format(str(total))}")
print(f"Average Change: ${str(round(avg_pl,2))}")
print(f"Greatest Increase in Profits: {str(max_month)} (${str(max_pl)})")
print(f"Greatest Decrease in Losses: {str(min_month)} (${str(min_pl)})")

# Have code create/export a text file containing the analysis table when run
pybank_analysis = os.path.join('..', 'PyBank', 'pybank_analysis.txt')
with open(pybank_analysis, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("-----------------------------------\n")
    outfile.write(f"Total Months: {num_rows}\n") 
    outfile.write(f"Total: ${format(str(total))}\n")
    outfile.write(f"Average Change: ${str(round(avg_pl,2))}\n")
    outfile.write(f"Greatest Increase in Profits: {str(max_month)} (${str(max_pl)})\n")
    outfile.write(f"Greatest Decrease in Losses: {str(min_month)} (${str(min_pl)})\n")