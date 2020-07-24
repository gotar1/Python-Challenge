# PyBank Data Code:
# csv filePath = C:\Users\tahir\Desktop\repos\Python-Challenge\PyBank\Resources\budget_data.csv
import os
import csv
# pybank_csv = os.path.join('..', 'Resources', 'budget_data.csv')
# V.S code csv filepath
pybank_csv = os.path.join('.', 'Desktop', 'repos', 'Python-Challenge', 'PyBank', 'Resources', 'budget_data.csv')
print(pybank_csv)
def Average(row): 
    return sum(row) / len(row) 
def average_change(row):
    new_lst = []
    for number in range(len(row)):
        if number < 0:
            new_lst.append(number)      
    return sum(new_lst)/len(new_lst)
def min(row):
    min = 0
    for number in range(len(row)):
        if number <= min:
            min = number
    return min
def max(row):
    max = 0
    for number in range(len(row)):
        if number >= max:
            max = number
    return max

# with open(pybank_csv) as csvfile:
#     fast_reader = csv.reader(csvfile, delimiter = ",") 
#     next(fast_reader, None)
    # print(csv_header)

    for row in fast_reader:
        # average = Average(row)
        total_months = len(str(row[0]))
    print("Total Months: ", total_months)
    print(f"{max(row[1])} {row[0]}")
    print(f"{min(row[1])} {row[0]}")
    print(average_change(row[1]))
    # print(average(row[1]))
with open(pybank_csv, 'r') as file_handler:
    lines = file_handler.read()
    csv_header = next(file_handler)
    print(csv_header)
    print(lines)
    print(type(lines))
   