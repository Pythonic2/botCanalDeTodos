import time
import os
import asyncio
from playwright.sync_api import sync_playwright
from joblib import Parallel, delayed
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from fake_useragent import UserAgent

tempo_inicial = time.time()





with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ua = UserAgent()
    page = browser.new_page()
        # page.locator('//div[@id="banner"]/a').click()
        # page.screenshot(path="foto.png")
    page.goto("https://www.canaldopovo.com/")
       