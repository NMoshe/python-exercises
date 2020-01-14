# Tabulate pop. and census tracts for each country

import openpyxl
import pprint
print('Opening Workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

print('Reading Rows..')
for row in range(2, sheet.max_row + 1):
    # each row has data for 1 census tract
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # Make sure state key exists
    countyData.setdefault(state, {})
    # Make sure county in state exists
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    # Each row represents one census tract
    countyData[state][county]['tracts'] += 1
    # increase county pop by pop in census
    countyData[state][county]['pop'] += int(pop)

# Open text file and write countyData content to it.
print('Writing Results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')