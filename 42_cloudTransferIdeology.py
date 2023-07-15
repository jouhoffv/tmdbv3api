import csv
import glob

# Input file to check for matches
input_file = input("Enter the input file name: ")

# List of Python files starting with "01" or "00"
python_files = glob.glob("01*.py") + glob.glob("00*.py")

# Check for matches and add columns accordingly
with open('extng.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)

# Get the header row and append new column names
header = rows[0]
header.append("Column_01")
header.append("Column_00")

# Iterate over the rows and check for matches
for row in rows[1:]:
    filename = row[0]
    if filename in python_files:
        row.append("X")  # Add "X" to indicate a match
        row.append("")   # Empty cell for "00" column
    else:
        row.append("")   # Empty cell for "01" column
        row.append("")   # Empty cell for "00" column

# Write the updated rows to the output file
with open('extng.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print("Columns added to extng.csv successfully.")
