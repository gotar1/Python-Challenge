# PyPoll Data Code:
# csv filePath = C:\Users\tahir\Desktop\repos\Python-Challenge\PyPoll\Resources\election_data.csv
import os
import csv
# pybank_csv = os.path.join('..', 'Resources', 'election_data.csv')
# V.S code csv filepath
pypoll_csv = os.path.join('.', 'Desktop', 'repos', 'Python-Challenge', 'PyPoll', 'Resources', 'election_data.csv')

# def unique(list1): 
#     unique_list = [] 
#     for i in list1: 
#         if i not in unique_list: 
#             unique_list.append(i) 
voter_dict = {}
candidate_list = []
id_count = 0
with open(pypoll_csv) as csvfile:
    poll_reader = csv.reader(csvfile, delimiter = ",") 
    csv_header = next(poll_reader)
    # print(csv_header)
    for row in poll_reader:
        id_count += 1
        name = row[2]
        if name not in candidate_list:
            candidate_list.append(name)
            voter_dict[name] = 0
        voter_dict[name] += 1 
print(voter_dict)

        


    