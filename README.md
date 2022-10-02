# python-challenge
Repository of Python scripts, data, and resulting analysis from Python scripts for the PyBank and Pypoll challenges.

## PyBank
In this challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses". (Thankfully, your company has rather lax standards for accounting, so the records are simple.)

Your task is to create a Python script that analyzes the records to calculate each of the following:

- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and then the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in profits (date and amount) over the entire period

Your analysis should look similar to the following:

    Financial Analysis
    ----------------------------
    Total Months: 86
    Total: $22564198
    Average Change: $-8311.11 
    Greatest Increase in Profits: Aug-16 ($1862002)
    Greatest Decrease in Profits: Feb-14 ($-1825558)

In addition, your final script should both print the analysis to the terminal and export a text file with the results.