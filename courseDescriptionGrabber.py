'''
want to get all course codes from solus
is the format math:Mathematics
'''
'''
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import selenium
import Solus
'''
import gspread
from oauth2client.service_account import ServiceAccountCredentials
'''
def addRow(code,title,description):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name('./client_secret.json',scope)
    client = gspread.authorize(creds)

    sheet = client.open('CourseDescriptions').sheet1


    row = [code,title,description]

    row_num = len(sheet.get_all_values())+1

    sheet.insert_row(row,row_num)
'''
def getDescription(query):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name('./client_secret.json',scope)
    client = gspread.authorize(creds)

    sheet = client.open('CourseDescriptions').sheet1

    names = sheet.col_values(1)

    for i in range(0,len(names)):
        #print(names[i])
        if names[i] == query.upper() or names[i]==query or names[i] == query+"A" or names[i] == query.upper() + "A":
            return sheet.cell(i+1,3).value
     
    return ""
        
    
'''
def main():
    letters = 'abcdefghijklmnopqrstuwx'

    driver = Solus.SolusLogin(False)
    
    iframe = driver.find_element_by_id("ptifrmtgtframe")
    driver.switch_to.frame(iframe)
    
    driver.find_element_by_id("DERIVED_SSS_SCL_SSS_GO_4$83$").click()
    driver.implicitly_wait(100)

    driver.switch_to.default_content()
    driver.switch_to.frame(iframe)

    driver.find_element_by_xpath('/html/body/form/div[5]/table/tbody/tr/td/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td/table/tbody/tr[6]/td[3]/div/div/table/tbody/tr/td[8]/a').click()
    
    for i in range(19,len(letters)): #len(letters) #iterate through the letters
        addRow(letters[i],"","")
        courses=[]
        driver.implicitly_wait(100)
        driver.switch_to.default_content()
        driver.switch_to.frame(iframe)
        driver.find_element_by_id('DERIVED_SSS_BCC_SSR_ALPHANUM_'+letters[i].upper()).click()
        
        time.sleep(0.5)
        courses = driver.find_elements_by_xpath('//*[contains(@id, "DERIVED_SSS_BCC_GROUP_BOX_1$147$$")]')
        

        for j in range(0,len(courses)//3): #len(courses)//3 #iterate through the courses
            time.sleep(0.75)
            line = driver.find_element_by_id('DERIVED_SSS_BCC_GROUP_BOX_1$147$$'+str(j)).text
            parts = line.split('-')
            print(parts[0] + parts[1])
            
            
            
            driver.find_element_by_id('DERIVED_SSS_BCC_GROUP_BOX_1$147$$'+str(j)).click() #click course drop down 
            time.sleep(0.5)
            classes = driver.find_elements_by_xpath('//*[contains(@id, "CRSE_TITLE$")]') #find the elements that are the individual course codes
            driver.implicitly_wait(100)
            print(len(classes))

            for k in range(0,len(classes)//3):
                #driver.implicitly_wait(100)
                if len(classes)!=0: #as long as there exists at least 1 class
                    #time.sleep(0.3)
                    driver.implicitly_wait(100)
                    driver.switch_to.default_content()
                    driver.switch_to.frame(iframe)

                    subject = parts[0].replace(' ','')
               

                    number = driver.find_element_by_id("CRSE_NBR$"+str(k)).text.replace(' ','') #gets course code as string
                    #time.sleep(0.3)

                    title = driver.find_element_by_id("CRSE_TITLE$"+str(k)).text #gets title of course
                    #time.sleep(0.3)

                    driver.find_element_by_id("CRSE_TITLE$"+str(k)).click() #click into course

                    driver.implicitly_wait(100)
                    driver.switch_to.default_content()
                    driver.switch_to.frame(driver.find_element_by_id("ptifrmtgtframe"))

                    time.sleep(0.5)
                    driver.implicitly_wait(1)
                    pagetitle="Course List"

                    while pagetitle == "Course List":
                        time.sleep(0.1)
                        try:
                            driver.implicitly_wait(1)
                            pagetitle = driver.find_element_by_xpath("/html/body/form/div[5]/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td/table/tbody/tr[4]/td[2]/div/span").text
                        except:
                            driver.implicitly_wait(1)
                            pagetitle=driver.find_element_by_xpath("/html/body/form/div[5]/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td/table/tbody/tr[4]/td[2]/div/span").text
                        print(pagetitle)            

                    if pagetitle[-3:] == "ail":
                        driver.implicitly_wait(0.1)
                        descript = driver.find_elements_by_id("SSR_CRSE_OFF_VW_DESCRLONG$0")
                        
                        if len(descript)!=0:
                            descript = descript[0].text
                        else:
                            descript = ""
                        
                        #time.sleep(0.3)
                        descript = descript.replace(":","").replace(";","")
                        #print(descript)
                        driver.implicitly_wait(1)
                        driver.find_element_by_id("DERIVED_SAA_CRS_RETURN_PB").click()
                    elif pagetitle[-3:]=="ing":
                        driver.implicitly_wait(1)
                        driver.find_element_by_id("CAREER$0").click()

                        driver.implicitly_wait(1)
                        driver.switch_to.default_content()
                        driver.switch_to.frame(driver.find_element_by_id("ptifrmtgtframe"))

                        driver.implicitly_wait(1)
                        descript = driver.find_elements_by_id("SSR_CRSE_OFF_VW_DESCRLONG$0")                       
                        if len(descript)!=0:
                            descript = descript[0].text
                        else:
                            descript = ""
                    
                    
                        descript = descript.replace(":","").replace(";","")
                        time.sleep(0.3)
                        driver.implicitly_wait(1)
                        driver.find_element_by_id("DERIVED_SAA_CRS_RETURN_PB").click()

                        driver.implicitly_wait(1)
                        driver.switch_to.default_content()
                        driver.switch_to.frame(driver.find_element_by_id("ptifrmtgtframe"))
                        driver.implicitly_wait(1)
                        driver.find_element_by_id("DERIVED_SSS_SEL_RETURN_PB").click()
                    else:
                        descript = ""

                    

                    lines =  subject + number + ": **" + title +"** "+ descript +";\n"
                    addRow(subject+number,title,descript)
                    
            driver.implicitly_wait(100)
            driver.switch_to.default_content()
            driver.switch_to.frame(driver.find_element_by_id("ptifrmtgtframe"))
        
            driver.find_element_by_id('DERIVED_SSS_BCC_GROUP_BOX_1$147$$'+str(j)).click()#close course  Dropdown
            driver.implicitly_wait(100)
            driver.switch_to.default_content()
            driver.switch_to.frame(iframe)
            time.sleep(0.3)
            
            
        
        time.sleep(0.5)
    
if __name__ == '__main__':
    main()
'''
