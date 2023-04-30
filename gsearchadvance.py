import json
import requests
from bs4 import BeautifulSoup
import re
    
class googlesearch:
    def __init__(self,question=None,options=None):
        self.question = question
        self.options = options
    def advanceSearch(self,question,mainOption,advanceOptions):
        query=question.replace(" ","+")
        mainOptionq = mainOption.replace(" ","+")
        googlelink = "https://www.google.com/search?q="
        url = f'{googlelink}{query}+"{mainOptionq}"&num=50'
        #print(url)
        headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'}
        page = requests.get(url,headers=headers).text
        soup = BeautifulSoup(page, 'html.parser')
       # print(soup)
        titles = soup.find_all('h3')
        #print(titles)
        descriptions = soup.find_all('span', attrs={'class': 'st'})
       # print(descriptions)
        response = {}
        response[mainOption] = 0
        ignorelist = ['a','the','The','A','As','in','In','at','At']
        for option in advanceOptions:
            response[option]=0
            optionlist = option.split(" ")
            for ignore in ignorelist:
                if ignore in optionlist:
                    optionlist.remove(ignore)
            for desc in descriptions:
                if option.lower() in desc.text.lower().replace("\n"," "):
                    response[option]+=1
            for desc in titles:
                if option.lower() in desc.text.lower().replace("\n"," "):
                    response[option]+=1
        print(response)
        return response




    def results(self):
        response = {'scores': {}}
        #print(self.options)
        for option in self.options:
            response['scores'][option] = 0
        for option in self.options:
            advanceOptions = self.options.copy()
            advanceOptions.remove(option)
            queryResults = googlesearch().advanceSearch(self.question,option,advanceOptions)
            response['scores'][option] =response['scores'][option] +queryResults[option]
            for ops in advanceOptions:
                response['scores'][ops] +=queryResults[ops]
        
        return response