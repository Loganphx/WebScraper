import requests
from bs4 import BeautifulSoup
import requests  # required for HTTP requests: pip install requests
from bs4 import \
    BeautifulSoup  # required for HTML and XML parsing                                                              # required for HTML and XML parsing: pip install beautifulsoup4
import pandas as pd  # required for getting the data in dataframes : pip install pandas
import time  # to time the requests
from multiprocessing import Process, Queue, Pool
import threading
import sys


def test(searcKey):
    URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    jobResults = soup.find(id='ResultsContainer')

    jobElements = jobResults.find_all('section', class_='card-content')
    python_jobs = jobResults.find_all('h2', string=lambda text: 'software' in text.lower())
    print(len(python_jobs))
    for job_elem in jobElements:
        # Each job_elem is a new BeautifulSoup object.
        # You can use the same methods on it as you did before.
        # python_jobs = jobResults.find_all('h2', string='Python Developer')
        title_elem = job_elem.find('h2', class_='title')
        company_elem = job_elem.find('div', class_='company')
        location_elem = job_elem.find('div', class_='location')
        if None in (title_elem, company_elem, location_elem):
            continue


def indeed(searchKey):
    URL = 'https://www.indeed.com/jobs?q='+ searchKey + '&l=Austin%2C%20TX&vjk=adedb006cb583d30'
    pageResponse = requests.get(URL)

    soup = BeautifulSoup(pageResponse.content, 'html.parser')
    jobResults = soup.find(id='resultsCol')
    jobElements = jobResults.find_all('div', class_='jobsearch-SerpJobCard')
    jobDict = []
    for jobElement in jobElements:
        title = jobElement.find('h2', class_='title')

        jobDict.append((title.find('a', class_='jobtitle').text).strip('\n'))
    print(jobDict)

def amazon(searchKey):
    URL = 'https://www.amazon.com/s?k=' + searchKey
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64;     x64; rv:66.0) Gecko/20100101 Firefox/66.0",
               "Accept-Encoding": "gzip, deflate",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
               "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    pageResponse = requests.get(URL, headers=headers)

    soup = BeautifulSoup(pageResponse.content, 'html.parser')
    searchResults = soup.find(id='search')
    for d in soup.findAll('div', class_='sg-col-4-of-12 sg-col-8-of-16 sg-col-16-of-24 sg-col-12-of-20 sg-col-24-of-32 sg-col sg-col-28-of-36 sg-col-20-of-28'):
        name = d.find('span', class_='a-size-medium a-color-base a-text-normal')
        print(name.text)

indeed('art')
indeed('programming')
indeed('gaming')
