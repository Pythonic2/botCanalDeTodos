from django.shortcuts import render,redirect
from datetime import datetime
# Create your views here.
from time import sleep
import time
import os
import asyncio
from playwright.sync_api import sync_playwright
from joblib import Parallel, delayed
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from fake_useragent import UserAgent
from random import randint
import subprocess
tempo_inicial = time.time()
subprocess.run(["playwright", "install", "chromium"])

def home(request): 
    v = request.POST.get("nome")
    if v == None or v == '':
        pass
    else:
        valor = int(v)
        if request.method == 'POST':
    
            def calcular(arquivo):
                with sync_playwright() as p:
                    
                    browser = p.chromium.launch(headless=True,chromium_sandbox=False)
                    ua = UserAgent()
                    page = browser.new_page(user_agent=ua.random)
                    
                    page.goto("https://www.canaldopovo.com/")
                    
                    lista = page.query_selector_all("//div[contains(text(),'Últimas notícias')]/../div/div/h3/a")
                    nova_lista = [i.get_attribute('href') for i in lista ]
                    
                    for i in nova_lista:    
                        print('Abrindo mais uma aba')
                        page.evaluate(f"window.open('{i}', '_blank')")
                        sleep(4)                        
                        

                        
                      
                        # try:
                        #     banner = page.locator(f'//ins[contains(@data-revive-seq,"{randint(0,1)}")]/iframe')
                        #     page.goto(banner.get_attribute('src'))
                        #     page.evaluate('javascript:window.open(window.clickTag)')
                        # except:
                        #     pass

                  
            resultado = Parallel(n_jobs=2)(delayed(calcular)(arquivo) for arquivo in range(valor))
            print(f"Demorou:{time.time() - tempo_inicial}")

    return render(request,'index.html')





