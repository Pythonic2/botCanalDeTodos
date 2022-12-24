from django.shortcuts import render,redirect
from django.views.generic import ListView
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
   

    return render(request,'index.html')



