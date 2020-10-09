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

    # Variable for Profit and Loss
    pl_change = []
    pl_new = []
    months = []
    

    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    num_rows = -1

    # Read each row of data after the header
    for row in csvreader:
        
        #
        num_rows += 1
# Count the total number of months included in the dataset (be sure not to include header row!)
        
#or row in open("pybank_Resources_budget_data.csv"):
        #num_rows += 1
        # Appending colum 1
        months.append(row[0])
# Calculate the Profits/Losses per month 
        pl_change.append(int(row[1]))

# Calculate the net total amount of "Profit/Losses" for entire dataset

    #total = sum(float(row["Profit/Losses"]) for row in csvreader)
    total  = sum(pl_change)
    total_months = len(months)


    
    for row in range(1,len(pl_change)):
        pl_new.append(int(pl_change[row])-(int(pl_change[row-1]))) 
        #print(pl_new)
    # Calculate the average change of the "Profit/Losses" column
    #avg_pl = round((total/num_rows),2)
    avg_pl = sum(pl_new)/len(pl_new)

# Determine the greatest increase in profits (date and amount) over the entire period
#with open("pybank_Resources_budget_data.csv") as csv_file:
    #reader = csv.DictReader(csv_file)
    #max_pl = max(float(row["Profit/Losses"]) for row in csvreader)
    max_pl = max(pl_new)
    min_pl = min(pl_new)

# Determine the greatest decrease in losses (date) over the entire period
    max_month = months[pl_new.index(max_pl) + 1]
    min_month = months[pl_new.index(min_pl) + 1]

# Print analysis table (with all calculate varaibles from above)
print("")
print('Financial Anlaysis')
print('-----------------------------------')
print('Total Months: ',num_rows) 
print("Total: $" + format(str(total))+"0")
print("Average Change: $" + str(round(avg_pl,2)))
print("Greatest Increase in Profits: " + str(max_month) + " $" +str(max_pl))
print(f"Greatest Decrease in Losses: {str(min_month)}  (${str(min_pl)})")
