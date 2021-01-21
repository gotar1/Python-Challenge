# import dependencies
import os
import csv
from datetime import datetime

# P.C csv filepath:
# pyboss_csv = os.path.join('.', 'Resources', 'employee_data.csv')

# V.S code csv filepath:
# pyboss_csv = os.path.join('.', 'PyBoss', 'Resources', 'employee_data.csv')

# output csv filepath:
output_path = os.path.join('.', 'PyBoss', 'output', 'new_employee_data.csv')

# state abbreviation dictionary.
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

# function to use for changing states full names to abbreviation
abbrev_us_state = dict(map(reversed, us_state_abbrev.items()))

# create a new dictionary to hold our new values
new_csv_dict = {"Emp ID": [],"First Name": [], "Last Name": [], "DOB": [], "SSN": [], "State": []}

# open csv file and read header
with open(pyboss_csv) as csvfile:
    boss_reader = csv.reader(csvfile, delimiter = ",") 
    csv_header = next(boss_reader)

    # loop through the csv reader do data analysis and append new dictionary with new values
    for row in boss_reader:

        # append employees id to new dictionary
        new_csv_dict["Emp ID"].append(row[0])

        # split employees names to first name and last name and save seperately in new dictionary
        first = row[1].split()[0]
        last = row[1].split()[1]
        new_csv_dict["First Name"].append(first)
        new_csv_dict["Last Name"].append(last)

        # change date format from Y-m-d to m/d/Y and append in new dictionary
        date = row[2]
        date = datetime.strptime(date, '%Y-%m-%d')
        date = datetime.strftime(date, '%m/%d/%Y')
        new_csv_dict["DOB"].append(date)

        # hide first 5 numbers of SSN leaving only last 4 digits visible and save to new dictionary 
        SSN = "xxx-xx-" + row[3][-4:]
        new_csv_dict["SSN"].append(SSN)

        # abbreviate all states and save to new dictionary
        statecode = us_state_abbrev[row[4]]
        new_csv_dict["State"].append(statecode)

# write and save a new csv file with new dictionary values
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter = ',')
    csvwriter.writerow(new_csv_dict.keys())
    csvwriter.writerows(zip(*new_csv_dict.values()))