# PyPoll Data Code:
import os
import csv

# P.C bash terminal csv filepath:
# pybank_csv = os.path.join('..', 'Resources', 'election_data.csv')
# V.S code csv filepath:
# pypoll_csv = os.path.join('.', 'Desktop', 'repos', 'Python-Challenge', 'PyPoll', 'Resources', 'election_data.csv')
# analysis output filepath:
# analysis_text = os.path.join('.', 'Desktop', 'repos', 'Python-Challenge', 'PyPoll', 'analysis', 'pypoll_results.txt')
voter_dict = {}
candidate_names = voter_dict.items()
vote = voter_dict.values()
candidate_list = []
id_count = 0
total_vote = 0
f = open(analysis_text, 'a')
with open(pypoll_csv) as csvfile:
    poll_reader = csv.reader(csvfile, delimiter = ",") 
    csv_header = next(poll_reader)
    for row in poll_reader:
        id_count += 1
        name = row[2]
        if name not in candidate_list:
            candidate_list.append(name)
            voter_dict[name] = 0  
        voter_dict[name] += 1 
        total_vote = sum(vote)
        winner_max = max(vote)
    print("Election Results", file=f)
    print("-------------------------", file=f)
    print(f"Total Votes:  {total_vote}", file=f)
    print("-------------------------", file=f)
    for k, v in candidate_names:
        vote_percentage = round((v*100/total_vote), 3)
        print(f"{k}: {vote_percentage}% ({v})", file=f)
        if v == winner_max:
            winner = k
    print("-------------------------", file=f)
    print(f"Winner: {winner}", file=f)
    f.close()

        


    