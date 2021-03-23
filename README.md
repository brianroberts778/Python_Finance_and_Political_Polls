# PyBank & PyPoll, Python Projects
Two part project involving one script for analyzing financial records, and one for modernizing a rural town's vote counting process.

PyBank: A script that analyzes a csv file pertaining to the Profit and Losses of an unamed company over a set of months. 
The script intially imports a few modules pertaining to csv reading and writing and sets variable for late analyses. 
Csv then becomes the focus with an external csv file being read, delimiter specified, header read and columns appended.
The total number of months was found using a for loop. Then the net total of the Profit/Losses column was found via the sum function being applied to the list of that column.
Another for loop was used to subtract the previous month's prof/loss from the current each time to determine the relative values for this column.
This made it possible to use sum of the P/L(Profits/Losses) divided by the len(length) of the appended column to determine the average P/L each month.
The max and min functions were applied to the "new" P/L column to determine the most and least successful months for the company. 
An index was used to find the months associated with the min and max P/L values.
Finally, a set of print funcions produced the final analysis table. 
Finally, the content of the analysis table was exported to a .txt file 

PyPoll: A script intended to help a small rural town modernize its vote counting process.
The script intially imports a few modules pertaining to csv reading and writing and sets variable for late analyses. 
The provided csv file, was then read into python, had a delimiter set, and columns appended.
The len funtion was used on the appended columns to determine the total of all cast votes. 
A for loop was created to run through the entire dataset and count the amount of times each candidate received a vote,...
...storing these counts into candidate-specific variables. 
The percentage each candidate received of the total vote count was established by simply dividing the candidate counts by the total count.
A conditional was then run to determine the winner based on comparing the cadidate voting percentages calculated.
Finally, the results found were printed into the terminal, along with a text file being written and exported when the code is run, similar to PyBank's code.



