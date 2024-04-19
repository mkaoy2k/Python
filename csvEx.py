import csv
"""Demonstrate reading and writing CSV files
using DictReader() and DictWriter() methods"""


# Initialize the folder where data is located
data_path = 'sample'  # relative to the current dir

# all data files in this example
file_read = f'{data_path}/csv_data.csv'
file_write = f'{data_path}/csv_data_new.csv'

with open(file_read, 'r') as csv_file:

    # reader() method is commonly used for reading CSV files
    # But, DictReader() method is preferred to read csv contents
    # into a dictionary with the values of the first row as keys
    csv_reader = csv.DictReader(csv_file)

    with open(file_write, 'w') as new_file:
        fieldnames = ['first_name', 'last_name']

        # writer() method is commonly used for writing CSV files
        # But, DictWriter() method is preferred to write csv
        csv_writer = csv.DictWriter(
            new_file, fieldnames=fieldnames, delimiter='\t')

        # write all the keys in the first row explicitly
        csv_writer.writeheader()

        for line in csv_reader:

            # filter email out so that first and last names are
            # written to the CSV file
            del line['email']

            # writerow() method is to write one row of data to file
            csv_writer.writerow(line)

print(f'==>Please check a new file, called {file_write} that has been created')
