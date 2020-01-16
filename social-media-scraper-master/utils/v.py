from textblob import TextBlob
import requests
from bs4 import BeautifulSoup

class Analysis:
    def __init__(self,term):
        self.term=term
        self.subjectivity = 0
        self.sentiment = 0
        
        self.url = 'https://www.google.com/search?q={0}&source=lmns&tbm=nws'.format(self.term)
    def run(self):
        response = requests.get(self.url)
        print(response.text)
        soup = BeautifulSoup(response.text,'html.parser')
        headline_results = soup.find_all('div',class_='BNeawe s3v9rd AP7Wnd')
        for h in headline_results:
            blob = TextBlob(h.get_text())
            self.sentiment += blob.sentiment.polarity / len(headline_results)
            self.subjectivity += blob.sentiment.subjectivity / len(headline_results)
            
    
a=Analysis('trump')
a.run()
print(a.term,'Subjectivity',a.subjectivity,'sentiment',a.sentiment)
