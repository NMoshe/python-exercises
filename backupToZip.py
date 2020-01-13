# Copies contents of folder into ZIP file whose filename increments

import zipfile
import os

def backupToZip(folder):
    #make sure folder is absolute
    folder = os.path.abspath(folder)

    #figure out filename based on files that already exists
    num = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(num) + '.zip'
        if not os.path.exists(zipFilename):
            break
        num += 1

    #create zip file
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.Zipfile(zipFilename, 'w')

    #walk folder tree and compress files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        #add current folder to zip file
        backupZip.write(foldername)

        #add all files in folder to zip file
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue #dont backup backup zip files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')
#backupToZip('C:\\delicious')