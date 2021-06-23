
import requests
import pandas as pd
import StockPeers as peers



class InstitutionalInvestor():

        def __init__(self):
            # api_key = "08bfbdf1fe1e7e8908c2fcc0be1e81ff"
            self.api_key   = "802b63ba7f7d06305d7ca936e6f3b2ca"



        def getInstitutionalInvestor(self , stockList):

            change = {}
            
            for company in stockList :
                institutions = requests.get(f'https://financialmodelingprep.com/api/v3/institutional-holder/{company}?apikey=802b63ba7f7d06305d7ca936e6f3b2ca').json()
                change[company] = {}
                identify = 0
                count_down = 0
                count_up = 0
                total_shares_exchanged = 0
                for item in institutions:
                    identify = identify + 1
                    if item['dateReported'] > '2021-02-11':
                          change[company][item['dateReported']+ str(identify)] = item['change']
                          if item['change'] > 0:
                                  count_up = count_up + 1
                          if item['change'] < 0:
                                  count_down + 1
                                  total_shares_exchanged = total_shares_exchanged + item['change']
            change[company]['total'] = count_up + count_down
            change[company]['buys'] = count_up
            change[company]['sells'] = count_down
            change[company]['total_shares_exchanged'] = total_shares_exchanged
            institutions_DF = pd.DataFrame(change)
            institutions_DF = institutions_DF.T
            institutions_investment = institutions_DF.iloc[: , -4:]
            print(institutions_investment)
            
            
            


# stockCompetitors = peers.StockPeers('AAPL')
# stockCompetitorsList = peers.StockPeers.stockPeersList(stockCompetitors)


# getInstActivity = InstitutionalInvestor()
# getInstitutionsInvestorList = InstitutionalInvestor.getInstitutionalInvestor(getInstActivity , ['AAPL' , 'AMZN'])









