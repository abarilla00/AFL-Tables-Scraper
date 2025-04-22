from dataclasses import dataclass

class Team:
    def __init__(self, name: str):
        self.name = name
        self.matches = {}

    def add_match(self, round_name: str, id: int):
        """
        Adds a match's id to a team's list of played matches for easy access
        """
        self.matches[round_name] = id
        

class Match:
    def __init__(self, match_content: dict):
        self.home_team_name = match_content["home_team"]
        self.away_team_name = match_content["away_team"]
              
        self.score = match_content["score"]
        self.venue = match_content["venue"]
        self.date_time = match_content["date_time"]
        self.id = match_content["id"]
        self.attendance = match_content["attendance"]

        self.is_bye = True if self.away_team_name == "Bye" else False
        self.winner = self.calculate_winner() if not self.is_bye else ""   

    def calculate_winner(self):
        """
        Calculates the winner of a given match using the stored score variable
        """

        #Cleaning stored score data
        home_score = int(self.score["FT"].split(" - ")[0].split(".")[2])
        away_score = int(self.score["FT"].split(" - ")[1].split(".")[2])
        
        if home_score > away_score:
            return self.home_team_name
        elif home_score < away_score:
            return self.away_team_name
        else:
            return
    
    def __str__(self):
        """
        Overriding the default string representation of this object to return match content cleanly
        """
        if self.is_bye:
            return f"[Bye] {self.home_team_name}"
        else:
            return f"{self.home_team_name} ({self.score['FT'].split(' - ')[0]}) {'def.' if self.winner == self.home_team_name else 'def by.' if self.winner == self.away_team_name else 'tied.'} {self.away_team_name} ({self.score['FT'].split(' - ')[1]}) @ {self.venue}"


class TeamInMatch:

    def __init__(self, team: Team, id: int):
        self.team = team
        self.id = id
        self.stats = ""

    def build(self):
        pass
    @dataclass(frozen=True)
    class TeamStats:
        pass

class Round:
    def __init__(self, round_content: list):
        self.name = round_content[0]['round_name']
        self.attendance = round_content[0]['attendance']
        self.avg_attendance = round_content[0]['average_attendance']
        self.matches = []

        self.build(round_content[1:])
        print(self)
    
    def build(self, round_content: list):
        """
        Builds the round's match list
        """
        
        for match in round_content:
            self.matches.append(Match(match))

    def __str__(self):
        """
        Overriding the default string representation of this object to return a round's content cleanly
        """
        output = f"{self.name}\n\n"

        for match in self.matches:
            output = output + str(match) + "\n"

        return output




class RoundLadder:
    def __init__(self):
        pass   