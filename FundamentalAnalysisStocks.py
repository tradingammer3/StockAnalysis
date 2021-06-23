# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import FundamentalAnalysis as fa
import StockPeers as peers
import datetime
import requests


ticker = "AMZN"
# api_key = "802b63ba7f7d06305d7ca936e6f3b2ca"
api_key = "08bfbdf1fe1e7e8908c2fcc0be1e81ff"

year = datetime.datetime.today().year
yearOfAnalysis = (list(range(year , year - 5 , -1)))

# Show the available companies
companies = fa.available_companies(api_key)

# Fetch stock Competitors
stockCompetitors = peers.StockPeers(ticker)
stockCompetitorsList = peers.StockPeers.stockPeersList(stockCompetitors)


# Collect general company information
profile = fa.profile(ticker, api_key)

# collect general information about the competitors
stockPeerDetails = pd.DataFrame()
stockPeerDetailsAll = pd.DataFrame()
for stock in stockCompetitorsList:
    stockPeerDetails = fa.profile(stock , api_key)
    stockPeerDetailsAll = pd.concat([stockPeerDetailsAll , stockPeerDetails] , axis = 1)
    
    

# Collect recent company quotes
quotes = fa.quote(ticker, api_key)

# Collect recent quotes for all Peer Company
stockPeerQuote = pd.DataFrame()
stockPeerQuoteAll = pd.DataFrame()
for stock in stockCompetitorsList:
    stockPeerQuote = fa.quote(stock , api_key)
    stockPeerQuoteAll = pd.concat([stockPeerQuoteAll , stockPeerQuote] , axis = 1)
    

# Collect market cap and enterprise value
entreprise_value = fa.enterprise(ticker, api_key)

# Collect recent market cap and enterprise values for all Peer Company
stockPeerEP = pd.DataFrame()
stockPeerEPAll = pd.DataFrame()
for stock in stockCompetitorsList:
    stockPeerEP = pd.DataFrame(fa.enterprise(stock , api_key))
    stockPeerEP = stockPeerEP.iloc[: , 0:6]
    stockPeerEPAll = pd.concat([stockPeerEPAll , stockPeerEP], axis = 1)
    



# Show recommendations of Analysts
# Not good to have for all stockPeers . Should CHange ticker and do the Analysis Accordingly
ratings = fa.rating(ticker, api_key)

# Obtain DCFs over time
dcf_annually = fa.discounted_cash_flow(ticker, api_key, period="annual")
dcf_quarterly = fa.discounted_cash_flow(ticker, api_key, period="quarter")

# Obtain DCFs for all Peers annually
dcfPeerA = pd.DataFrame()
dcfPeerAAll = pd.DataFrame()
for stock in stockCompetitorsList:
    dcfPeerA = fa.discounted_cash_flow(stock, api_key, period="annual")
    dcfPeerA = dcfPeerA.iloc[: , 0:6]
    dcfPeerA['symbol'] = stock
    dcfPeerAAll = pd.concat([dcfPeerAAll , dcfPeerA], axis = 1)
    

# Obtain DCFs for all Peers Quarterly 


# Collect the Balance Sheet statements
balance_sheet_annually = fa.balance_sheet_statement(ticker, api_key, period="annual")
balance_sheet_quarterly = fa.balance_sheet_statement(ticker, api_key, period="quarter")


# Collect the Income Statements
income_statement_annually = fa.income_statement(ticker, api_key, period="annual")
income_statement_quarterly = fa.income_statement(ticker, api_key, period="quarter")

# Collect the Cash Flow Statements
cash_flow_statement_annually = fa.cash_flow_statement(ticker, api_key, period="annual")
cash_flow_statement_quarterly = fa.cash_flow_statement(ticker, api_key, period="quarter")


# To call balance sheet , Income Statement , cash flow statement quarterly
# for all peers in one go call class FinancialQuarterly


# Show Key Metrics
key_metrics_annually = fa.key_metrics(ticker, api_key, period="annual")
key_metrics_quarterly = fa.key_metrics(ticker, api_key, period="quarter")

key_metrics_annually.to_csv('key metrics.csv')

# Show a large set of in-depth ratios
financial_ratios_annually = fa.financial_ratios(ticker, api_key, period="annual")
financial_ratios_quarterly = fa.financial_ratios(ticker, api_key, period="quarter")

# Show the growth of the company
growth_annually = fa.financial_statement_growth(ticker, api_key, period="annual")
growth_quarterly = fa.financial_statement_growth(ticker, api_key, period="quarter")

# Download general stock data
stock_data = fa.stock_data(ticker, period="ytd", interval="1d")

# Download detailed stock data
stock_data_detailed = fa.stock_data_detailed(ticker, api_key, begin="2000-01-01", end="2020-01-01")

