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

def calcular(arquivo):
    with sync_playwright() as p:
        print('Iniciando os Acessos...')
        browser = p.chromium.launch(headless=True)
        ua = UserAgent()
        page = browser.new_page(user_agent=ua.random)
        
        page.goto("https://www.canaldopovo.com/")
        lista = page.query_selector_all("//div[contains(text(),'Últimas notícias')]/../div/div/h3/a")
        nova_lista = [i.get_attribute('href') for i in lista ]
        titulos = list()
        for i in nova_lista:
            page = browser.new_page(user_agent=ua.random)
            page.goto(i)
            sleep(3)                        
            page.evaluate('window.scrollTo(0,600)')
            sleep(3)
            page.evaluate('window.scrollTo(0,600)')

            titulos.append(page.title())
          
            # try:
            #     banner = page.locator(f'//ins[contains(@data-revive-seq,"{randint(0,1)}")]/iframe')
            #     page.goto(banner.get_attribute('src'))
            #     page.evaluate('javascript:window.open(window.clickTag)')
            # except:
            #     pass

        print(len(titulos))
resultado = Parallel(n_jobs=-1)(delayed(calcular)(arquivo) for arquivo in range(1000))
print(resultado)
print(f"Demorou:{time.time() - tempo_inicial}")