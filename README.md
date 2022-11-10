# Transaction_Profile_Code

The Transactional_Profile is a script written in Python using Pandas to work with DataFrames, takes a file written as a CSV file, and applies different descriptive calculations such as Transaction Average, Transaction per Country, Transaction per Month and Transaction per Description.  

Skills Applied:

From OOP:
- Transactional Profile as a Class.
- Class Attributes for Data's and Output's Address
- Use of non-public methods due to user´s request for self-operation.
- Self-creation of output folder in CSV format.

Data Analysis applied with Pandas
- Data importing (CSV reading).
- Data Manipulation: Modifying tables to apply calculations.
- Formating date, and extraction of month element from date.
- Aggregate functions for mean and count.

All the outputs of the different calculations are placed as CSV files in an Output folder that is created by the same Transaction_Profile code.  The name of the folder created is a combination of the date when the script was run and the name of the raw data csv that was given to it

# Quick Settings

Before running the code:

1. Check that you have installed the Pandas package in your computer.
2. Change the CSV_ADDRESS and the OUTPUT_ADDRESS to the ones you are going to use in your local computer.
