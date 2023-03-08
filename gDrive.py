import gspread
from oauth2client.service_account import ServiceAccountCredentials

import search

def addRow(key,value):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name('./client_secret.json',scope)
    client = gspread.authorize(creds)

    sheet = client.open('DeaneBot').sheet1


    row = [key,value]

    row_num = len(sheet.get_all_values())+1

    sheet.insert_row(row,row_num)

    print("added "+key+" to sheet")
    

def delRow(key):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name('./client_secret.json',scope)
    client = gspread.authorize(creds)

    sheet = client.open('DeaneBot').sheet1
    num_deleted = 0

    names = sheet.col_values(1)

    for i in range(0,len(names)):
        if names[i] == key:
            
            sheet.delete_rows(i+1)#delete row with key in it (indexed at 1)
            return "deleted"
            
        
    return "nothing to delete"

def saveNewRows():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
    client = gspread.authorize(creds)

    sheet = client.open('DeaneBot').sheet1
    num_deleted = 0
    
    names = sheet.col_values(1)

    file = ""
    for i in range(0,len(names)):
        result = search.searchLocal(names[i])

        if result == "not found":
            file = open('./Definitions/'+names[i][0]+'.txt','a',errors="ignore")
            file.write(names[i].lower().replace(" ",'')+":"+sheet.cell(i+1, 2).value.replace("https","")+";\n")
            file.close()


if __name__ == "__main__":

    
    saveNewRows()
    
