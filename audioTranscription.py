# Upwork Task 

import requests

from bs4 import BeautifulSoup as bs
import pandas as pd
import time

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def get_info():

  list_one = []
  list_two = []
  
  master_list = []

  options = webdriver.ChromeOptions()
  service = webdriver.chrome.service.Service(ChromeDriverManager().install())

  driver = webdriver.Chrome(service=service, options=options)
  driver.get(f"https://www.tapesearch.com/episode/is-neurodiversity-really-a-superpower-in-business-dan-harris/MrZUpL8iMmsbYXqATgfqr9")

  time.sleep(5)
  html_code = driver.page_source

  soup = bs(html_code, "html.parser")
  time.sleep(5)
  table = soup.find("table")

  transcription_times = table.find_all("p", {"class": "MuiTypography-root MuiTypography-body1 MuiTypography-alignCenter css-1afvpvs"})
  for transcription_time in transcription_times: 
    transcription_time = transcription_time.text
    list_one.append(transcription_time)

  transcription_texts = table.find_all("p", {"class": "MuiTypography-root MuiTypography-body1 css-dezo25"})
  for transcription_text in transcription_texts: 
    if transcription_text.text != "...":
      transcription_text = transcription_text.text
      list_two.append(transcription_text)

  for i in range(min(len(list_one), len(list_two))):
  transcription_info = {
    "Transcription Time": list_one[i],
    "Transcription Text": list_two[i]
  }

  master_list.append(transcription_info)

  df = pd.DataFrame(master_list)
  df.to_csv("trans_info2.txt", index=False)
  print("File Created.")
  driver.quit()

get_info()
