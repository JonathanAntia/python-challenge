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

# create empty lists to hold the candicate names, votes, and percentages

    total_votes = []
    candidate_names = []
    votes_per_candidate = []
    percentage_per_candidate = []

# loop through the data provided to populate the list created above

    for row in csvreader:
        total_votes.append(row[2])

        if row[2] not in candidate_names:
            candidate_names.append(row[2])

    for names in candidate_names:
        votes_per_candidate.append(total_votes.count(names))

    for votes in range (0, len(votes_per_candidate)):
        percentage_per_candidate.append(votes_per_candidate[votes]*100/len(total_votes))

# print the results of the election to the terminal        

    print("Election Results")
    print("------------------------------")
    print(f'Total Votes: {len(total_votes)}') 
    print("------------------------------")
    for i in range (0, len(candidate_names)):
        print(f'{candidate_names[i]}: {percentage_per_candidate[i]: .3f}% , ({votes_per_candidate[i]})')
    print("------------------------------")
    print(f'Winner: {candidate_names[votes_per_candidate.index(max(votes_per_candidate))]}')
    print("------------------------------")

# print the results in a text file

# path for the output file
output_path = os.path.join("analysis", "ElectionResults.txt")

# create the file using "write" mode
with open(output_path, 'w') as txtfile:
    write_results = txtfile.write('Election Results:\n'
    '------------------------------\n'
    f'Total Votes: {len(total_votes)})\n'
    '------------------------------\n'
    for i in range (0,len(candicate_names)):f'{candidate_names[i]}: {percentage_per_candidate[i]: .3f}% , ({votes_per_candidate[i]})\n'
    '------------------------------\n'
    f'Winner: {candidate_names[votes_per_candidate.index(max(votes_per_candidate))]}\n'
    '------------------------------\n')
