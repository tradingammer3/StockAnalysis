# =============================================================================
# Measuring the performance of a buy and hold strategy - sharpe & sortino
# Author : Mayank Rasu (http://rasuquant.com/wp/)

# Please report bug/issues in the Q&A section
# =============================================================================

# Import necesary libraries
import yfinance as yf
import numpy as np
import datetime as dt
import pandas as pd

# Download historical data for required stocks

# SnP = yf.download(ticker,dt.date.today()-dt.timedelta(1825),dt.datetime.today())

class performanceKPI():
    
    def __init__(self , ticker):
        self._ticker = ticker
               
    
    def getData(self):
        perfDF = ()
        SnP = yf.download(self._ticker,dt.date.today()-dt.timedelta(1825),dt.datetime.today())
        company = self._ticker
        CAGR = self.CAGR(SnP)
        volatility = self.volatility(SnP)    
        sharpRatio = self.sharpe(SnP, 5, CAGR, volatility)
        sortinoRatio = self.sortino(SnP, 5, CAGR)
        perfDF = (company , CAGR , volatility , sharpRatio , sortinoRatio)
 
        # perfDF['sortinoRatio'] = self.sortino(SnP , 5 , perfDF['CAGR'] )
        
        return perfDF
    
    def CAGR(self , DF):
        "function to calculate the Cumulative Annual Growth Rate of a trading strategy"
        df = DF.copy()
        df["daily_ret"] = DF["Adj Close"].pct_change()
        df["cum_return"] = (1 + df["daily_ret"]).cumprod()
        n = len(df)/252
        CAGR = (df["cum_return"][-1])**(1/n) - 1
        return CAGR

    def volatility(self , DF):
        "function to calculate annualized volatility of a trading strategy"
        df = DF.copy()
        df["daily_ret"] = DF["Adj Close"].pct_change()
        vol = df["daily_ret"].std() * np.sqrt(252)
        return vol

    def sharpe(self , DF,rf , CAGR , volatility):
        "function to calculate sharpe ratio ; rf is the risk free rate"
        # df = DF.copy()
        sr = (CAGR - rf)/volatility
        return sr
 
    def sortino(self , DF,rf , CAGR):
        "function to calculate sortino ratio ; rf is the risk free rate"
        df = DF.copy()
        df["daily_ret"] = DF["Adj Close"].pct_change()
        df["neg_ret"] = np.where(df["daily_ret"]<0,df["daily_ret"],0)
        neg_vol = df["neg_ret"].std() * np.sqrt(252)
        sr = (CAGR - rf)/neg_vol
        return sr
    
    


# # ticker = "^GSPC"
ticker = "AAPL"
KPI = performanceKPI(ticker)
perfKPI = performanceKPI.getData(KPI)
perfKPIList = np.reshape(list((perfKPI)) , (1,5))
perfKPIDF = pd.DataFrame(perfKPIList , columns=['Company' , 'CAGR' , 'Volatility' , 'SharpeRatio' , 'SortinoRatio'])
