# PyBank Data Code:
# csv filePath = C:\Users\tahir\Desktop\repos\Python-Challenge\PyBank\Resources\budget_data.csv
import os
import csv
# pybank_csv = os.path.join('..', 'Resources', 'budget_data.csv')
# V.S code csv filepath
pybank_csv = os.path.join('.', 'Desktop', 'repos', 'Python-Challenge', 'PyBank', 'Resources', 'budget_data.csv')
def average(list1): 
    return round((sum(list1) / len(list1)), 2)
with open(pybank_csv) as csvfile:
    fast_reader = csv.reader(csvfile, delimiter = ",") 
    total_month = 0
    nimir = []
    new_list = []
    positive_numbers = []
    negative_numbers = []
    csv_header = next(fast_reader)
    # print(lines)
    # print(csv_header)
    # print(lines)
    # print(type(lines))
    for row in fast_reader:
        total_month += 1
        new_list.append(int(row[1]))
        if int(row[1]) >= 0:
            positive_numbers.append(int(row[1]))
            greatest_increase = max(positive_numbers)
            juan = (row[0])
        elif int(row[1]) < 0:   
            negative_numbers.append(int(row[1]))
            greatest_decrease = min(negative_numbers)
    print(f"Total Months: {len(new_list)}")       
    print(f"Total: ${sum((new_list))}")
    print(f"Average Change:  ${average((negative_numbers))}")
    print(f"Greatest Increase in Profits:  {row[0]} (${greatest_increase})")
    print(f"Greatest Decrease in Profits:  {row[0]} (${greatest_decrease})")
 
    # print(negative_numbers)
    

   