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

# Create path to read CSV file
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

    # Create a for loop that contains a conditional, which will run through the dataset...
    # ...and extract the amount of times each candidate received a vote
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

    # Use the total votes and the amount of votes each candidate received above...
    # ...to determine the percentage of total votes each candidate received
    khan_percent = (khan_votes)/(All_Votes)
    correy_percent = (correy_votes)/(All_Votes)
    li_percent = (li_votes)/(All_Votes)
    otooley_percent = (otooley_votes)/(All_Votes)

    # Create a confitional to determine the winner of the election based on percentages from above
    if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
    elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"
    elif li_percent > max(khan_percent, correy_percent, otooley_percent):
        winner = "Li"
    else: 
        winner = "Otooley"

    
# Print Analysis Table
print("")
print("Election Results")
print("------------------------------")
print(f"Total Votes: {str(All_Votes)}")
print("------------------------------")
print(f"Khan: {str(round(khan_percent,3)*100)}% ({khan_votes})")
print(f"Correy: {str(round(correy_percent,3)*100)}% ({correy_votes})")
print(f"Li: {str(round(li_percent,3)*100)}% ({li_votes})")
print(f"O'Tooley: {str(round(otooley_percent,3)*100)}% ({otooley_votes})")
print("------------------------------")
print(f"Winner: {winner}")
print("------------------------------")

# Have code create/export a text file containing the analysis table when run
pypoll_analysis = os.path.join('..', 'PyPoll', 'pypoll_analysis.txt')
with open(pypoll_analysis, "w") as outfile:

    outfile.write("Election Results\n")
    outfile.write("------------------------------\n")
    outfile.write(f"Total Votes: {str(All_Votes)}\n") 
    outfile.write("------------------------------\n")
    outfile.write(f"Khan: {str(round(khan_percent,3)*100)}00% ({khan_votes})\n")
    outfile.write(f"Correy: {str(round(correy_percent,3)*100)}00% ({correy_votes})\n")
    outfile.write(f"Li: {str(round(li_percent,3)*100)}% ({li_votes})\n")
    outfile.write(f"O'Tooley: {str(round(otooley_percent,3)*100)}00% ({otooley_votes})\n")
    outfile.write("------------------------------\n")
    outfile.write(f"Winner: {winner}\n")
    outfile.write("------------------------------\n")
