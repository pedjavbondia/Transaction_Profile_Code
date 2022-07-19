# Importing Libraries
import pandas as pd
from datetime import date
import os

# Creating the Class Transactional Profile


class TransactProfile:

    # Declaring the address of the CSV file as Class Level Data
    CSV_ADDRESS = 'C:/Users/p_bon/Proyectos/SIA_PARTNERS/Data/'

    # Declaring the address of the output folver as a Class Level Data
    OUTPUT_ADDRESS = 'C:/Users/p_bon/Proyectos/SIA_PARTNERS/Output/'

    def __init__(self, name, address=CSV_ADDRESS):

        # Name of the Raw Data File
        self.name = name

        # Initizaling the location of csv file
        self.raw_data_adress = address + self.name

        # Creating Raw Data Object as a Pandas Data Frame
        Raw_Data = pd.read_csv(self.raw_data_adress.strip(), sep=';')

        # Creating the Output Folder
        self._output_folder()

        # Defining the Main Table that is going to be used for Calculations
        self.df_OfficialData = Raw_Data[['AccountNumber', 'TransAmountBase',
                                         'TransCountry', 'TransactionID', 'TransactionDate',
                                         'TransDesc']]

        # Calling the Transaction Average Calculator
        self._transaction_average()

        # Calling the Transaction per Country Calculator
        self._transaction_country()

        # Calling the Transaction per Month Calculator
        self._transaction_month()

        # Calling the Transaction per Description Calculator
        self._transaction_description()

    # Create an Output folder with the Date as the name:
    def _output_folder(self, output_address=OUTPUT_ADDRESS):
        # Getting the current date
        self.current_date = date.today()

        # Change the date to a string
        current_date_string = self.current_date.strftime('%d-%b-%Y')

        # Location of Output Folder
        self.output_address = output_address + current_date_string + '_' + self.name

        # Create the Output folder
        return os.mkdir(self.output_address)

    # Transaction Average Method
    def _transaction_average(self):

        # Table of Account Number vs Transaction Amount
        self.df_AccountNumber_TransAmountBase = self.df_OfficialData[[
            'AccountNumber', 'TransAmountBase']]

        # Storage Location
        self.transaction_average_location = self.output_address + \
            '/' + 'transaction_average.csv'

        # Transaction Average Calculation
        transaction_average = self.df_AccountNumber_TransAmountBase.groupby(
            'AccountNumber').agg(Transaction_Average=("TransAmountBase", 'mean'))

        # Creating a csv file as the output
        transaction_average.to_csv(self.transaction_average_location)
        return

    # Transaction per Country
    def _transaction_country(self):
        # Table of Account Number vs Transaction per Country
        self.df_AccountNumber_TransCountry = self.df_OfficialData[[
            'AccountNumber', 'TransCountry']]

        # Storage Location
        self.transaction_country_location = self.output_address + \
            '/' + 'transaction_country.csv'

        # Transaction per Country Calculation
        transaction_country = self.df_AccountNumber_TransCountry['TransCountry'].value_counts(
        ).sort_index().to_frame()

        # Creating a csv file as the ouput
        transaction_country.to_csv(self.transaction_country_location)
        return

    # Transaction per Month
    def _transaction_month(self):
        # Generating Month Column in Official Data Table
        self.df_OfficialData['Month'] = pd.to_datetime(
            self.df_OfficialData['TransactionDate'], format='%m/%d/%Y').dt.month_name()

        # Table of Account Number vs Month
        self.df_AccountNumber_Transactions_perMonth = self.df_OfficialData[[
            'AccountNumber', 'Month']]

        # Storage Location
        self.transaction_month_location = self.output_address + \
            '/' + 'transaction_month.csv'

        # Transactions per Month Calculation
        transaction_month = self.df_AccountNumber_Transactions_perMonth.groupby(
            ['AccountNumber', 'Month']).value_counts().to_frame('Count')

        # Creating the csv file as the ouput
        transaction_month.to_csv(self.transaction_month_location)
        return

    # Transaction per Description
    def _transaction_description(self):
        # Table of Transactions per Description
        self.df_AccountNumber_Transactions_perDescription = self.df_OfficialData[[
            'AccountNumber', 'TransDesc']]

        # Storage Location
        self.transaction_description_location = self.output_address + \
            '/' + 'transaction_description.csv'

        # Transactions per Description Calculation
        transaction_description = self.df_AccountNumber_Transactions_perDescription.groupby(
            ['AccountNumber', 'TransDesc']).value_counts().to_frame('Count')

        # Creating the csv file as the output
        transaction_description.to_csv(self.transaction_description_location)
        return


# Getting the CSV file name
csv_file_name = input('Escriba el nombre del archivo CSV: ')

# Instantiation of the Transaction Profile Object
trans_prof = TransactProfile(csv_file_name.strip())
