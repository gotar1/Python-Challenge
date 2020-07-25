# PyPoll Data Code:
# csv filePath = C:\Users\tahir\Desktop\repos\Python-Challenge\PyPoll\Resources\election_data.csv
import os
import csv
from collections import Counter
# import numpy as np
# pybank_csv = os.path.join('..', 'Resources', 'election_data.csv')
# V.S code csv filepath
pypoll_csv = os.path.join('.', 'Desktop', 'repos', 'Python-Challenge', 'PyPoll', 'Resources', 'election_data.csv')
# def unique(list1): 
#     unique_list = [] 
#     for i in list1: 
#         if i not in unique_list: 
#             unique_list.append(i) 
candidate_list = []
votes_list = []
counter = 0
new_list = []
total_month = 0
with open(pypoll_csv) as csvfile:
    poll_reader = csv.reader(csvfile, delimiter = ",") 
    csv_header = next(poll_reader)
    print(csv_header)
    for row in poll_reader:
        new_list.append(str(row[2]))
        gt = Counter(new_list).keys() 
        mag = Counter(new_list).values()
        print(gt)
        print(mag)
        # total_month += 1
        
        # for name in new_list:
        #     if name not in candidate_list:
        #         counter += 1
        #     else:
        #         candidate_list.append(name)
        # print(candidate_list)
        # print(new_list)


    