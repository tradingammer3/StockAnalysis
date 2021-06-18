# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 17:20:10 2021

@author: Aamerali.Sayyed
"""

# =============================================================================
# Data extraction from stockrow.com
# Author : Reza Sadegehi (Reviewed by Mayank Rasu)

# Please report bug/issues in the Q&A section
# =============================================================================
import pandas as pd 
from enum import Enum
import StockPeers as peers
import os
import glob



stock = 'AAPL'
stockCompetitors = peers.StockPeers(stock)
stockCompetitorsList = peers.StockPeers.stockPeersList(stockCompetitors)

tickers=["BA"] #list of tickers whose data needs to be extracted
path = "F:\\Stockrow\\Income Statements" # please create this folder in your local machine
#Please also create subfolders Annual, Quartely and Trailing in your local machine

class Financials(Enum):
    
    Income_Statement = 1
    Balanced_Sheet = 2
    CashFlow = 3
    Key_Metrics=4
    Growth=5

class Terms(Enum):
    Quarterly=1
    Annual=2
    Trailing=3


def FinFun(ticker,Fin,Term):
    """Please create subfolders Annual, Quartely and Trailing in your local machine"""
    if Fin==Financials.Balanced_Sheet:
        if Term==Terms.Annual:
            URL="https://stockrow.com/api/companies/"+ticker+"/financials.xlsx?dimension=A&section=Income%20Statement&sort=desc"
            
            filename= path+"\\Annual\\Income-Statement-Ann-{}.csv".format(ticker)
            return URL, filename
        
        elif Term==Terms.Quarterly:
            URL="https://stockrow.com/api/companies/"+ticker+"/financials.xlsx?dimension=Q&section=Income%20Statement&sort=desc"
                     
            filename= path+"\\Quarterly\\Income-Statement-Qtr-{}.csv".format(ticker)
            return URL, filename   
        

        elif Term==Terms.Trailing:
            URL="https://stockrow.com/api/companies/"+ticker+"/financials.xlsx?dimension=T&section=Income%20Statement&sort=desc"
         
            filename= path+"\\Trailing\\Income-Statement-ttm-{}.csv".format(ticker)
            return URL, filename   
        
        
        
def Download_data(ticker,Fin,Term):        
        

    URL,filename= FinFun(ticker ,Fin,Term)
    print(" Download "+ str(Fin) +" for stock: " + ticker + " terms : " +str(Term) )

    df= pd.read_excel(URL)
    
    
    
    df.to_csv(filename,index=False)
    pd.read_csv(filename, header=None).T.to_csv(filename, header=False, index=False)
    
    
    df=pd.read_csv(filename,index_col=False   )
    
     # change the name of the columns 
    columns=df.columns.values.tolist()
    columns[0]="date"
    columns[1]="stock"
    df.columns=columns
    
    #shorten the date and change the index to date
    df['date'] =pd.to_datetime(df["date"])
    df['date']  = df['date'].dt.date
    df['stock'] = ticker
    
    # save the file
    df.to_csv(filename,index=False)



# for ticker in tickers:
for ticker in stockCompetitorsList:
    Download_data(ticker ,Financials.Balanced_Sheet,Terms.Annual)
    Download_data(ticker ,Financials.Balanced_Sheet,Terms.Quarterly)
    Download_data(ticker ,Financials.Balanced_Sheet,Terms.Trailing)



os.chdir("F:\Stockrow\Income Statements\Annual")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])


