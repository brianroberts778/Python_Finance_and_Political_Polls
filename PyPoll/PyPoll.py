# Import necessary modules
import os
import csv

# Define Variables for later use 
csv_votes = []
csv_candidates = []
khan = []
correy = []
li = []
otooley = []

# Create path to read provided CSV file
pypoll_csv = os.path.join('..','PyPoll', 'PyPoll_election_data.csv')


# Read file using the CSV module
with open(pypoll_csv) as csvfile:

    # Specify delimiter and variable to hold contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Append columns (Omitted 'County' because it does not apply to our analysis)
    for column in csvreader:
        csv_votes.append(column[0])
        csv_candidates.append(column[2])

    # Calculate the total number of votes cast
    All_Votes = len(csv_votes)

    for candidate in csv_candidates:

        if candidate == "Khan":
            khan.append(csv_candidates)
            khan_votes = len(khan)

        elif candidate == "Correy":
            correy.append(csv_candidates)
            correy_votes = len(correy)

        elif candidate == "Li":
            li.append(csv_candidates)
            li_votes = len(li)

        else:
            otooley.append(csv_candidates)
            otooley_votes = len(otooley)

    # Percent
    khan_percent = (khan_votes)/(All_Votes)
    correy_percent = (correy_votes)/(All_Votes)
    li_percent = (li_votes)/(All_Votes)
    otooley_percent = (otooley_votes)/(All_Votes)

    if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
    elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"
    elif li_percent > max(khan_percent, correy_percent, otooley_percent):
        winner = "Li"
    else: 
        winner = "Otooley"

        # Determine the total numeber of votes received by each candidate
        

    
        


# Print Analysis Table
print("")
print("Election Results")
print("------------------------------")
print(f"Total Votes: {str(All_Votes)}")
print("------------------------------")
print(f"Khan: {khan_percent}% ({khan_votes})")
print(f"Correy: {correy_percent}% ({correy_votes})")
print(f"Li: {li_percent}% ({li_votes})")
print(f"O'Tooley: {otooley_percent}% ({otooley_votes})")
