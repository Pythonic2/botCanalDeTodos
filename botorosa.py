import time
import os
import asyncio
from playwright.sync_api import sync_playwright
from joblib import Parallel, delayed
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from fake_useragent import UserAgent
from random import randint
tempo_inicial = time.time()





from playwright.sync_api import sync_playwright
from time import sleep

with sync_playwright() as p:
    ua = UserAgent()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page(user_agent=ua.random)
    page.goto("https://www.canaldopovo.com/")
    print(page.title())

    lista = page.query_selector_all("//div[contains(text(),'Últimas notícias')]/../div/div/h3/a")
    nova_lista = [i.get_attribute('href') for i in lista ]
    page.close()
    titulos = list()
    for i in nova_lista:
        page = browser.new_page(user_agent=ua.random)
        page.goto(i)
        try:
            banner = page.locator(f'//ins[contains(@data-revive-seq,"{randint(0,1)}")]/iframe')
            page.goto(banner.get_attribute('src'))
            page.evaluate('javascript:window.open(window.clickTag)')
        except:
            pass
        print(page.title())
        page.close()
      
        
       