import pandas as pd
from bs4 import BeautifulSoup
import StockPeers as peers



class InstitutionalInvestor():

        def __init__(self ):
            pass
        
        
        def getInstitutionalInvestor(self , stockList):
            
           
            # identify = 0
            count_down = 0
            count_up = 0
            total_shares_exchanged = 0
            insider = pd.DataFrame()
 
            
            # for company in ['AAPL', 'AMZN']:
            insider1 = pd.read_html(f'http://openinsider.com/screener?s={stockList}&o=&pl=&ph=&ll=&lh=&fd=730&fdr=&td=0&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&xs=1&vl=&vh=&ocl=&och=&sic1=-1&sicl=100&sich=9999&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=500&page=1')
            insider1 = insider1[-3]
            insider1['company'] = stockList
            insider = pd.concat([insider,insider1])
  
               
            
                
            insider.columns.values[1] = "Filing Date"
            insider.columns.values[2] = "Trade Date"
            insider.columns.values[4] = "Insider Name"
            insider.columns.values[6] = "Trade Type" 
            insider.columns.values[10] = "Percentage Own"  
            insider.to_csv('insider.csv')
            
            
            for i in range(len(insider)):
                if insider.iloc[i , 2] > '2021-02-11':
                    if int(str(insider.iloc[i , 8]).replace(',' , '')) > 0:
                        count_up = count_up + 1
                    if int(str(insider.iloc[i , 8]).replace(',' , '')) < 0:
                        count_down = count_down + 1  
                    total_shares_exchanged = total_shares_exchanged + int(str(insider.iloc[i , 8]).replace(',' , ''))
            
                    insider['Buy'] = count_up
                    insider['Sell'] = count_down
                    insider['Total'] = count_up + count_down
                    insider['ShareExchanged'] = total_shares_exchanged
            
            
            return insider[['company' , 'Buy' , 'Sell' , 'Total' , 'ShareExchanged']]
            
            
stockCompetitors = peers.StockPeers('AAPL')
stockCompetitorsList = peers.StockPeers.stockPeersList(stockCompetitors)


getInstActivity = InstitutionalInvestor()

getInstitutionsInvestorList = pd.DataFrame()
getInstitutionsInvestorListAll = pd.DataFrame()

for stock in ['AAPL' , 'AMZN']:
    getInstitutionsInvestorList = InstitutionalInvestor.getInstitutionalInvestor(getInstActivity , stock)
    getInstitutionsInvestorListAll = pd.concat([getInstitutionsInvestorList , getInstitutionsInvestorListAll])


getInstitutionsInvestorListAll = getInstitutionsInvestorListAll.drop_duplicates(
  subset = ['company'], keep = 'last').reset_index(drop = True)

