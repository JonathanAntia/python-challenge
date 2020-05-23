# PyBank
# In this challenge, the task is to create a Python script for analyzing the financial records of a company. 
# The financial dataset to analyze is called budget_data.csv.
# The dataset is composed of two columns: Date and Profit/Losses.

# import os and csv modules
import os
import csv
import statistics

# indicate the path to the csv file using the os notation
csvpath = os.path.join('Resources', 'budget_data.csv')

# use the csv.reader function to read through the file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

# skip the header
    csv_header = next(csvreader)

# initialize empty lists to store the Dates and Profit/Loses data
    months = []
    profit = []
    
# populate the lists with values from each row in the csv file
    for row in csvreader:

        months.append(row[0])
        profit.append(int(row[1]))

# use len() and sum() functions to calculate total months and total profit
        total_num_months = len(months)
        total_profit = sum(profit)

# use item indices to calculate change from one item to the next in the profit list
    monthly_change = [] # this list stores the changes from one month to the next
    for i in range (0, len(profit)-1):
        monthly_change.append(profit[i+1] - profit[i]) 
        average_change = statistics.mean(monthly_change)
        greatest_increase = max(monthly_change)
        greatest_decrease = min(monthly_change)
# because change starts being recorded after the first month
# a +1 needs to be added to the greatest increase or greatest decrease index
# to get the correct index in the list of months[]
        greatest_month = months[monthly_change.index(greatest_increase)+1]
        worst_month = months[monthly_change.index(greatest_decrease)+1]

# the following commands print the results to the terminal
    print(f'Total Months: {total_num_months}')
    print(f'Total: ${total_profit}')
    print(f'Average Change: {average_change: .2f}')
    print(f'Greatest Increase in Profits: {greatest_month} (${greatest_increase})')
    print(f'Greatest Decrease in Profits: {worst_month} (${greatest_decrease})')


# path for the output file
output_path = os.path.join("analysis", "FinancialAnalysis.txt")

# create the file using "write" mode
with open(output_path, 'w') as txtfile:
    write_results = txtfile.write('Financial Analysis:\n'
    '------------------------------------\n'
    f'Total Months: {total_num_months}\n' 
    f'Total: ${total_profit}\n'
    f'Average Change: {average_change: .2f}\n'
    f'Greatest Increase in Profits: {greatest_month} (${greatest_increase})\n'
    f'Greatest Decrease in Profits: {worst_month} (${greatest_decrease})')
    