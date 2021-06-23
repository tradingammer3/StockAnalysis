import pandas as pd
from bs4 import BeautifulSoup
import StockPeers as peers


class InstitutionalInvestor():

        def __init__(self ):
            pass
        
        def getInstitutionalInvestor(self , stockList):
            
            identify = 0
            count_down = 0
            count_up = 0
            total_shares_exchanged = 0
            insider = pd.DataFrame()
            
            for company in ['AAPL']:
                insider1 = pd.read_html(f'http://openinsider.com/screener?s={company}&o=&pl=&ph=&ll=&lh=&fd=730&fdr=&td=0&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&xs=1&vl=&vh=&ocl=&och=&sic1=-1&sicl=100&sich=9999&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=500&page=1')
                insider1 = insider1[-3]
                insider1['company'] = company
                insider1.rename(columns = {"FilingÂ Date":"Fil Date", "TradeÂ Date":"Trade Date"}, inplace = True)
                insider = pd.concat([insider,insider1])

            
            insider.to_csv('insider.csv')
                
                
                

            #         identify = identify + 1                    
            #         if insider1.iloc[index , 3] > '2021-02-11':
            #             if insider1['Qty'][index] > 0:
            #                 count_up = count_up + 1
            #             if insider1['Qty'][index] < 0:
            #                 count_down = count_down + 1        
                    
            #         total_shares_exchanged = total_shares_exchanged + insider1['Qty'][index]
                    
            
            # insider1['Buy'] = count_up
            # insider1['Sell'] = count_down
            # insider1['Total'] = count_up + count_down
            # insider1['ShareExchanged'] = total_shares_exchanged
            
            # insider = pd.concat([insider,insider1])
            return insider
            
            
stockCompetitors = peers.StockPeers('AAPL')
stockCompetitorsList = peers.StockPeers.stockPeersList(stockCompetitors)


getInstActivity = InstitutionalInvestor()
getInstitutionsInvestorList = InstitutionalInvestor.getInstitutionalInvestor(getInstActivity , stockCompetitorsList)


