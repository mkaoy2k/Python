import csv
from datetime import datetime
"""Demonstrate reading and writing CSV files
using reader() and writer() methods
Steps to read a CSV file:

    1. Import the csv library.
        import csv.
    2. Open the CSV file. 建議用語境管理就可省掉 step 6
    3. Use the csv.reader object to read the CSV file, e.g.
        csvreader = csv.reader(file)
    4. Extract the field names in the 1st line, called header. ...
    5. Extract the rows/records. ...
    6. Close the file.

"""

data = []

# Initialize the folder where data is located
data_path = 'sample'  # relative to the current dir

# Locate all data files in this example
file_read = f'{data_path}/csv_stocks.csv'
file_write = f'{data_path}/csv_stocks_daily_return.csv'

with open(file_read, 'r') as csv_file:

    # reader() method is commonly used for reading CSV files
    # But, DictReader() method is preferred to read csv contents
    # into a dictionary with the values of the first row as keys
    csv_reader = csv.reader(csv_file)

    # Skip the first line which is the header
    header = next(csv_reader)

    print(f'Reading {csv_file.name} ...\n')
    for line in csv_reader:

        # [Date, Open, High, Low, Close, Volume, Adj. Close]
        date = datetime.strptime(line[0], '%m/%d/%Y')
        open_price = float(line[1])  # 'open' is a built-in keyword
        high = float(line[2])
        low = float(line[3])
        close = float(line[4])
        volume = int(line[5])
        adj_close = float(line[6])

        data.append([date, open_price, high, low, close, volume,
                     adj_close])

# Assume stock data sorted in chronogically decending order
# Otherwise, need to sort it first

# Write to another CSV file
with open(file_write, 'w') as new_file:
    fieldnames = ['Date', 'return']

    csv_writer = csv.writer(new_file, delimiter='\t')

    # write the header at the first line
    csv_writer.writerow(fieldnames)

    for i in range(len(data) - 1):

        # Compute and store daily stock returns
        today_row = data[i]
        today_date = today_row[0]
        today_price = today_row[-1]
        yesterday_row = data[i + 1]
        yesterday_price = yesterday_row[-1]

        daily_return = (today_price - yesterday_price) / yesterday_price
        formatted_date = today_date.strftime('%m/%d/%Y')

        # writerow() method is to write one row of data to file
        csv_writer.writerow([formatted_date, daily_return])

print(f'==>Please check a new file, called {file_write}, created')
