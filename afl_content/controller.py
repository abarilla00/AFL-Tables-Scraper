import utilities
import classes
from bs4 import BeautifulSoup

class Controller:  
    def __init__(self):
        self.rounds = []
        self.team_registry = {}
        self._match_cache = {}
    
    def build(self):
        regular_season = utilities.Scraper.scrape_season(2024)
        
        #for round in regular_season:
         #   round_struct = utilities.RoundParser.parse(round)
         
        round_struct = utilities.RoundParser.parse(regular_season[0])
        print(round_struct)
        

if __name__ == "__main__":
    controller = Controller()
    controller.build()