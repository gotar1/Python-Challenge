# import dependancies
import os
import csv

# P.C csv filepath:
# pybank_csv = os.path.join('..', 'Resources', 'election_data.csv')

# V.S code csv filepath:
# pypoll_csv = os.path.join('.', 'PyPoll', 'Resources', 'election_data.csv')

# analysis output filepath:
analysis_text = os.path.join('.', 'PyPoll', 'analysis', 'pypoll_results.txt')

# create empty lists to hold our values
voter_dict = {}
candidate_names = voter_dict.items()
vote = voter_dict.values()
candidate_list = []
id_count = 0
total_vote = 0

# open a file to save a text output
f = open(analysis_text, 'a')

# open csv file and read header
with open(pypoll_csv) as csvfile:
    poll_reader = csv.reader(csvfile, delimiter = ",") 
    csv_header = next(poll_reader)

    # loop through our files and do analysis
    for row in poll_reader:

        # keep track of id and names
        id_count += 1
        name = row[2]

        # populate cnadidate_list with names and add keys and values to voter dictionary
        if name not in candidate_list:
            candidate_list.append(name)
            voter_dict[name] = 0

        # calculate total votes for each candidate and maximum vote achieved.
        voter_dict[name] += 1 
        total_vote = sum(vote)
        winner_max = max(vote)

    # print total votes and save to output text file
    print("Election Results", file=f)
    print("-------------------------", file=f)
    print(f"Total Votes:  {total_vote}", file=f)
    print("-------------------------", file=f)

    # loop through candidate name list and do analysis on keys and values
    for k, v in candidate_names:

        # calculate vote percentage and print into text file
        vote_percentage = round((v*100/total_vote), 3)
        print(f"{k}: {vote_percentage}% ({v})", file=f)

        # find the election winner based on maximum votes
        if v == winner_max:
            winner = k

    # print winner name into text file
    print("-------------------------", file=f)
    print(f"Winner: {winner}", file=f)

    # close text file
    f.close()

        


    