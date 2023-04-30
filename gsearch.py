import json
import requests
from bs4 import BeautifulSoup
import re
    
class googlesearch:
    def __init__(self,question,options):
        self.question = question
        self.options = options
    def results(self):
        query=self.question.replace(" ","+")
        googlelink = "https://www.google.com/search?q="
        url = f"{googlelink}{query}&num=50"
        headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'}
        page = requests.get(url,headers=headers).text
        soup = BeautifulSoup(page, 'html.parser')
        found_results=[]
        titles = soup.find_all('h3')
        descriptions = soup.find_all('span', attrs={'class': 'st'})
        option1= self.options[0].lower().replace("'","")
        option2= self.options[1].lower().replace("'","")
        option3= self.options[2].lower().replace("'","")
        count1=0
        count2=0
        count3=0
        response = {'scores': {}}
        for option in self.options:
            response['scores'][option] = 0
            for desc in descriptions:
                if option.lower() in desc.text.lower().replace("\n"," "):
                    response['scores'][option]+=1
            for desc in titles:
                if option.lower() in desc.text.lower().replace("\n"," "):
                    response['scores'][option]+=1
        binglink = "https://www.bing.com/search?q="
        url = f"{binglink}{query}&num=50"
        headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'}
        page = requests.get(url,headers=headers).text
        soup = BeautifulSoup(page, 'html.parser')
        titles = soup.find_all('h2')
        descriptions = soup.find_all('p')
        for option in self.options:
        # response['scores'][option] = 0
            for desc in descriptions:
                if option.lower() in desc.text.lower().replace("\n"," "):
                    response['scores'][option]+=1
            for desc in titles:
                if option.lower() in desc.text.lower().replace("\n"," "):
                    response['scores'][option]+=1
        asklink = "https://www.ask.com/web?q="
        url = f"{asklink}{query}"
        headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'}
        page = requests.get(url,headers=headers).text
        soup = BeautifulSoup(page, 'html.parser')
        found_results=[]
        titles = soup.find_all('div', attrs={'class': 'PartialSearchResults-item-title'})
        descriptions = soup.find_all('p', attrs={'class': 'PartialSearchResults-item-abstract'})
        for option in self.options:
            for desc in descriptions:
                if option.lower() in desc.text.lower().replace("\n"," "):
                    response['scores'][option]+=1
            for desc in titles:
                if option.lower() in desc.text.lower().replace("\n"," "):
                    response['scores'][option]+=1
        #for Option,scores in response['scores'].items():
        #    print(f"results for {Option} : {scores}")
        return response