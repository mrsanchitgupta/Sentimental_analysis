from textblob import TextBlob
import requests
from bs4 import BeautifulSoup
import pandas as pd
from sys import argv

class Analysis:
    def __init__(self,term):
        self.term=term
        self.subjectivity = 0
        self.sentiment = 0
        self.url = 'https://www.google.com/search?q={0}&source=lnms&tbm=nws'.format(self.term)
    def run(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text,'html.parser')
        headline_results = soup.find_all('div',class_='BNeawe s3v9rd AP7Wnd')
        df = pd.DataFrame(headline_results,columns=['review'])
        df.to_csv('sentiments.csv')
        for h in headline_results:
            blob = TextBlob(h.get_text())
            self.sentiment += blob.sentiment.polarity / len(headline_results)
            self.subjectivity += blob.sentiment.subjectivity / len(headline_results)
            
            
       
a=Analysis(argv[1])
a.run()
print(a.term,'Subjectivity',a.subjectivity,'sentiment',a.sentiment)
