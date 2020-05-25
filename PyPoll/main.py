# 1. Import dependencies: os and csv
# 2. Create a csv_path variable to connect to the csv file using os.path.join
# 3. With open csv_path as file apply a reader funtion to the csv file: csv.reader
# 4. skip the header row
# 5. Count the total number of votes (rows) in the csv file
# 6. Create a list of all the unique names in the candicates column
# 7. Count the votes per candidate and calculate the percentage
# 8. Identify the highest percentage of votes and declare a winner

# dependencies

import os
import csv

# file path

csv_path = os.path.join ('Resources','election_data.csv')

# open and read csv file

with open (csv_path, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter = ',')

# skip the header row

    csv_header = next(csvreader)

# cound the total number of votes using a counter variable
# initicallize the counter at zero

    total_votes = []
    candidate_names = []
    votes_per_candidate = []
    percentage_per_candidate = []

    for row in csvreader:
        total_votes.append(row[2])

        if row[2] not in candidate_names:
            candidate_names.append(row[2])

    for names in candidate_names:
        votes_per_candidate.append(total_votes.count(names))

    for votes in range (0, len(votes_per_candidate)):
        percentage_per_candidate.append(votes_per_candidate[votes]*100/len(total_votes))

    print(candidate_names)
    print(votes_per_candidate)
    print(percentage_per_candidate)
    print("Election Results")
    print("-----------------------")
    print(f'Total Votes: {len(total_votes)}') 
    print("-----------------------")  
    for i in range (0, len(candidate_names)):
        print(f'{candidate_names[i]}: {percentage_per_candidate[i]}% , ({votes_per_candidate[i]} votes)')
    print("-----------------------")
    print("Winner: ")
    print("-----------------------")
