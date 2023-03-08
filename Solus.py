from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

def SolusLogin(silent=True):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--log-level=3")

    if silent:
        driver = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)
    else:
        driver = webdriver.Chrome('./chromedriver')
    driver.get("https://my.queensu.ca/sidebar/20")
    

    username= open('netID.txt').read() #input("Enter a Username: ")
    password = open('password.txt').read() #input("Enter a Password: ")

    
    
    usernameField = driver.find_element_by_id("username")
    passwordField = driver.find_element_by_id("password")


    usernameField.clear()
    usernameField.send_keys(username)

    passwordField.clear()
    passwordField.send_keys(password)

    passwordField.send_keys(Keys.RETURN)

    

    

    return driver

def main():

    
    driver = SolusLogin(False)

    driver.implicitly_wait(10)

    iframe = driver.find_element_by_id("ptifrmtgtframe")
    driver.switch_to.frame(iframe)
    select = Select(driver.find_element_by_xpath('/html/body/form/div[5]/table/tbody/tr/td/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td/table/tbody/tr[4]/td[2]/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/div/table/tbody/tr/td/table/tbody/tr[6]/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/div/select'))
    select.select_by_visible_text('Grades')
    driver.find_element_by_id("DERIVED_SSS_SCL_SSS_GO_1").click()

    driver.switch_to.default_content()
    driver.switch_to.frame(iframe)
    driver.find_element_by_id("SSR_DUMMY_RECV1$sels$1$$0").click()
    driver.find_element_by_id("DERIVED_SSS_SCT_SSR_PB_GO").click()

    driver.switch_to.default_content()
    driver.switch_to.frame(iframe)
    print(driver.find_element_by_id("CLS_LINK$0").text + "  | " + driver.find_element_by_id("STDNT_ENRL_SSV1_CRSE_GRADE_OFF$0").text)
    print(driver.find_element_by_id("CLS_LINK$1").text + "  | " + driver.find_element_by_id("STDNT_ENRL_SSV1_CRSE_GRADE_OFF$1").text)
    print(driver.find_element_by_id("CLS_LINK$2").text + "  | " + driver.find_element_by_id("STDNT_ENRL_SSV1_CRSE_GRADE_OFF$2").text)
    print(driver.find_element_by_id("CLS_LINK$3").text + "  | " + driver.find_element_by_id("STDNT_ENRL_SSV1_CRSE_GRADE_OFF$3").text)
    print(driver.find_element_by_id("CLS_LINK$4").text + "  | " + driver.find_element_by_id("STDNT_ENRL_SSV1_CRSE_GRADE_OFF$4").text)
    print(driver.find_element_by_id("CLS_LINK$5").text + "  | " + driver.find_element_by_id("STDNT_ENRL_SSV1_CRSE_GRADE_OFF$5").text)

    driver.close()
    driver.quit()

if __name__ == '__main__':
    main()
