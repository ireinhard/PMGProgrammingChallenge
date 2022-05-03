'''
csvCombiner: Script that creates database from input files on command line
Database Structure: email_hash, category, filename
Author: Isaac Reinhard
'''

# Import statements
import pandas as pd
import sys
import ntpath
import time

'''
Function that creates combined database from given csv files
@filesToRead: array of files to be read 
@chunkSize: size of chunks to read in data 
'''
def makeCombinedCSV(filesToRead, chunkSize):
    # Creating database
    csvDatabase = pd.DataFrame()

    # Iterate through all files in chunks, add new column, and then append to database
    for file in filesToRead:
        for chunk in pd.read_csv(file, chunksize=chunkSize):
            chunk['fileName'] = ntpath.basename(file)
            csvDatabase = pd.concat([csvDatabase, chunk], ignore_index=True)
    return csvDatabase

# Create array of input files
fileNamesToCombine = []
for inputValue in sys.argv:
    if inputValue.endswith('.csv'):
        fileNamesToCombine.append(inputValue)

# Creating database and printing to new csv
start = time.time() # used to test runtime speeds
finalCsv = makeCombinedCSV(fileNamesToCombine, 50000)
end = time.time()
print(finalCsv.to_csv())
