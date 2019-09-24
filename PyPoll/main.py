#Python-Challenge No. 2: PyPoll 
#by Gerard Tieng

#---------------------------

#TASK A: Find the total number of votes cast
#TASK B: Make a complete list of candidates who received votes
#TASK C: Find the percentage of votes each candidate won plus the total number of votes each candidate won
#TASK D: The winner of the election based on popular vote.

#---------------------------

#Step 1: Import and open relevant libraries and files.
import os
import csv
import decimal
file = os.path.join("Resources", "election_data.csv")

#---------------------------

#Step 2: Set up empty containers and separate the columns into lists.

vote_list = [] #ANSWER A
candidates = [] #ANSWER B
vote_counter = [] #ANSWER B
percent = [] #ANSWER C
winner = [] #ANSWER D

#---------------------------

#Step 3: Open file to begin analyzing.
with open (file, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #NEXT the header
    next(csvreader)
    
    #TASK A:
    for vote in csvreader:
        vote_list.append(vote[2])


id_starter = 0
candidate_id = []

for check in vote_list:
    if check not in candidates:
        #TASK B-1: Compile list of available candidates by comparing analyzed entries against newly-appended entries.
        candidates.append(check)
        #TASK B-2: Append an index for each confirmed candidate to collect tallied votes.
        vote_counter.append(0)
        #TASK B-3: Assign each candidate an integer index.
        candidate_id.append(id_starter)
        id_starter = id_starter + 1



#TASK B-4: Use a while loop to set upper threshold of candidates when tallying votes.

counter_max = 0
while counter_max <= max(candidate_id):
    for tally in vote_list:
        if tally == candidates[counter_max]:
            vote_counter[counter_max] = vote_counter[counter_max] + 1
    counter_max = counter_max + 1

#TASK C
percent_max = 0
while percent_max <= max(candidate_id):
    percent.append(round((vote_counter[percent_max] / len(vote_list)) * 100, 3))
    percent_max = percent_max + 1

#TASK D
winner_max = 0
while winner_max <= max(candidate_id):
    for biggest in vote_counter:
        if vote_counter[winner_max] == max(vote_counter):
            winner = candidates[winner_max]
    winner_max = winner_max + 1

    
#Step 4: Print the results

#PRINT TO TERMINAL

print("Gerard's Election Results")
print("------------------------------")
print("Total Votes: " + str(len(vote_list)))
print("------------------------------")

print_max = 0
while print_max <= max(candidate_id):
    print(candidates[print_max] + ": " + str(percent[print_max]) + "%" + " (" + str(vote_counter[print_max]) + ")")
    print_max = print_max + 1

print("------------------------------")
print("Winner: " + winner)
print("------------------------------")


#WRITE TO FILE
        
with open ("PyPoll_output.txt", 'w') as f:

    f.write("Gerard's Election Results")
    f.write("\n")
    f.write("------------------------------")
    f.write("\n")
    f.write("Total Votes: " + str(len(vote_list)))
    f.write("\n")
    f.write("------------------------------")
    f.write("\n")
    
    write_max = 0
    while write_max <= max(candidate_id):
        f.write(candidates[write_max] + ": " + str(percent[write_max]) + "%" + " (" + str(vote_counter[write_max]) + ")")
        write_max = write_max + 1
        f.write("\n")
        
    f.write("------------------------------")
    f.write("\n")
    f.write("Winner: " + winner)
    f.write("\n")
    f.write("------------------------------")
