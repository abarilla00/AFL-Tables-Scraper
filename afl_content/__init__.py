from bs4 import BeautifulSoup
import requests
from itertools import zip_longest
from urllib.parse import urljoin
from dataclasses import dataclass

#Global Variable
BASE_URL = 'https://afltables.com/afl/'

def grouper(iterable, n = 2, fillvalue=None):
    """
    Groups items in an iterable into chunks of size n (2 by deefault)
    """

    args = [iter(iterable)] * n
    return list(zip_longest(*args, fillvalue=fillvalue))


class Team:
    def __init__(self):
        pass

class Match:
    def __init__(self):
        pass

class TeamInMatch:
    @dataclass(frozen=True)
    class TeamStats:
        pass

    def __init__(self):
        pass

class Round:
    def __init__(self):
        pass

class Ladder:
    def __init__(self):
        pass

        
class Scraper:
    """
    Static class that can scrape HTML from AFL Tables web pages.
    """

    @staticmethod
    def url(content_url):
        """
        Returns the AFL Tables URL for the desired content page
        """
        return urljoin(BASE_URL, content_url)
    
    @classmethod
    def scrape_season(cls, year: int):
        """
        Scrapes web pages designated as a season
        """

        url =  cls.url(f'seas/{year}.html')
        html = requests.get(url).text
        soup = BeautifulSoup(html)


        tables = []

        # Iterates over the page HTML and stores relevant tables in a variable.
        for table in soup.select('center > table'):
            if table.get('class') != ['sortable']:
                tables.append(table)

            #We want iterating to stop after the regular seeason has been iterated
            if table.text == "Finals":
                break

        regular_season = grouper(tables)

        print(regular_season)

    @classmethod
    def scrape_match (cls, year:int, match: str):
        """
        Scrapes web pages designated as a match
        """
        
        url =  cls.url(f'stats/games/{year}/{match}.html')
        html = requests.get(url).text
        soup = BeautifulSoup(html)

