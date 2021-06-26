import pandas as pd
import requests
import FundamentalAnalysis as fa


api_key = '802b63ba7f7d06305d7ca936e6f3b2ca'
screener = requests.get(f'https://financialmodelingprep.com/api/v3/stock-screener?marketCapMoreThan=1000000000&sector=Technology&exchange=NASDAQ&limit=10&apikey=802b63ba7f7d06305d7ca936e6f3b2ca').json()


ticker = []
for item in screener:
    ticker.append(item['symbol'])


# BSScreener = pd.DataFrame()
# BSScreenerAll = pd.DataFrame()

# for stock in ticker:
#    BSScreener = fa.balance_sheet_statement(stock, api_key, period="annual")
#    BSScreener = BSScreener.iloc[: , 0:1]
#    BSScreener['symbol'] = stock
#    BSScreenerAll = pd.concat([BSScreenerAll , BSScreener], axis = 1)
   
   
# BSScreenerAll = BSScreenerAll.T


BSScreener = {}

for stock in ticker:
    BS = requests.get(f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{stock}?limit=1&apikey=802b63ba7f7d06305d7ca936e6f3b2ca').json()
    BSScreener[stock] = BS[0]
    

BSIndustry = pd.DataFrame.from_dict(BSScreener)