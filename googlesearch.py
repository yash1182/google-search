import json
import requests
from bs4 import BeautifulSoup
import re
from dhooks import Webhook, Embed

#===========================

ignored_word_list =['the','is','to','for']
negetive_word_list = ['not','never']

#============================

def google_search(question,options):

    query=question.replace(" ","+")
    googlelink = "https://www.google.com/search?q="
    url = f"{googlelink}{query}&num=50"
    headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'}
    page = requests.get(url,headers=headers).text
    soup = BeautifulSoup(page, 'html.parser')
    found_results=[]
    #result_block = soup.find_all('div', attrs={'class': 'r'})
    titles = soup.find_all('h3')
    descriptions = soup.find_all('span', attrs={'class': 'st'})
    option1= options[0].lower().replace("'","")
    option2= options[1].lower().replace("'","")
    option3= options[2].lower().replace("'","")
    count1=0
    count2=0
    count3=0
    response = {'scores': {}}
    for option in options:
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
    for option in options:
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
    for option in options:
        for desc in descriptions:
            if option.lower() in desc.text.lower().replace("\n"," "):
                response['scores'][option]+=1
        for desc in titles:
            if option.lower() in desc.text.lower().replace("\n"," "):
                response['scores'][option]+=1
    for Option,scores in response['scores'].items():
        print(f"results for {Option} : {scores}")
    return response
if __name__ == "__main__":
    question = "Where in the world is the largest life size house, made from Lego bricks built?"
    option1 = "Stoke on Trent, England"
    option2 = "Dorking, England"
    option3 = "Hebden Bridge, England"
    option4 = "Birnbaum"
    options=[option1,option2,option3]#,option4]
    response = google_search(question,options)
