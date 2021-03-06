import pandas as pd
import numpy as numpy
import os
from bs4 import BeautifulSoup as bs
import requests
import re
import sys

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


def extract_data_from_url(url_values):
    for i in url_values:
        print(i)
        texts = requests.get(i)
        text_utf = texts.text.encode('utf-8')
        m, y, _ = re.findall(r'\d+', i)
        if not os.path.exists("Data/Html_Data/{}".format(y)):
            os.makedirs("Data/Html_Data/{}".format(y))
        with open("Data/Html_Data/{}/{}.html".format(y,m),"wb") as output:
            output.write(text_utf)


if __name__ == '__main__':
    url_values = generate_url()
    extract_data_from_url(url_values)