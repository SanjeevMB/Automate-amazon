from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


# To automate User Registration and Login
# To automate scroll action using Mouse Events of Actions class
# To automate Search Product
# To automate Add to Cart Page
# To automate end-to-end functionality of Buy Product

servDriver = Service('/home/sanjeev/Downloads/chromedriver_linux64/chromedriver')

driver = webdriver.Chrome(service=servDriver)

driver.maximize_window()

def registration():

    driver.get('https://www.amazon.com/')

    driver.find_element(By.XPATH, '//*[@id="nav-signin-tooltip"]/a/span').click()

    driver.find_element(By.XPATH, '//*[@id="createAccountSubmit"]').click()

    driver.find_element(By.XPATH, '//*[@id="ap_customer_name"]').send_keys('Sanjeev')

    driver.find_element(By.XPATH, '//*[@id="ap_email"]').send_keys('sanjeev110522@gmail.com')

    driver.find_element(By.XPATH, '//*[@id="ap_password"]').send_keys('Mountblue@12345')

    driver.find_element(By.XPATH, '//*[@id="ap_password_check"]').send_keys('Mountblue@12345')

    driver.find_element(By.XPATH, '//*[@id="continue"]').click()

    time.sleep(60)

    driver.close()

# registration()

def login():

    driver.get('https://www.amazon.com/')

    driver.find_element(By.XPATH, '//*[@id="nav-signin-tooltip"]/a').click()

    driver.find_element(By.XPATH, '//*[@id="ap_email"]').send_keys('sanjeev110522@gmail.com')

    driver.find_element(By.XPATH, '//*[@id="continue"]').click()

    driver.find_element(By.XPATH, '//*[@id="ap_password"]').send_keys('Mountblue@12345')

    driver.find_element(By.XPATH, '//*[@id="signInSubmit"]').click()

    time.sleep(15)

# login()

def searchProduce():

    driver.get('https://www.amazon.com/')

    # driver.find_element(By.XPATH, '//*[@id="nav-signin-tooltip"]/a').click()
    #
    # driver.find_element(By.XPATH, '//*[@id="ap_email"]').send_keys('sanjeev110592@gmail.com')
    #
    # driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    #
    # driver.find_element(By.XPATH, '//*[@id="ap_password"]').send_keys('Dr@1prabhat')
    #
    # driver.find_element(By.XPATH, '//*[@id="signInSubmit"]').click()

    driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys('one plus')

    driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]').click()

    time.sleep(3)

searchProduce()


def addToCart():

    driver.get('https://www.amazon.com/')

    # driver.find_element(By.XPATH, '//*[@id="nav-signin-tooltip"]/a').click()
    #
    # driver.find_element(By.XPATH, '//*[@id="ap_email"]').send_keys('sanjeev110592@gmail.com')
    #
    # driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    #
    # driver.find_element(By.XPATH, '//*[@id="ap_password"]').send_keys('Dr@1prabhat')
    #
    # driver.find_element(By.XPATH, '//*[@id="signInSubmit"]').click()

    driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys('one plus')

    driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]').click()

    driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[11]/div/div/div/div/div/div[1]/div/div[2]/div/span/a').click()

    driver.find_element(By.XPATH, '//*[@id="submit.add-to-cart"]').click()

    time.sleep(20)

    driver.close()

# addToCart()

def buyProduct():

    driver.get('https://www.amazon.com/')

    driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys('one plus')

    driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]').click()

    driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[11]/div/div/div/div/div/div[1]/div/div[2]/div/span/a').click()



buyProduct()



# def scrolling():




