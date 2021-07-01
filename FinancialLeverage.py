# Degree of Financial Leverage
# DFL (Degree of Financial Leverage) = Operating Profit / Earnings Before Taxes

# Degree of operating Leverage
# Contribution Margin = Sales – Variable Costs
# DOL = Contribution Margin / Operating Profit




import requests
import pandas as pd
import numpy as np

class FinancialLeverage():
    
    
    def __init__(self , stock):
        self._stock = stock
        # api_key = "08bfbdf1fe1e7e8908c2fcc0be1e81ff"
        self.api_key   = "08bfbdf1fe1e7e8908c2fcc0be1e81ff"
        
        
    def financialLeverage(self):
        url = f'https://financialmodelingprep.com/api/v3/income-statement/{self._stock}?limit=5&apikey={self.api_key}'
        stockIS = requests.get(url).json()
        
        operating_Profit = stockIS[0]['operatingIncome'] 
        EBT = stockIS[0]['incomeBeforeTax']
        financialLeverage = operating_Profit/ EBT
        
        return financialLeverage
    


FinancialLeverage = FinancialLeverage('AMZN')
companyFinancialLeverage = FinancialLeverage.financialLeverage()

print(companyFinancialLeverage)
