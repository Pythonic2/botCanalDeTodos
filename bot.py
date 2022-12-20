import time
import os
import asyncio
from playwright.sync_api import sync_playwright
from joblib import Parallel, delayed
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from fake_useragent import UserAgent
from time import sleep

tempo_inicial = time.time()




def calcular(arquivo):
    with sync_playwright() as p:
        
        browser = p.chromium.launch(headless=False)
        ua = UserAgent()
        page = browser.new_page(user_agent=ua.random)
        
        page.goto("https://www.whatismybrowser.com/pt/detect/what-is-my-user-agent/")
        sleep(5)
        # lista = page.query_selector_all('//div/h3/a')
        # nova_lista = [i.get_attribute('href') for i in lista ]
        # titulos = list()
        # for i in nova_lista:
        #     page.goto(i)
        
        #     page.evaluate('window.scrollTo(0,4200)')
        #     titulos.append(page.title())
        # return titulos
        
          
        
resultado = Parallel(n_jobs=-1)(delayed(calcular)(arquivo) for arquivo in range(10))
print(resultado)
print(f"Demorou:{time.time() - tempo_inicial}")


