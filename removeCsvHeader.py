# Remove header from csv files

import csv
import os

os.makedirs('headerRemoved', exist_ok=True)

# Loop through files in cwd
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue  # skip non csv files
    print('Removing header from ' + csvFilename + '...')

    # Read csv file skipping first row
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)

    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRows.append(row)
    csvFileObj.close()

    # Write out csv file
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
