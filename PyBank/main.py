# PyBank Data Code:
# import dependencies..
import os
import csv

# P.C csv filepath:
# pybank_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# V.S code csv filepath:
# pybank_csv = os.path.join('.', 'PyBank', 'Resources', 'budget_data.csv')

# analysis output filepath:
analysis_text = os.path.join('.', 'PyBank', 'analysis', 'pybank_results.txt')

# function to define average
def average(list1): 
    return round((sum(list1) / len(list1)), 2)

# open a file to save a text output
f = open(analysis_text, 'a')

# create empty lists to store values from analysis
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0

# Read csv file and convert to list of dictionaries
with open(pybank_csv) as csvfile:
    bank_reader = csv.reader(csvfile, delimiter = ",")

    #  Read header row 
    csv_header = next(bank_reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(bank_reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    # do a for loop to render our data and do anaysis
    for row in bank_reader:

        # Track the total
        total_months += 1
        total_net += int(row[1])

        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]
        print(net_change_list)

        # Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Calculate the greatest decrease
        elif net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# calculate average change using defined average function.
average_change = average(net_change_list)

# print values to a text file..
print("Financial Analysis", file=f)
print("----------------------------", file=f)
print(f"Total Months: {total_months}", file=f)       
print(f"Total: ${total_net}", file=f)
print(f"Average Change:  ${average_change}", file=f)
print(f"Greatest Increase in Profits:  {greatest_increase[0]} (${greatest_increase[1]})", file=f)
print(f"Greatest Decrease in Profits:  {greatest_decrease[0]} (${greatest_decrease[1]})", file=f)

# close text file
f.close()   
    

   