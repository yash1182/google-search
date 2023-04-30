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
        response = {'scores': {}}
        ignorelist = ['a','the','The','A','As']
        for option in self.options:
            response['scores'][option] = 0
            optionlist = option.split(" ")
            for ignore in ignorelist:
                if ignore in optionlist:
                    optionlist.remove(ignore)
            for desc in descriptions:
                for abc in optionlist:
                    if abc.lower() in desc.text.lower().replace("\n"," "):
                        response['scores'][option]+=1
                for desc in titles:
                    if abc.lower() in desc.text.lower().replace("\n"," "):
                        response['scores'][option]+=1

        return response