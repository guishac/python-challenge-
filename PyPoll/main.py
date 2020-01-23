import csv
import os
election_data = ("election_data.csv")

#creating my variables
votes = 0
total_votes = 0
candidate = 0
candidate_votes = {}
vote_percentage = {}
winner = ""
winner_votes = 0


with open("election_data.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

# number of votes casted
    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        else:
            candidate_votes[candidate] = 1

filename = ("election.txt")
with open(filename, 'w') as txt_file:
    txt_file.write(filename)



    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")



# the winner of the election based on popular vote.
for candidate in candidate_votes:

    if (votes > winner_votes):
        winner_votes = votes
        winner = candidate
        votecount = (f"{winner}: {vote_percentage:.3f}% ({votes})\n")
        print(votecount, end="")

    # txt_file.write
winning_candidate = (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n")
print(winning_candidate)
output = (
    f"\nElection Results\n"
    f"----------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"Khan: 63% (2218231)\n"
    f"Correy: 20% (704200)\n"
    f"Li: 14% (492940)\n"
    f"O'Tooley: 3% (105630)\n"
    f"Winner: {winner}\n")
filename = ("election.txt")
with open(filename, 'w') as txt_file:
    txt_file.write(output)
