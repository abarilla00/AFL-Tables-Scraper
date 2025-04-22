from bs4 import BeautifulSoup
import requests
from itertools import zip_longest
from urllib.parse import urljoin
from abc import ABC, abstractmethod

#Global Variable
BASE_URL = 'https://afltables.com/afl/'

def grouper(iterable, n = 2, fillvalue=None):
    """
    Groups items in an iterable into chunks of size n (2 by default)
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

                #We want iterating to stop after the regular seeason has been iterated
                if table.text == "Finals":
                    break
                tables.append(table)

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
    """
    Interface for data parsers
    """

    @staticmethod
    @abstractmethod
    def parse(content: list) -> list[dict]:
        pass

class RoundParser(ParserInterface):
    """
    Class that implemented the ParserInterface
    """

    @staticmethod
    def parse(content: tuple) -> list[dict]:
        """
        Parser method for converting HTML soup into structured data for AFL season rounds
        """

        #Needs to work for rounds that haven't happened yet (i.e, future fixtures)

        header_content = content[0].find_all("td")

        #Adding the header content to the round_content list
        round_content = [dict(
                        round_name = header_content[0].text.split("*")[0].strip(),
                        attendance = header_content[1].text.split(" ")[2],
                        average_attendance = header_content[1].text.split(" ")[3].strip("()")
                        )]
        
        #Gets all matches in table (soup) form
        matches = content[1].find_all('table', attrs={'border': '1'})
    
        for match in matches:
            
            #Data to be pulled from tables
            match_dict = {
            'home_team': '',
            'away_team': '',
            'score': '',
            'venue': '',
            'date_time': '',
            'id': '',
            'attendance': ''
        }
            
            #Allows retrieval of a match's teamnames, venue, and unique id
            match_data = match.find_all("a")

            #indicates a team had the bye
            if len(match_data) == 1:
                match_dict['home_team'] = match_data[0].text
                match_dict['away_team'] = "Bye"
            
            #empty table (not a match)
            elif len(match_data) == 0:
                continue

            #Completed Match
            else:

                #Filling easily accessible data
                match_dict['home_team'] = match_data[0].text
                match_dict['away_team'] = match_data[2].text
                match_dict['venue'] = match_data[1].text
                match_dict['id'] = match_data[3].get('href').split("/")[4].split(".")[0]

                #Generating score data
                scores = match.find_all("tt")
                home_score = scores[0].text.strip().replace("\xa0", "").split(" ")
                away_score = scores[1].text.strip().replace("\xa0", "").split(" ")

                #Combines both scores into a single list for iteration
                both_team_scores = home_score + away_score
                
                #Creating quarter by quarter totals based on team scores at each break
                for i in range(len(both_team_scores)):
                    score = both_team_scores[i]
                    goals_behinds = score.split(".")
                    goals = int(goals_behinds[0])
                    behinds = int(goals_behinds[1])
                    total_score = (goals * 6) + behinds
                    score = score + "." + str(total_score)
                    both_team_scores[i] = score
                
                #Splits scores table into seperate team score tables
                home_score = both_team_scores[:4]
                away_score = both_team_scores[4:]

                score_dict = {
                    'QT': home_score[0] + " - " + away_score[0],
                    'HT': home_score[1] + " - " + away_score[1],
                    '3QT': home_score[2] + " - " + away_score[2],
                    'FT': home_score[3] + " - " + away_score[3],
                }

                match_dict['score'] = score_dict
            
            round_content.append(match_dict)

        return round_content

class MatchParser(ParserInterface):
    """
    Class that implemented the ParserInterface
    """


    @staticmethod
    def parse(content: list) -> list[dict]:
        """
        Parser method for converting HTML soup into structured data for AFL season matches
        """

        pass 