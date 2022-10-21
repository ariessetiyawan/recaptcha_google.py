import random
import urllib
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import FirefoxProfile
import os
import sys
import time
import requests
import winreg
import pydub
import urllib
from speech_recognition import Recognizer, AudioFile
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from random import uniform, randint,choice

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
user_agents = user_agent_rotator.get_user_agents()
user_agent = user_agent_rotator.get_random_user_agent()
audioToTextDelay = 10
delayTime = 5
audioFile = "\\payload.mp3"
URL = "https://www.google.com/recaptcha/api2/demo"
browserP=[0,1,2,3]
if random.randint(0,1)==1:
	browserP=browserP[::-1]
xxb=choice(browserP)
#xxb=1
#reg_set()
#print('browser',xxb)
driver_path = r"C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

def perform_actions(driver, keys):
    actions = ActionChains(driver)
    actions.send_keys(keys)
    time.sleep(2)
    print('Performing Actions!')
    actions.perform()
def delete_cache(driver):
    driver.execute_script("window.open('')")  # Create a separate tab than the main one
    driver.switch_to.window(driver.window_handles[-1])  # Switch window to the second tab
    driver.get('chrome://settings/clearBrowserData')  # Open your chrome settings.
    perform_actions(driver, Keys.TAB * 2 + Keys.DOWN * 4 + Keys.TAB * 5 + Keys.ENTER)  # Tab to the time select and key down to say "All Time" then go to the Confirm button and press Enter
    driver.close()  # Close that window
    driver.switch_to.window(driver.window_handles[0])  # Switch Selenium controls to the original tab to continue normal functionality.
def saveFile(content,filename):
	with open(filename, "wb") as handle:
		for data in content.iter_content():
			handle.write(data)
def delay():
    time.sleep(random.randint(2, 3))
def audioToText(audioFile):
    path=os.getcwd()
    sound = pydub.AudioSegment.from_mp3(audioFile).export(path+"\\audio.wav", format="wav")
    recognizer = Recognizer()
    recaptcha_audio = AudioFile(path+"\\audio.wav")
    with recaptcha_audio as source:
        audio = recognizer.record(source)
    #text = recognizer.recognize_google(audio, language="id-ID")
    text = recognizer.recognize_google(audio, language="en-EN")
    return text
try:
    # create chrome driver
    option = webdriver.ChromeOptions()
    option.add_argument('--disable-notifications')
    option.add_argument('--mute-audio')
    option.add_argument(f'user-agent={user_agent}')
    option.add_argument("--disable-infobars")
   
    if xxb==1:
        from selenium.webdriver.chrome.service import Service as BraveService
        from webdriver_manager.chrome import ChromeDriverManager
        from webdriver_manager.core.utils import ChromeType
        option.binary_location = brave_path
        option.add_experimental_option("excludeSwitches", ["enable-automation"])
        option.add_experimental_option('useAutomationExtension', False)
        #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
        driver = webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()),options=option)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        delete_cache(driver)
    elif xxb==2:
        from selenium.webdriver.firefox.service import Service
        from selenium.webdriver.firefox.service import Service as FirefoxService
        from webdriver_manager.firefox import GeckoDriverManager
        options = Options()  # Configure options for Firefox.
        options.add_argument('--log-level=3')  # No logs is printed.
        options.add_argument('--mute-audio')  # Audio is muted.
        options.set_preference('intl.accept_languages', 'en,en-US')
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)
    elif xxb==3:
        from selenium.webdriver.edge.service import Service as EdgeService
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        option.add_experimental_option("excludeSwitches", ["enable-automation"])
        option.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        delete_cache(driver)
    delay()
    driver.delete_all_cookies() 
    # go to website which have recaptcha protection
    driver.get(URL)
    delay()
    wait=WebDriverWait(driver, 30)
except Exception as e:
    sys.exit(
        "[-] Please update the chromedriver.exe in the webdriver folder according to your chrome version:https://chromedriver.chromium.org/downloads")
btnsubmit=wait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="recaptcha-demo-submit"]')))
action = ActionChains(driver)
googleClass = driver.find_element(By.XPATH,'//div[@class="g-recaptcha"]')
time.sleep(2)
outeriframe = googleClass.find_element(By.XPATH,'//iframe[@title="reCAPTCHA"]')
time.sleep(1)
outeriframe.click()
time.sleep(2)
allIframesLen = driver.find_elements(By.TAG_NAME,'iframe')
time.sleep(1)
audioBtnFound = False
audioBtnIndex = -1
for index in range(len(allIframesLen)):
    driver.switch_to.default_content()
    iframe =  driver.find_elements(By.TAG_NAME,'iframe')[index]
    driver.switch_to.frame(iframe)
    driver.implicitly_wait(delayTime)
    try:
        audioBtn = driver.find_element(By.XPATH,'//button[@id="recaptcha-audio-button"]') or driver.find_element(By.XPATH,'//button[@id="recaptcha-anchor"]')
        audioBtn.click()
        audioBtnFound = True
        audioBtnIndex = index
        break
    except Exception as e:
        pass
if audioBtnFound:
    try:
        buttonklik=False
        while True:
            try:
                href = driver.find_element(By.XPATH,'//audio[@id="audio-source"]')
                href=href.get_attribute('src')
                urllib.request.urlretrieve(href, os.getcwd() + audioFile)
                #response = requests.get(href, stream=True)
                #saveFile(response,filename)
                response = audioToText(os.getcwd() + '/' + audioFile)
                driver.switch_to.default_content()
                iframe =  driver.find_elements(By.TAG_NAME,'iframe')[audioBtnIndex]
                driver.switch_to.frame(iframe)
                inputbtn = driver.find_element(By.XPATH,'//*[@id="audio-response"]')
                inputbtn.send_keys(response)
                inputbtn.send_keys(Keys.ENTER)
                time.sleep(2)
                errorMsg = driver.find_element(By.XPATH,'//*[@class="rc-audiochallenge-error-message"]')
                if errorMsg.text == "" or errorMsg.value_of_css_property('display') == 'none':
                    print("Success")
                    buttonklik=True                   
                    break
            except Exception as e:
                print(e)
                pass
        while True:
            if buttonklik:
                driver.switch_to.default_content()
                inpt=wait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="recaptcha-demo-submit"]')))
                inpt.click()
                buttonklik=False
                time.sleep(5)
                driver.close()
                driver.quit()
                break
    except Exception as e:
        print(e)
        print('Caught. Need to change proxy now')
else:
	print('Button not found. This should not happen.')



