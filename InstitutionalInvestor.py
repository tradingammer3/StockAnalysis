
import requests
import pandas as pd
import StockPeers as peers
import time as dt



class InstitutionalInvestor():

        def __init__(self):
            self.api_key = "08bfbdf1fe1e7e8908c2fcc0be1e81ff"
            # self.api_key   = "802b63ba7f7d06305d7ca936e6f3b2ca"



        def getInstitutionalInvestor(self , ticker):
            
            stock = str(ticker)
            change = {}
            change[stock] = {}
            # for company in stock:
            url = ''    
            url = 'https://financialmodelingprep.com/api/v3/institutional-holder/' + stock + '?apikey=802b63ba7f7d06305d7ca936e6f3b2ca'   
            institutions = requests.get(url).json()
            # institutions = requests.get(f'https://financialmodelingprep.com/api/v3/institutional-holder/stock?apikey=802b63ba7f7d06305d7ca936e6f3b2ca').json()
            identify = 0
            count_down = 0
            count_up = 0
            total_shares_exchanged = 0
            for item in institutions:
                identify = identify + 1
                if item['dateReported'] > '2021-02-11':
                    change[stock][item['dateReported']+ str(identify)] = item['change']
                    if item['change'] > 0:
                        count_up = count_up + 1
                    if item['change'] < 0:
                        count_down = count_down + 1
                        
                    total_shares_exchanged = total_shares_exchanged + item['change']
            
            change[stock]['total'] = count_up + count_down
            change[stock]['buys'] = count_up
            change[stock]['sells'] = count_down
            change[stock]['total_shares_exchanged'] = total_shares_exchanged
            institutions_DF = pd.DataFrame(change)
            institutions_DF = institutions_DF.T
            institutions_investment = institutions_DF.iloc[: , -4:]
        
            return institutions_investment
            
            
            


stockCompetitors = peers.StockPeers('AAPL')
stockCompetitorsList = peers.StockPeers.stockPeersList(stockCompetitors)


getInstActivity = InstitutionalInvestor()
getInstitutionsInvestorList = InstitutionalInvestor.getInstitutionalInvestor(getInstActivity , 'AMZN')
# InstitutionsInvestorList = pd.DataFrame()
# InstitutionsInvestorListAll = pd.DataFrame()
# for stock in ['AAPL' , 'AMZN']:
#     InstitutionsInvestorList = InstitutionalInvestor.getInstitutionalInvestor(getInstActivity , str(stock))
#     InstitutionsInvestorListAll = pd.concat([InstitutionsInvestorListAll , InstitutionsInvestorList] , axis = 1)
#     dt.sleep(90)







