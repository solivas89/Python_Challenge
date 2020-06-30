#!/usr/bin/env python
# coding: utf-8

# In[118]:


import csv
import os


# In[119]:


#setting the path
budget_path = os.path.join("Resources", "budget_data.csv")
budget_path


# In[120]:


#establish counts and set lists to append into
total_months = 0
net_amount = 0
changes = []
months = []

#open read file path
with open(budget_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #skipping header row
    header = next(csvreader)
    
    #loop through the data
    for line in csvreader:
        #need to calculate total_months
        total_months += 1
        
        #need to calculate net_amount in [1]
        net_amount += int(line[1])
        
        #need to establish previous months revenue
        if total_months == 1:
            prev_revenue = int(line[1])
        
        #need to append into changes and months index's for average_change calculation
        if total_months > 1:
            monthly_change = int(line[1])-prev_revenue
            changes.append(monthly_change)
            months.append(line[0])
            prev_revenue = int(line[1])
    
    #calculate average_change    
    for x in range(len(amount)):
        changes.append(amount[x]-pre_revenue)
        prev_revenue = amount[x]
    average_change = sum(changes)/(total_months-1)      
    
    #need to find greatest increase in profits (date & amount) in changes index
    grt_incr = max(changes)
    grt_incr_date = str(months[changes.index(max(changes))])
    
    grt_decr = min(changes)
    grt_decr_date = str(months[changes.index(min(changes))])
    
# print(total_months)
# print(net_amount)    
# print(len(changes), len(months))
# print(average_change)
# print(changes[0], months[0])
# print(grt_decr)
# print(grt_decr_date)


# In[114]:


#print out analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {(total_months)}")
print(f"Total: ${(net_amount)}")
print(f"Average  Change: ${round((average_change),2)}")
print(f"Greatest Increase in Profits: {grt_incr_date} (${grt_incr})")
print(f"Greatest Decrease in Profits: {grt_decr_date} (${grt_decr})")


# In[117]:


#write rows to txt file
out_budget_path = os.path.join("Analysis", "PyBank.txt")
with open(out_budget_path, "w") as datafile:
    writer = csv.writer(datafile,delimiter=",")
    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------------"])
    writer.writerow([f"Total Months: {(total_months)}"])
    writer.writerow([f"Total: ${(net_amount)}"])
    writer.writerow([f"Greatest Increase in Profits: {grt_incr_date} (${grt_incr})"])
    writer.writerow([f"Greatest Decrease in Profits: {grt_decr_date} (${grt_decr})"])


# In[ ]:




