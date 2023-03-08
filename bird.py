import selenium
from selenium import webdriver

def getDistros():
    #check if course is on list

    #make list
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://www.qubirdhunter.com/?page_id=283")

    table = driver.find_element_by_class_name("wp-block-table")

    entries = table.find_elements_by_tag_name("tr")
    file = open("birdhunter.txt","w")
    for course in entries:
        columns = course.find_elements_by_tag_name("td")
       
        one = columns[0].text+":"+" "+columns[1].text
        two = "|Enrollment|A+|A |A-|B+|B |B-|C+|C |C-|D+|D |D-|F |GPA    |"
        spaces = (10-len(columns[2].text))*" "
        toprnt="|"+columns[2].text+spaces+"|"
        for i in range(3,17):
            spaces = (2-len(columns[i].text))*" "
            toprnt+=columns[i].text+spaces+"|"
        toprnt=toprnt[:-1]+" |"

        three = toprnt

        complete = "**" + one + "**\n" + two +"\n" + three + "\n" + "https://www.qubirdhunter.com/?page_id=283" + ";"
        file.write(complete)
    file.close()

def haveDistro(course):
    course=course.upper()

    

    if len(course.split())!=2:
        course = [course[:5]+" "+course[5:8]]
    if len(course.split()[0])!=4 or len(course.split()[1])!=3:
        return "not valid course"
    
    file = open("birdhunter.txt")
    strings = file.read().split(';')
    course=course.split()
    for string in strings:
        code = string[2:10].split()
        if course[0] == code[0] and course[1]==code[1]:
            return string
    return "not found"
        
        
        
if __name__=='__main__':
    print(haveDistro("SOFT 437"))
