import os, csv  # Import dependencies.

# Direct to and open 'budget_data.csv'.
csv_file_path = os.path.join('Resources', 'budget_data.csv')
with open(csv_file_path, mode='r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')

    # Obtain header row and indexes of columns.
    csvheader = next(csvreader) 
    date_index = csvheader.index('Date')
    profit_index = csvheader.index('Profit/Losses')

    # Obtain first row and initilize variables for Financial Analysis.
    firstrow = next(csvreader)
    months_count = 1
    profit_total = int(firstrow[profit_index])
    last_profit = int(firstrow[profit_index])    # Used to calculate change
    greatest_change_amount = 0
    lowest_change_amount = 0
    total_change = 0

    # Loop through each row in 'budget_data.csv', excluding header and first row.
    for row in csvreader:
        
        # Store row's "Date" and "Profit/Losses".
        row_month_year = row[date_index]
        row_profit = int(row[profit_index])

        # Track Total Months by counting rows in the dataset.
        months_count += 1

        # Add row's "Profit/Losses" to Total.
        profit_total += row_profit

        # Compute change from last month's "Profit/Losses".
        change = row_profit - last_profit

        # Check if row meets criteria for Greatest Increase in Profits and Greatest Decrease in Profits against latest stored values in "greatest_amount" and "lowest_amount" variables.
        # If so, replace latest stored values in variables with row's "Date" and change values.
        if change > greatest_change_amount: 
            greatest_change_month = row_month_year
            greatest_change_amount = change
        elif change < lowest_change_amount:
            lowest_change_month = row_month_year
            lowest_change_amount = change

        # Compute total change.
        total_change += change

        # Set "last_profit" to row's "Profit/Losses" before moving on to the next row.
        last_profit = row_profit 

    # Divide total change by "Total Months" (minus 1, since there's one less change than the total number of months) to calculate "Average Change".
    average_change = total_change / (months_count - 1)

    # Store Financial Analysis results in list.
    financial_analysis_results = [    
        "Financial Analysis",
        "-----------------------------",
        f"Total Months: {months_count}",
        f"Total: ${profit_total}",
        f"Average Change: {average_change}",
        f"Greatest Increase in Profits: {greatest_change_month} (${greatest_change_amount})",
        f"Greatest Decrease in Profits: {lowest_change_month} (${lowest_change_amount})"
    ]

    # Print results to terminal.
    for line in financial_analysis_results:
        print(line)

    # Print results to 'PyBank_Analysis.txt'.
    txt_file_path = os.path.join('Analysis', 'PyBank_Analysis.txt')
    with open(txt_file_path, mode='w') as txt_file:
        txt_file.write('\n'.join(financial_analysis_results)) # Write each line to text file, separating each item by a new line.