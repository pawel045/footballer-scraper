import os
from football import *

clear = lambda: os.system('cls')

print('''The program is used to search for the 10 most important transfers in the period selected by the user (1990-2022).
The footballers will be listed in Excel. The sheet will be automatically saved. In addition, two charts will be generated:
   - the first chart gives the sum values of the prices of football players in each season,
   - the second chart sums up the number of transfers in each country.
The program adopts the convention that the 2015/2016 season is given as 2015, etc.
\nIn a moment you will be asked to enter the necessary information.''')
input('To move on, press enter.')
clear()

good_start_year = False
good_end_year = False

while not good_start_year:

    start_year = input('Enter the beginning of the period you are interested in and press enter:')
    if not start_year.isdecimal():
        clear()
        print("It has to be a number. Please type again.")
    elif int(start_year) < 1990 or int(start_year) > 2022:
        clear()
        print("Please provide a year between 1990 and 2022.")
    elif int(start_year) == 2022:
        end_year = 2022
        clear()
        good_start_year = True
        good_end_year = True
    else:
        good_start_year = True

while not good_end_year:

    end_year = input('Enter the end of the period you are interested in and press enter:')
    if not end_year.isdecimal():
        clear()
        print("It has to be a number. Please type again.")
    elif int(end_year) < int(start_year) or int(end_year) > 2022:
        clear()
        print(f"(Please provide a year between 1991 and 2022, but larger than the initial year {start_year})")

    else:
        good_end_year = True

clear()
years = (int(start_year), int(end_year))
if years[0] == years[1]:
    print(f'Please wait, the search for the most important transfers of the season is underway {years[0]}')
else:
    print(f'Please wait, the search for the most important transfers of the seasons is underway {years[0]}-{years[1]}')

start_program(f'best_transf_{years[0]}_{years[1]}', years)

clear()
print(f'The file was saved under the path: {os.getcwd()}')
input('Press enter to exit.')

