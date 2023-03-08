import random
import os
from bs4 import BeautifulSoup
import requests

def randomArticle(letterChoice=""):
    if letterChoice == "" or letterChoice.lower() not in 'abcdefghijklmnopqrstuvw':
        letter = random.choice(os.listdir('./Encyclopedia'))
    else:
        letter = letterChoice+'.txt'
    
    file = open('./Encyclopedia/'+letter)
    text = file.read().split(';\n')
    file.close()
    text.pop()
    index = random.randint(0,len(text)-1)
    article = text[index].split(':')[1]
       

    page = requests.get('https://www.queensu.ca/encyclopedia/'+article[0]+'/'+article)

    soup = BeautifulSoup(page.content,'html.parser')

    paragraphs = soup.find_all('p')
    for tag in paragraphs:
        blurb = tag.get_text()
        if blurb != "" and len(blurb)>50:
            break
    if blurb == "":
        return ("error","no description found")
    else:
        return (soup.find_all('h1')[1].get_text(),blurb+'\nhttps://www.queensu.ca/encyclopedia/'+article[0]+'/'+article)

if __name__=='__main__':
    for i in range(0,120):
        try:
            
            print(randomArticle()[0])
        except:
            print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
