import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

def main():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--log-level=3")

    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://gpabars.fandom.com/wiki/Extracurricular_Bars")
    '''
    time.sleep(5)
    button = driver.find_element_by_id("ContentWarningApprove")
    time.sleep(5)
    button.click()
    driver.implicitly_wait(1000)
    '''
    bars = driver.find_elements_by_tag_name('a')

    for i in range(80,len(bars)-75):
        name = bars[i].get_attribute('text').lower().replace(" ",'')
        time.sleep(0.5)
        link = bars[i].get_attribute('href').split('/wiki/')[1]
        time.sleep(0.5)
        if name != "edit":
            driver.get("https://gpabars.fandom.com/wiki/"+link)
            time.sleep(0.5)
            header = driver.find_element_by_xpath("/html/body/div[3]/section/div[2]/header/div[1]/h1").text
            time.sleep(2)
            div = driver.find_element_by_id("mw-content-text")
            blurb= div.find_element_by_xpath("./p").text
            print(header+':' + blurb )
        time.sleep(0.5)
if __name__=='__main__':
    main()
