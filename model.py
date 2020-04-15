import pandas as pd
import numpy as numpy
import os
from bs4 import BeautifulSoup
import requests


url = []
def generate_url():
    """
    this function is used to generate the url's into a list which in further functions is extracted. 
    """
    for i in range(2012, 2020):
        for j in range(1, 13):
            if j < 10:
                link = f'https://en.tutiempo.net/climate/0{j}-{i}/ws-432950.html'
                url.append(link)
            else:
                link = f'https://en.tutiempo.net/climate/{j}-{i}/ws-432950.html'
                url.append(link)
    return url


def extract_data_from_url():
    




url_values = generate_url()
extract_data_from_url(url_values)