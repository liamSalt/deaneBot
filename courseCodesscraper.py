'''
want to get all course codes from solus
is the format math:Mathematics
'''

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import selenium
import Solus

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
    file = open('./CourseCodes/.courseDescriptions.txt','a')#+letters[i]+'.txt','a')
    for i in range(0,len(letters)): #len(letters) #iterate through the letters
        courses=[]
        driver.implicitly_wait(100)
        driver.switch_to.default_content()
        driver.switch_to.frame(iframe)
        driver.find_element_by_id('DERIVED_SSS_BCC_SSR_ALPHANUM_'+letters[i].upper()).click()
        
        time.sleep(0.5)
        courses = driver.find_elements_by_xpath('//*[contains(@id, "DERIVED_SSS_BCC_GROUP_BOX_1$147$$")]')
        

        for j in range(0,len(courses)//3): #len(courses)//3 #iterate through the courses
            time.sleep(0.5)
            line = driver.find_element_by_id('DERIVED_SSS_BCC_GROUP_BOX_1$147$$'+str(j)).text
            parts = line.split('-')
            print(parts[0] + parts[1])
            
            #file.write(parts[0].lower().replace(' ','')+':'+parts[1] + ';\n')
            
            driver.find_element_by_id('DERIVED_SSS_BCC_GROUP_BOX_1$147$$'+str(j)).click() #click course drop down 
            time.sleep(0.5)
            classes = driver.find_elements_by_xpath('//*[contains(@id, "CRSE_TITLE$")]') #find the elements that are the individual course codes
            driver.implicitly_wait(100)
            print(len(classes))

            for k in range(0,len(classes)//3):
                #driver.implicitly_wait(100)
                if len(classes)!=0: #as long as there exists at least 1 class
                    time.sleep(0.3)
                    driver.implicitly_wait(100)
                    driver.switch_to.default_content()
                    driver.switch_to.frame(iframe)

                    subject = parts[0].replace(' ','')
               

                    number = driver.find_element_by_id("CRSE_NBR$"+str(k)).text.replace(' ','') #gets course code as string
                    time.sleep(0.3)

                    title = driver.find_element_by_id("CRSE_TITLE$"+str(k)).text #gets title of course
                    time.sleep(0.3)

                    driver.find_element_by_id("CRSE_TITLE$"+str(k)).click() #click into course

                    driver.implicitly_wait(100)
                    driver.switch_to.default_content()
                    driver.switch_to.frame(driver.find_element_by_id("ptifrmtgtframe"))

                    descript = driver.find_element_by_id("SSR_CRSE_OFF_VW_DESCRLONG$0").text.replace(":","").replace(";","")
        
                    #print(subject + number + ":" + descrip)

                    lines =  subject + number + ":" + title + ";\n"
                    file.write(lines)
            driver.find_element_by_id('DERIVED_SSS_BCC_GROUP_BOX_1$147$$'+str(j)).click()
            '''
            time.sleep(0.3)
            
            
        
        time.sleep(0.5)
    file.close()
if __name__ == '__main__':
    main()
