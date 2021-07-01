import requests
import pandas as pd
import numpy as np

class MeanReversionStrategy():
    
    
    def __init__(self , stock):
        self._stock = stock
        # api_key = "08bfbdf1fe1e7e8908c2fcc0be1e81ff"
        self.api_key   = "08bfbdf1fe1e7e8908c2fcc0be1e81ff"
        
    
    def meanReversionStrategy(self):
        url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{self._stock}?apikey={self.api_key}'
        stockPrices = requests.get(url).json()
        stockPrices = stockPrices['historical'][0:1200]
        stockPrices = pd.DataFrame.from_dict(stockPrices)
        stockPrices = stockPrices.set_index('date')
        stockPrices['20d'] = stockPrices['close'].rolling(20).mean()
        stockPrices = stockPrices.iloc[::-1]
        
        
        stockPrices['returns'] = np.log(stockPrices['close'] / stockPrices['close'].shift(1))
        stockPrices['difference'] = stockPrices['close'] - stockPrices['20d']
        
        stockPrices['long'] = np.where((stockPrices['difference'] < -3) , 1 , np.nan)
        stockPrices['long'] = np.where((stockPrices['difference'] * stockPrices['difference'].shift(1)  < 0) , 0 , stockPrices['long'])
        stockPrices['long'] = stockPrices['long'].ffill().fillna(0)
        stockPrices['gain_loss'] = stockPrices['long'].shift(1) * stockPrices['returns']
        stockPrices = stockPrices.dropna(subset=['20d'])
        stockPrices['total_gain_loss'] = stockPrices['gain_loss'].cumsum()
        return stockPrices
    
    
    

stockMeanStrategy = MeanReversionStrategy('AAPL')
stockMeanDecision = MeanReversionStrategy.meanReversionStrategy(stockMeanStrategy)
        
        