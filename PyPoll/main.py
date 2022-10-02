import os, csv  # Import dependencies.

# Direct to and open 'election_data.csv'.
csv_file_path = os.path.join('Resources', 'election_data.csv')
with open(csv_file_path, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Obtain header row and indexes of needed columns.
    header = next(csv_reader)
    candidate_index = header.index('Candidate')

    # Initialize the Candidates Dictionary ("candidate_dict"): Track each candidate by total number of votes.
    candidate_dict = {} 

    # Loop through each row in 'election_data.csv', excluding header row.
    for row in csv_reader:

        # Store candidate name.
        row_candidate = row[candidate_index]

        # Check if candidate is in the Candidates Dictionary.
        if row_candidate in candidate_dict: # If so, add to candidate's total votes.
            candidate_dict[row_candidate] += 1
        else:   # If not, add the candidate to the Candidates Dictionary and start the candidate's total votes at 1.
            candidate_dict[row_candidate] = 1

    # Calculate total number of votes.
    total_votes = sum(candidate_dict.values())

    # Set up initial Election Results in list.
    election_results = [    
        "Election Results",
        "-------------------------",
        f"Total Votes: {total_votes}",
        "-------------------------"
    ]

    # Calculate each candidate's percentage of votes won, and store to the Election Results list in desired output.
    for candidate in candidate_dict:
        election_results.append(f"{candidate}: {'{0:.3%}'.format(candidate_dict[candidate] / total_votes)} ({candidate_dict[candidate]})")

    # Determine winner, and add to the Election Results in desired output.
    winner = max(candidate_dict, key=candidate_dict.get)
    election_results.extend([
        "-------------------------",
        f"Winner: {winner}",
        "-------------------------"
    ])

    # Print results to terminal.
    for line in election_results:
        print(line)

    # Print results to 'PyPoll_Analysis.txt'.
    txt_file_path = os.path.join('Analysis', 'PyPoll_Analysis.txt')
    with open(txt_file_path, mode='w') as txt_file:
        txt_file.write('\n'.join(election_results)) # Write each line to text file, separating each item by a new line.