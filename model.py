import pandas as pd
import numpy as numpy
import os
from bs4 import BeautifulSoup
import requests


url = []
def extract_data():
    for i in range(2012, 2020):
        for j in range(1, 13):
            if j < 10:
                link = f'https://en.tutiempo.net/climate/0{j}-{i}/ws-432950.html'
                url.append(link)
                # print(url)
            else:
                link = f'https://en.tutiempo.net/climate/{j}-{i}/ws-432950.html'
                url.append(link)
                # print(url)
    return url


url_values = extract_data()
print(url_values)