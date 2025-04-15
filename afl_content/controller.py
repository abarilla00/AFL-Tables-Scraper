import utilities
import classes

class Controller:  
    def __init__(self):
        self.rounds = []
        self.team_registry = {}
        self._match_cache = {}
    
    def build(self):
        regular_season = utilities.Scraper.scrape_season(2024)
        print(regular_season)


if __name__ == "__main__":
    controller = Controller()
    controller.build()