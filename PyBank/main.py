import os, csv  # Import dependencies.

# Locate and open CSV.
csv_file_path = os.path.join('Resources', 'budget_data.csv')
with open(csv_file_path, mode='r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader) # Obtain header row.
    # Initialize column indexes from header.
    date_index = csvheader.index('Date')
    profit_index = csvheader.index('Profit/Losses')

    firstrow = next(csvreader)  # Obtain next row of data.

    # Initilize variables for financial analysis to be used in later loop when reading through CSV file.
    months_count = 1
    profit_total = int(firstrow[profit_index])
    last_profit = int(firstrow[profit_index])    # Used to calculate change from last month
    greatest_change_amount = 0
    lowest_change_amount = 0
    total_change = 0

    # Loop through each row in CSV, excluding header and first row.
    for row in csvreader:
        
        # Set row's "Date" and "Profit/Losses" values to variables.
        row_month_year = row[date_index]
        row_profit = int(row[profit_index])

        # Track "Total Months" by counting rows in the dataset.
        months_count += 1

        # Add row's "Profit/Losses" to "Total".
        profit_total += row_profit

        # Compute "Change" from last.
        change = row_profit - last_profit

        # Check if row meets criteria for "Greatest Increase in Profits" and "Greatest Decrease in Profits" against latest stored values in "greatest_amount" and "lowest_amount" variables.
        # If so, replace latest stored values in variables with row's "Date" and change values.
        if change > greatest_change_amount: 
            greatest_change_month = row_month_year
            greatest_change_amount = change
        elif change < lowest_change_amount:
            lowest_change_month = row_month_year
            lowest_change_amount = change

        # Compute total change to utilize in calculating "Average Change" after loop.
        total_change += change

        # Set "last_profit" to row's "Profit/Losses" before moving on to the next row.
        last_profit = row_profit 

    # Divide total change by "Total Months" to calculate "Average Change".
    average_change = total_change / (months_count - 1)

    # Print results to terminal and text file.
    results_list = [    # Store lines of results to print in list.
        "Financial Analysis",
        "-----------------------------",
        f"Total Months: {months_count}",
        f"Total: ${profit_total}",
        f"Average Change: {average_change}",
        f"Greatest Increase in Profits: {greatest_change_month} (${greatest_change_amount})",
        f"Greatest Decrease in Profits: {lowest_change_month} (${lowest_change_amount})"
    ]
    
    for line in results_list:   # Loop through each item in "results_list" to print to the terminal.
        print(line)

    txt_file_path = os.path.join('Analysis', 'PyBank_Analysis.txt')
    with open(txt_file_path, mode='w') as txt_file:
        txt_file.write('\n'.join(results_list)) # Write each item in "results_list" to text file, separating each item by a new line.