from dataclasses import dataclass

class Team:
    def __init__(self):
        pass

class Match:
    def __init__(self, match_content: dict):
        self.home_team = match_content["home_team"]
        self.away_team = match_content["away_team"]
        self.score = match_content["score"]
        self.venue = match_content["venue"]
        self.date_time = match_content["date_time"]
        self.id = match_content["id"]
        self.attendance = match_content["attendance"]
        self.winner = ""
        
        if self.away_team != "Bye":
            self.winner = self.calculate_winner()

    def calculate_winner(self):
        home_score = int(self.score["FT"].split(" - ")[0].split(".")[2])
        away_score = int(self.score["FT"].split(" - ")[1].split(".")[2])
        
        if home_score > away_score:
            return self.home_team
        elif home_score < away_score:
            return self.away_team
        else:
            return
    
    def __str__(self):
        if self.away_team == "Bye":
            return f"[Bye] {self.home_team}"
        else:
            return f"{self.home_team} ({self.score['FT'].split(' - ')[0]}) {'def.' if self.winner == self.home_team else 'def by.' if self.winner == self.away_team else 'tied.'} {self.away_team} ({self.score['FT'].split(' - ')[1]}) @ {self.venue}"


class TeamInMatch:
    @dataclass(frozen=True)
    class TeamStats:
        pass

    def __init__(self):
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
        
        for match in round_content:
            self.matches.append(Match(match))

    def __str__(self):
        output = f"{self.name}\n\n"

        for match in self.matches:
            output = output + str(match) + "\n"

        return output




class RoundLadder:
    def __init__(self):
        pass   