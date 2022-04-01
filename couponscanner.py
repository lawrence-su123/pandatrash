from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome('C:/Users/lawre/Downloads/chromedriver_win32/chromedriver.exe')
#driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')
import cv2
import pytesseract
from pytesseract import Output

def inputSurveyCode(code, lastDigits):
    global driver
    driver = webdriver.Chrome('C:/Users/lawre/Downloads/chromedriver_win32/chromedriver.exe')
    #x = Service('C:\Program Files (x86)\chromedriver.exe')
    x = Service('C:/Users/lawre/Downloads/chromedriver_win32/chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=x, options=options)
    driver.get("https://www.pandaguestexperience.com/")

    code4Digit = code.split(" ")
    for i in range(1, 6):
        inputBox = driver.find_element(By.NAME, "CN" + str(i))
        print(code4Digit[i - 1])
        inputBox.send_keys(code4Digit[i - 1])
    inputbox = driver.find_element(By.NAME, "CN6")
    inputbox.send_keys(lastDigits)

    try:
        link = driver.find_element(By.ID, "NextButton")
        link.click()
    except selenium.common.exceptions.NoSuchElementException:
        print("Wrong survey code")
        driver.quit()


def FillOutSurvey():
    nextLink = driver.find_elements(By.ID, "NextButton")
    while len(nextLink) != 0:
        optionButton = driver.find_elements(By.CLASS_NAME, "radioSimpleInput")
        for i in range(0, len(optionButton), 5):
            optionButton[i].click()
        nextLink = driver.find_elements(By.ID, "NextButton")
        if len(nextLink) == 0:
            break
        nextLink[0].click()


def main():
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    #img = cv2.imread('invoice-sample.jpg')
    imageFile = 'C:/Users/lawre/Downloads/panda_receipt_ex.jpg'
    img = cv2.imread(imageFile)
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    #print(d.keys())
    #print(d.items())
    n_boxes = len(d['text'])
    custom_config = r'--oem 3 --psm 6 outputbase digits'
    #print(pytesseract.image_to_string(img, config=custom_config))
    z = pytesseract.image_to_string(img, config=custom_config)
    z1 = z.split()
    for i in z1:
        if len(i) > 14:
            coupon = i

    code = coupon.replace("-", " ")
    lastDigits = code[len(code) - 2:len(code):]
    code = code[:len(code) - 2:]
    inputSurveyCode(code, lastDigits)
    FillOutSurvey()


if __name__ == "__main__":
    main()