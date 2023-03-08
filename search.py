import os
import requests
from bs4 import BeautifulSoup
import courseDescriptionGrabber

def searchLocal(query,location='./Definitions/'):
    firstLetter = query[0]

    fullDef = False
    if query[-4:]=="full":
        fullDef = True
        query = query.replace("full","")
        
        
    
    file=""
    for i in range(0,len(query)):
        for filename in os.listdir(location):
            if filename.startswith(query[i]):
                file = open(location+filename)
                
        if file != "":
            break
    if file == "":
        return "not found"
    else:
       
        letterlist = file.read().split(';\n')
        file.close()
        for entry in letterlist:
            definition = entry.split(':')
            name = definition[0]
            if name == query or name==query.upper() or name == query+"A" or name == query.upper() + "A":
                cleaned = definition[1].replace("*** view multiple offerings","").rstrip()
                if fullDef:
                    
                    description = courseDescriptionGrabber.getDescription(query)
                    if description == "":
                        description = "no description found"
                    cleaned = "**"+cleaned+"**: " + description
                return cleaned
        return "not found"
    
def isSubject(query):
    file = open('./CourseCodes/.subjectCodes.txt')

    codes = file.read()

    codes = codes.split(';\n')

    for code in codes:
        #print(code)
        subject = code.split(':')
        #print(subject[0])
        if query == subject[0]:
            return True
    return False #not a subject code
    

def searchEncy(query=""):

    

    file=""
    firstLetter = query[0]
    for i in range(0,len(query)):
        for filename in os.listdir('./Encyclopedia'):
            if filename.startswith(query[i]):
                file=open('./Encyclopedia/'+filename)
        if file != "":
            break
    if file =="":
        return ("error","no description found")
    else:
        letterlist = file.read().split(';\n')
        file.close()
        for entry in letterlist:
            path = entry.split(':')
            
            aliases = path[0].split(',')
            
            if query in aliases:
                
                path =  path[1]
                break
            else:
                path=""
    if path!="":     
        page = requests.get('https://www.queensu.ca/encyclopedia/'+path[0]+'/'+path)
    else:
        return ("error","no description found")
    soup = BeautifulSoup(page.content,'html.parser')

    paragraphs = soup.find_all('p')
    for tag in paragraphs:
        blurb = tag.get_text()
        if blurb != "" and len(blurb)>50:
            break
    if blurb == "":
        return ("error","no description found")
    else:
        return (soup.find_all('h1')[1].get_text(),blurb+'\nhttps://www.queensu.ca/encyclopedia/'+path[0]+'/'+path)

'''
def write():
    dic = 'abcdefghijklmnopqrstuvw'
    for i in range(0,len(dic)):
        
        page = requests.get('https://www.queensu.ca/encyclopedia/'+dic[i])
        soup = BeautifulSoup(page.content,'html.parser')
        menu=soup.find_all('ul',class_='menu')[1]
        children = menu.findChildren('a')

        file=open('./Encyclopedia/'+dic[i]+'.txt','w')
    
        for child in children:
            child = child['href'].split('/')[-1]
            spaces= child.replace('-','')
            file.write(spaces+':'+child+';\n')
        file.close
'''
if __name__ == '__main__':
    print(searchLocal("math210full",'./CourseCodes/'))
   # print(isSubject('cisc'))
   
    
    
