import requests
import pandas as pd

#demo= 'your api key'

company = 'AAPL'

transcript = requests.get(f'https://financialmodelingprep.com/api/v3/earning_call_transcript/{company}?quarter=3&year=2020&apikey=08bfbdf1fe1e7e8908c2fcc0be1e81ff').json()

transcript = transcript[0]['content'].split('\n')
print(transcript)

earnings_call = pd.DataFrame(transcript,columns=['content'])
word_to_analyze = 'expect'

analysis = earnings_call[earnings_call['content'].str.contains(word_to_analyze)]
text_earnings = analysis['content'].values

print(text_earnings)

for text in text_earnings:
  for phrase in text.split('. '):
    if word_to_analyze in phrase:
      print(phrase)
      print()