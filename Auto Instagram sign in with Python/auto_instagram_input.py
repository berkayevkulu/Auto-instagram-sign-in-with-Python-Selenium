import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#chrome'u açık tutuyor / keeps the chrome open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#input username and password
user = input("username: ")
passw = input("password: ")

#chrome açılış /opens chrome
browser = webdriver.Chrome()
browser.get("https://instagram.com")


#pencere boyutu tam ekran / max size window
browser.maximize_window()
time.sleep(2)


#username,kullanıcı adı input seçme / username and password location
username = browser.find_element(By.NAME, 'username')
password = browser.find_element(By.NAME, 'password')

#username,password yazdırma / inputs username and password
username.send_keys(user)
time.sleep(1)
password.send_keys(passw)
time.sleep(1)

#login butonuna basma / clicks login button
login = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
login.click()
time.sleep(5)


#şimdi değil butonuna tıklama / clicks not now button
not_now = browser.find_element(By.XPATH, '//button[text()="Şimdi Değil"]') #/for english instagram users change "Şimdi Değil" to "Not Now"
not_now.click()
time.sleep(1)

#2. şimdi değil butonuna tıklama / clicks 2. not now button
not_now_2 = browser.find_element(By.XPATH, '//button[text()="Şimdi Değil"]') #/for english instagram users change "Şimdi Değil" to "Not Now"
not_now_2.click()

time.sleep(99999)