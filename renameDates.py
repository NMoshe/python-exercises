#renameDates - Rename filenames with american date format

import shutil
import os
import re

#Create regex that matches American date format
datePattern = re.compile(r"""^(.*?)  #text before the date
    ((0|1)?\d)-                      #1 or 2 digits for the month
    ((0|1|2|3)?\d)-                  #1 or 2 digits for the day
    ((19|20)\d\d)                    #4 digits for the year
    (.*?)$                           #text after the date
    """, re.VERBOSE)

#Loop files in working directory
for americanFilename in os.listdir('.'):
    mo = datePattern.search(americanFilename)

    #skip files without date
    if mo == None:
        continue

    #Get different parts of filenames
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    #create european filenames
    europeanFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    #get the absolute paths
    absWorkingDir = os.path.abspath('.')
    americanFilename = os.path.join(absWorkingDir, americanFilename)
    europeanFilename = os.path.join(absWorkingDir, europeanFilename)

    #rename files
    print(f'Renaming "{americanFilename}" to "{europeanFilename}"...')
    #shutil.move(americanFilename, europeanFilename) #Uncomment to truly change filenames