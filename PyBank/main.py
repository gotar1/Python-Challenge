# PyBank Data Code:
# csv filePath = C:\Users\tahir\Desktop\repos\Python-Challenge\PyBank\Resources\budget_data.csv

import os
import csv
csvpath = os.path.join('.', 'Desktop', 'repos', 'Python-Challenge', 'PyBank', 'Resources', 'budget_data.csv')
def Average(row): 
    return sum(row) / len(row) 
with open(csvpath) as csvfile:
    fast_reader = csv.reader(csvfile, delimiter = ",") 
    next(fast_reader, None)
    # print(csv_header)

    for row in fast_reader:
        # average = Average(row)
        total_months = len(row[0])
    print("Total Months: ", total_months)
    # print(average(row[1]))
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     csv_header = next(file_handler)
#     print(csv_header)
#     print(lines)
#     print(type(lines))
   