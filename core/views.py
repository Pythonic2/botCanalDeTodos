from django.shortcuts import render,redirect
import time
from fake_useragent import UserAgent
from random import randint
from time import sleep
import asyncio
from playwright.async_api import async_playwright
import subprocess
subprocess.run(["playwright", "install", "chromium"])
# Create your views here.
vazia = list()

def relatorios(request):
    dados = {'fim': 'Processo Finalizado com Sucesso. Clique aqui para ver as matérias que foram acessadas',
             'mostrar': '', 'materias': vazia}
    return render(request,'relatorio.html',dados)

def home(request):
    v = request.POST.get("nome")
    s = request.POST.get("segundos")
    if v == None or v == '' and s ==None or s =='':
        pass
    else:
        valor = int(v)
        tempo_por_page = int(s)
        if request.method == 'POST':
            menu = ['Fé','Cotidiano','Início','Política','Brasil','Mundo','Tecnologia','Esportes','Entretenimento','Opinião']
           
            mostrar = {'mostrar':' '}
            async def main():
                async with async_playwright() as p:

                    browser = await p.chromium.launch(headless=True)
                    ua = UserAgent()
                    page = await browser.new_page(user_agent=ua.random)
                    page.set_default_timeout(0)
                    await page.goto("https://www.canaldopovo.com/")
                    print(await page.title())
                    lista = await page.query_selector_all("//div[contains(text(),'Últimas notícias')]/../div/div/h3/a")
                    nova_lista = [await i.get_attribute('href') for i in lista]
                    await page.close()
                    for r in range(valor):
                        for i in nova_lista:
                            page = await browser.new_page()
                            await page.goto(i, timeout=0)
                            sleep(randint(20, tempo_por_page))
                            vazia.append(await page.title())
                            print(await page.title())
                            
                            await page.locator(f"//div[contains(@class,'td-pb-span8')]//a/div[text()='{menu[randint(0,10)]}']").click()
                            sleep(5)
                            print(await page.title())
                            await page.close()
            asyncio.run(main())
            return render(request, 'index.html', mostrar)
    mostrar = {'mostrar':'d-none'}
    return render(request,'index.html',mostrar)

3