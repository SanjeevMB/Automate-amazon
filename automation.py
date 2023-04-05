from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


# To automate User Registration and Login
# To automate scroll action using Mouse Events of Actions class
# To automate Search Product
# To automate Add to Cart Page
# To automate end-to-end functionality of Buy Product

servDriver = Service('/home/sanjeev/Downloads/chromedriver_linux64/chromedriver')

driver = webdriver.Chrome(service=servDriver)

driver.maximize_window()

# driver.implicitly_wait(10)

def registration():

    driver.get('https://www.amazon.in/')

    driver.find_element(By.XPATH, '//*[@id="nav-signin-tooltip"]/a/span').click()

    driver.find_element(By.XPATH, '//*[@id="createAccountSubmit"]').click()

    driver.find_element(By.XPATH, '//*[@id="ap_customer_name"]').send_keys('Sanjeev')

    driver.find_element(By.XPATH, '//*[@id="ap_phone_number"]').send_keys('9415227466')

    driver.find_element(By.XPATH, '//*[@id="ap_password"]').send_keys('Mountblue@12345')

    driver.find_element(By.XPATH, '//*[@id="continue"]').click()

    time.sleep(5)

# registration()

def login():

    driver.get('https://www.amazon.in/')

    driver.find_element(By.XPATH, '//*[@id="nav-signin-tooltip"]/a').click()

    driver.find_element(By.XPATH, '//*[@id="ap_email"]').send_keys('8808760096')

    driver.find_element(By.XPATH, '//*[@id="continue"]').click()

    driver.find_element(By.XPATH, '//*[@id="ap_password"]').send_keys('Dr@1prabhat')

    driver.find_element(By.XPATH, '//*[@id="signInSubmit"]').click()

    time.sleep(2)

login()

def scrolling():

    action = ActionChains(driver)

    first = driver.find_element(By.XPATH, '//*[@id="nav-hamburger-menu"]')

    second = driver.find_element(By.XPATH, '//*[@id="nav-xshop"]/a[1]')

    third = driver.find_element(By.XPATH, '//*[@id="nav-xshop"]/a[2]')

    fourth = driver.find_element(By.XPATH, '//*[@id="nav-xshop"]/a[4]')

    time.sleep(2)

    action.move_to_element(first).move_to_element(second).move_to_element(third).move_to_element(fourth).click().perform()

    driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')

    time.sleep(2)

    driver.execute_script('window.scrollBy(0,-document.body.scrollHeight)')

    time.sleep(2)

scrolling()

def searchProduct():

    driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys('oneplus')

    driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]').click()

    driver.execute_script('window.scrollBy(0,2000),""')

    time.sleep(5)

searchProduct()

def addToCart():

    # driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys('oneplus')
    #
    # driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]').click()

    driver.find_element(By.XPATH, '//*[@id="search"]/span[1]/div/div[13]/div/div/div/div[1]/span/a').click()

    driver.find_element(By.XPATH, '//input[@id="add-to-cart-button"]').click()

    time.sleep(20)

addToCart()

# def buyProduct():


# buyProduct()





