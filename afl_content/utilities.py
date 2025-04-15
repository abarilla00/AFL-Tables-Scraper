from bs4 import BeautifulSoup
import requests
from itertools import zip_longest
from urllib.parse import urljoin
from dataclasses import dataclass
from abc import ABC, abstractmethod

#Global Variable
BASE_URL = 'https://afltables.com/afl/'

def grouper(iterable, n = 2, fillvalue=None):
    """
    Groups items in an iterable into chunks of size n (2 by deefault)
    """

    args = [iter(iterable)] * n
    return list(zip_longest(*args, fillvalue=fillvalue))
   
class Scraper:
    """
    Static class that can scrape HTML from AFL Tables web pages.
    """

    @staticmethod
    def _url(content_url):
        """
        Returns the AFL Tables URL for the desired content page
        """
        return urljoin(BASE_URL, content_url)
    
    @classmethod
    def scrape_season(cls, year: int) -> list:
        """
        Scrapes web pages designated as a season
        """

        url =  cls._url(f'seas/{year}.html')
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

        return regular_season

    @classmethod
    def scrape_match (cls, year:int, match: str):
        """
        Scrapes web pages designated as a match
        """
        
        url =  cls._url(f'stats/games/{year}/{match}.html')
        html = requests.get(url).text
        soup = BeautifulSoup(html)


class ParserInterface(ABC):

    @staticmethod
    @abstractmethod
    def parse(self, content: list) -> dict:
        pass

class RoundParser(ParserInterface):

    @staticmethod
    def parse(self, content: list) -> dict:
        pass

class MatchParser(ParserInterface):

    @staticmethod
    def parse(self, content: list) -> dict:
        pass 