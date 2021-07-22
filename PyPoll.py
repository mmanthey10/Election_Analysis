import csv
import os

# assign variable to load a file from path

path = "/Users/michaelmanthey/Documents/Bootcamp/Module_3_Python/Election_Analysis/election_results.csv"

file_to_load = os.path.join(path)
file_to_save = os.path.join(path)

with open(file_to_load) as election_data:   
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
  #  for row in file_reader:
   #     print(row)