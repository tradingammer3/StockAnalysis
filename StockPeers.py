# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 17:08:39 2021

@author: Aamerali.Sayyed
"""

import requests
import pandas as pd 


class StockPeers():

    def __init__(self , stock):
        self._stock = stock
        self.api_key = '802b63ba7f7d06305d7ca936e6f3b2ca'
        
    def stockPeersList(self):
        url = f'https://financialmodelingprep.com/api/v4/stock_peers?symbol={self._stock}&apikey={self.api_key}'
        peers = requests.get(url).json()
        peers = peers[0]['peersList']
        return peers