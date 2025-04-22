import utilities
from classes import *

class Controller:  
    def __init__(self):
        self.rounds = []
        self.team_registry = {}
        self._match_cache = {}
    
    def build(self, year: int):
        regular_season = utilities.Scraper.scrape_season(year)
        
        for round in regular_season:
            round_struct = utilities.RoundParser.parse(round)
            
            if not self.team_registry:
                
                for match in round_struct[1:]:
                    self.team_registry[match["home_team"]] = Team(match["home_team"])
                    if match["away_team"] != "Bye":
                        self.team_registry[match["away_team"]] = Team(match["away_team"])            

            self.rounds.append(Round(round_struct))
        
        self.fill_team_registry()
        

    def fill_team_registry(self):
        
        for round in self.rounds:
            for match in round.matches:
                
                if match.is_bye:
                    self.team_registry[match.home_team_name].add_match(round.name, 0)
                
                else:
                    self.team_registry[match.home_team_name].add_match(round.name, match.id)
                    self.team_registry[match.away_team_name].add_match(round.name, match.id)

                  

if __name__ == "__main__":
    controller = Controller()
    controller.build(2024)