# Step 1: Import relevant libraries & files.
import os
import csv
file = os.path.join("Resources", "budget_data.csv")


# Step 2: Set empty lists and variables to fill with future calculations.

#A
months_list = []
months = 0

#B
revenue_list = []
rev_counter = 0

#C
change_list = []
change_counter = 0
pastvalue_pointer = 0
presentvalue_pointer = 1


# Step 3: Open the CSV file to start working with the dataset.
with open (file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Next the HEADER to work exclusively with the data
    next(csvreader)
    
    # Step 4: Begin looping through data
    for row in csvreader:
        
# -----------------------------------------
        
    
        # TASK A: Add 1 to "months" for every iteration in the CSV
        months_list.append(row[0])
    
    
# -----------------------------------------
    
    
        #TASK B-1: Separate the "revenue" column into its own list.
        revenue_list.append(row[1])
        
#TASK B-2: Convert the "revenue" column from string to integer to get sum.
revlist_convert = [int(revenue) for revenue in revenue_list]    

# TASK B-3: Use loop counter to calculate "revenue" sum and store it in a new variable.
for i in revlist_convert:
    rev_counter = rev_counter + i
    

# -----------------------------------------


# TASK C-1: Use a loop to create a list based on the "converted revenue" to hold "average changes".
for j in revlist_convert:
    
    # TASK C-2: Add IF conditional to avoid error (ending calculations at end of CSV)
    if presentvalue_pointer < len(revlist_convert):
        
        # TASK C-3: Calculate difference from past and present value.
        change = revlist_convert[presentvalue_pointer] - revlist_convert[pastvalue_pointer]
        
        # TASK C-4: Move counter value for next calculation.
        presentvalue_pointer = presentvalue_pointer + 1
        pastvalue_pointer = pastvalue_pointer + 1
        
        # TASK C-5: Add each average change calculation to list.
        change_list.append(change)
        
# TASK C-6: Use loop counter to calculate "average change" sum and store it in a new variable.  
for k in change_list:
    change_counter = change_counter + k
    
    
# -----------------------------------------


# TASK D/E-1: Find the minimum and maximum values in the "average change" list.
maxchange_value = (max(change_list))
minchange_value = (min(change_list))

# TASK D/E-2: Locate the corresponding months for maximum and minimum in the "months list".
maxmonth = months_list[(change_list.index(maxchange_value)) + 1]
minmonth = months_list[(change_list.index(minchange_value)) + 1]


# -----------------------------------------

    
#Step 5: Print the results.

#Printing in terminal
print("Gerard's Financial Analysis")
print("---------------------------")
print("Total Months: " + str(len(months_list))) #TASK A - COMPLETE
print("Total Revenue: " + "$" + str(rev_counter)) #TASK B - COMPLETE
print("Average Change: " + "$" + str(change_counter/len(change_list))) #TASK C - COMPLETE
print("Greatest Increase in Profits: " + maxmonth + " ($"+ str(maxchange_value) + ")") #TASK D - COMPLETE
print("Greatest Decrease in Profits: " + minmonth + " ($"+ str(minchange_value) + ")") #TASK E - COMPLETE


#Printing in separate .txt file

with open("PyBankOutput.txt", 'w') as f:

    f.write("Gerard's Financial Analysis\n")
    f.write("---------------------------\n")
    f.write("Total Months: " + str(len(months_list)))
    f.write("\n")
    f.write("Total Revenue: " + "$" + str(rev_counter))
    f.write("\n")
    f.write("Average Change: " + "$" + str(change_counter/len(change_list))) 
    f.write("\n")
    f.write("Greatest Increase in Profits: " + maxmonth + " ($"+ str(maxchange_value) + ")")
    f.write("\n")
    f.write("Greatest Decrease in Profits: " + minmonth + " ($"+ str(minchange_value) + ")")
