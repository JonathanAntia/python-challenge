# PyBank
# In this challenge, the task is to create a Python script for analyzing the financial records of a company. 
# The financial dataset to analyze is called budget_data.csv.
# The dataset is composed of two columns: Date and Profit/Losses.

# import os and csv modules
import os
import csv

# indicate the path to the csv file using the os notation
csvpath = os.path.join('Resources', 'budget_data.csv')

# use the csv.reader function to read through the file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

# skip the header
    csv_header = next(csvreader)

# use a for loop to count the remaining number of rows in the file
# start the counter at zero
    total_num_months = 0
    for rows in csvreader:
        total_num_months += 1
    print(total_num_months)

# sum the values in the Profit/Loses column to calculate the total amount

# calculate the mean for of the Profit/Loses over the entire period

# find the max Profit/Loses and print it along with the date of its occurrence

# find the min Profit/Loses and print it along with the date of its occurrence