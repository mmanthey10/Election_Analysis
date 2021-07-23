import csv
import os

# assign variable to load a file from path

path = "/Users/michaelmanthey/Documents/Bootcamp/Module_3_Python/Election_Analysis/election_results.csv"

file_to_load = os.path.join(path)
file_to_save = os.path.join(path)

# initialize total vote counter
total_votes = 0

#create list for candidate options
candidate_options = []

#dictionary with candidate options and total votes for each
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:   
    file_reader = csv.reader(election_data)

    #read header row
    headers = next(file_reader)
    
    #print each row in csv file
    for row in file_reader:
        #add to the total vote count
        total_votes += 1

        #print the candidate name for each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:
          
            #add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            #track candidate vote counts
            candidate_votes[candidate_name] = 0

        #add a vote to that candidates count
        candidate_votes[candidate_name] += 1



    for candidate_name in candidate_options:
        votes = candidate_votes[candidate_name]
        
        #calculate vote_percentage
        vote_percentage = float(votes) / float(total_votes) * 100
        rounded_percent = round(vote_percentage, 2)

        #print candidate name and percentage of votes
        #print(f"{candidate_name} received {rounded_percent} % of the total votes.")

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")    
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)  