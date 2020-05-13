#!/usr/bin/env python
# Final Project

'''
Goal of project: create a module that allows users to update tab names of an Excel file they specify without having to
open the Excel file.
Use cases:
    1. Updating tab names for large files (which takes a while to open and save) without having to open the files.
    2. Update tabs names of multiple files efficiently by copying and pasting in Python
'''

'''
How to run the script:
1. Run code as it is.  When prompted, enter filepath as indicated.
2. When prompted, update tab names in relevant .txt file as indicated.
'''


# Step one: get user input of filepath and open the file that needs to be handled
import sys
import pandas as pd
import os

while True:
    file_to_be_handled = input("Please input filepath of the Excel file that needs to be updated: ")
    # Example filepath: C:\Users\shiwe\PycharmProjects\untitled1\venv\Scripts\Cities.xlsx
    try:
        xls = pd.ExcelFile(file_to_be_handled)
    except FileNotFoundError:
        print("I cannot find this file.  Please try another one.")
    except TypeError:
        print("Looks like the file name is missing.  Please input one.")
    except Exception:
        print("Unhandled exception.")
    finally:
        break
'''Grading criteria: Read in and Process a file'''
'''Grading criteria: Have one try/except statement'''

# Step two: count the number of tabs and create a dictionary of current tab names
num_of_tabs = len(xls.sheet_names)
tabs = xls.sheet_names

tab_dict = {}
for i,tab in enumerate(tabs):
    tab_dict["Tab "+str(i+1)] = tab

print("You have {} tabs.".format(num_of_tabs))
print(tab_dict)

'''Grading criteria: Use at least one dictionary'''

# Step three: write to output file and ask user to update tab names
with open("tab_dict.txt", "w") as outfile:
    for i, tab in tab_dict.items():
        outfile.writelines("{}:{}".format(i, tab))
        outfile.write("\n")

'''Grading criteria: Output something (write) to a file, using string formatting'''

# Ask user to update tab names in relevant txt file

print("Please update tab names as needed in {}\\tab_dict.txt".format(os.getcwd()))
input("Once finished, enter anything to continue: ")

# Step four: update Excel tab names with user input in text file
tab_dict_updated = {}
with open("tab_dict.txt") as f:
    for line in f:
        (i, tab) = line.strip().split(":")
        tab_dict_updated[i.strip()] = tab.strip()

print("Your updated tab names are:")
print(tab_dict_updated)

import openpyxl
updated_xls = openpyxl.load_workbook(file_to_be_handled)
i = 0
for tab in tab_dict_updated.values():
    sheet = updated_xls[tabs[i]]
    sheet.title = tab
    if i < num_of_tabs:
        i = i + 1
    else:
        break
updated_xls.save(file_to_be_handled)

'''Grading criteria: Contain at least one if/else statement.'''
'''Grading criteria: Use a list comprehension'''





