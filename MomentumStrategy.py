import requests
import pandas as pd
import numpy as np

class MomentumStrategy():
    
    
    def __init__(self , stock):
        self._stock = stock
        # api_key = "08bfbdf1fe1e7e8908c2fcc0be1e81ff"
        self.api_key   = "08bfbdf1fe1e7e8908c2fcc0be1e81ff"
        
    
    def momentumStrategy(self):
        url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{self._stock}?apikey={self.api_key}'
        stockPrices = requests.get(url).json()
        stockPrices = stockPrices['historical'][0:1200]
        stockPrices = pd.DataFrame.from_dict(stockPrices)
        stockPrices = stockPrices.set_index('date')
        stockPrices = stockPrices.iloc[::-1]
        
        stockPrices['returns'] = np.log(stockPrices['close'] / stockPrices['close'].shift(1))
        stockPrices['movement'] = stockPrices['close'] - stockPrices['close'].shift(1)
        
        stockPrices['up'] = np.where( (stockPrices['movement'] > 0) , stockPrices['movement'] , 0)
        stockPrices['down'] = np.where((stockPrices['movement'] < 0) , stockPrices['movement'] , 0)
        
        up = stockPrices['up'].rolling(14).mean()
        down = stockPrices['down'].abs().rolling(14).mean()
        
        RS = up / down
        RSI = 100 - (100 / (1 + RS))
        RSI = RSI.rename('RSI')

        
        stockPricesNew = pd.merge(stockPrices , RSI , left_index = True , right_index=True)
        stockPricesNew['long'] = np.where((stockPricesNew['RSI'] < 30) , 1 , np.nan )
        stockPricesNew['long'] = np.where((stockPricesNew['RSI'] > 70) , 0 , stockPricesNew['long'] )
        stockPricesNew['long'].ffill(inplace = True)
        stockPricesNew['gain_loss'] = stockPricesNew['long'].shift(1) * stockPricesNew['returns']
        stockPricesNew['total_gain_loss'] = stockPricesNew['gain_loss'].cumsum()
        return stockPricesNew
    
    
    

stockMomentum = MomentumStrategy('AAPL')
stockMomentumDecision = MomentumStrategy.momentumStrategy(stockMomentum)
        
        