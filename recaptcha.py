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

'''---------------------------------'''
