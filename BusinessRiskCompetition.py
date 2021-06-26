import bs4 as bs
import requests
import pandas as pd
import nltk
import xlsxwriter


class RiskCompetitor():
    
    def __init__(self , company , companyname , filing , year , qtr):
        self._company = company
        self._companyname = companyname
        self._filing = filing
        self._year = year
        self._qtr = qtr
        
        
    def getRiskCompetitor(self):
        
#       company = 'Facebook Inc'
#       companyname = 'Facebook Inc'
#       filing = '10-Q'
#       year = 2020
#       quarter = 'QTR3'
#       get name of all filings 
        download = requests.get(f'https://www.sec.gov/Archives/edgar/full-index/{self._year}/{self._qtr}/master.idx').content
        download = download.decode("utf-8").split('\n')


        # print(download)


        for item in download:
            #company name and report type
            if (self._company in item) and (self._filing in item): 
                #print(item)
                company = item
                company = company.strip()
                splitted_company = company.split('|')
                url = splitted_company[-1]

    

        print(url) #edgar/data/1326801/0001326801-20-000076.txt

        url2 = url.split('-') 
        url2 = url2[0] + url2[1] + url2[2]
        url2 = url2.split('.txt')[0]
        print(url2) #edgar/data/1326801/000132680120000076

        to_get_html_site = 'https://www.sec.gov/Archives/' + url
        data = requests.get(to_get_html_site).content
        data = data.decode("utf-8") 
        data = data.split('FILENAME>')
        #data[1]
        data = data[1].split('\n')[0]

        print(data)

        url_to_use = 'https://www.sec.gov/Archives/'+ url2 + '/'+data
        print(url_to_use)


        resp = requests.get(url_to_use)
        soup = bs.BeautifulSoup(resp.text, 'lxml')
        print(soup)



        nltk.download('punkt')
        word_to_analyze = 'risk'
        for tag in soup.div.find_all_next('span'):
            #print(type(tag))
            tag = tag.getText()
            #print(tag)
            if word_to_analyze in tag:
                sentences = nltk.sent_tokenize(tag)
                resultRisk = [sentence for sentence in sentences]
                print(resultRisk)

        filenamespace = str(self._companyname) + "-Risk"
        filename = "%s.txt" % filenamespace
        textfile = open(filename, "w")
        for element in resultRisk:
            textfile.write(element + "\n")
        textfile.close()


        filenamespace = ""
        filename = ""
        textfile = ""
        word_to_analyze = 'compete with'
        for tag in soup.div.find_all_next('span'):
            #print(type(tag))
            tag = tag.getText()
            #print(tag)
            if word_to_analyze in tag:
              sentences = nltk.sent_tokenize(tag)
              resultCompetitor = [sentence for sentence in sentences]
              print(resultCompetitor)

        filenamespace = str(self._companyname) + "-Competitor"
        filename = "%s.txt" % filenamespace
        textfile = open(filename, "w")
        for element in resultCompetitor:
            textfile.write(element + "\n")
        textfile.close()



riskAnalysis = RiskCompetitor("Facebook Inc" ,
                              "Facebook Inc" ,
                              "10-Q", "2020" , "QTR3")


RiskCompetitor.getRiskCompetitor(riskAnalysis)