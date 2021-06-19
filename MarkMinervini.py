# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 16:58:04 2021

@author: Aamerali.Sayyed
"""
import pandas as pd
import requests
import time


class markMinerviniApproach():

  def __init__(self , stock):
      self._stock = stock
      # api_key = "08bfbdf1fe1e7e8908c2fcc0be1e81ff"
      self.api_key   = "08bfbdf1fe1e7e8908c2fcc0be1e81ff"
  
  def markMinerviniFormula(self , stockList):
  
      price = {}
      metrics = {}
      count = 0
  
      for company in stockList:
        count = count + 1
        time.sleep(3)
        print('count ' ,count)
	      
        try:
            prices_retrieval = requests.get(f'https://financialmodelingprep.com/api/v3/historical-price-full/{company}?timeseries=500&apikey={self.api_key}').json()
            prices_retrieval = prices_retrieval['historical']
		  
            price[company] = {}
            metrics[company] = {}
            
            for item in prices_retrieval:
                price_date = item['date']
                price[company][price_date] = item['adjClose']
                
                price_DF = pd.DataFrame.from_dict(price)
                price_DF['200_MA'] = price_DF[company].rolling(window=200).mean()
                price_DF['150_MA'] = price_DF[company].rolling(window=150).mean()
                price_DF['50_MA'] = price_DF[company].rolling(window=50).mean()
                price_DF['RS'] = (price_DF[company][-1]/price_DF['^GSPC'][-1] )/ (price_DF[company][-252]/price_DF['^GSPC'][-252]) *100
        	
                metrics[company]['200 MA'] = price_DF['200_MA'][-1]
                metrics[company]['150 MA'] = price_DF['150_MA'][-1]
                metrics[company]['50 MA'] = price_DF['50_MA'][-1]
                metrics[company]['200 MA_1mago'] = price_DF['200_MA'][-30]
                metrics[company]['150 MA_1mago'] = price_DF['150_MA'][-30]
                metrics[company]['200 MA_2mago'] = price_DF['200_MA'][-60]
                metrics[company]['150 MA_2mago'] = price_DF['150_MA'][-60]
                metrics[company]['52W_Low'] = price_DF[company][-252:].min()
                metrics[company]['52W_High'] = price_DF[company][-252:].max()
                metrics[company]['price'] = price_DF[company][-1]
                metrics[company]['Relative Strength'] = price_DF['RS'][-1]
                #Current Price is at least 30% above 52 week low (1.3*low_of_52week)
                metrics[company]['Above_30%_low'] = metrics[company]['52W_Low'] *1.3
                # Condition 7: Current Price is within 25% of 52 week high   (.75*high_of_52week)
                metrics[company]['Within_25%_high'] = metrics[company]['52W_High'] * 0.75
                
                metrics_DF = pd.DataFrame.from_dict(metrics)
                metrics_DF = metrics_DF.T 
                #to determine the rank percentil and see which are the 80% top performers
                metrics_DF['pct_rank'] = metrics_DF['Relative Strength'].rank(pct=True)
                metrics_DF = metrics_DF.T
                metrics_DF.to_csv('all_stocks_SP500.csv')
                
        except:
              pass
            		


