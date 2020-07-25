# PyPoll Data Code:
# csv filePath = C:\Users\tahir\Desktop\repos\Python-Challenge\PyPoll\Resources\election_data.csv
import os
import csv
import numpy as np
# pybank_csv = os.path.join('..', 'Resources', 'election_data.csv')
# V.S code csv filepath
pypoll_csv = os.path.join('.', 'Desktop', 'repos', 'Python-Challenge', 'PyPoll', 'Resources', 'election_data.csv')
# def average(list1): 
#     return round((sum(list1) / len(list1)), 2)
# def unique(list1): 
#     unique_list = [] 
#     for x in list1: 
#         if x not in unique_list: 
#             unique_list.append(x) 
with open(pypoll_csv) as csvfile:
    poll_reader = csv.reader(csvfile, delimiter = ",") 
    csv_header = next(poll_reader)
    print(csv_header)
    for row in poll_reader:
        print(unique(row[2]))

    