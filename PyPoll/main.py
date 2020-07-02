#!/usr/bin/env python
# coding: utf-8

# In[11]:


import csv
import os


# In[12]:


election_path = os.path.join("Resources", "election_data.csv")
election_path


# In[13]:


#set counts
total_votes = 0
candidates = []
candidates_tally = {}

#reading csv file
with open(election_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #skipping header
    header = next(csvreader)
    
    #counting total votes
    for row in csvreader:
        total_votes += 1
        
        #print list of candidates
        name = row[2]
        
        if name not in candidates:
            candidates.append(name)
            candidates_tally[name] = 0
        candidates_tally[name] += 1
            
# print(total_votes)
# print(candidates)
# print(candidates_tally)


# In[14]:


#create out path and txt file
out_election = os.path.join("Analysis","PyPoll.txt")
#set count
winning_count = 0

#writing csv file
with open (out_election, "w") as datafile:
    datafile.write("Election Results\n")
    datafile.write("-------------------------\n")
    datafile.write(f"Total Votes: {total_votes}\n")
    datafile.write("-------------------------\n")
    
    #printing in terminal
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    
    #calculate percentage, write to csv and print to terminal
    for key, value in candidates_tally.items():
        percentage = (value / total_votes) * 100
        
        #write % to 3 decimal places per instructions
        datafile.write(f"{key}: {percentage:.3f}% ({value})\n")
        
        #write % to 3 decimal places per instructions
        print(f"{key}: {percentage:.3f}% ({value})")
        
        #still looping through and finding the winner
        if value > winning_count:
            winning_count = value
            winner = key
    
    #writing csv file and printing in terminal
    datafile.write("-------------------------\n")
    print("-------------------------")
    datafile.write(f"Winner: {winner}\n")
    datafile.write("-------------------------\n")
    print(f"Winner: {winner}")
    print("-------------------------")


# In[ ]:




