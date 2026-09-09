import datetime

class Player:
    def __init__(self, fname,lname, birth_year):
        self.fname = fname
        self.lname = lname
        self.birth_year = birth_year

    def get_age(self):
        now=datetime.datetime.now()
        return now.year-self.birth_year


# class TennisPlayer(Player):  #classname(Parent Class)
#     pass #it has accss of its parent class constructor

#now if we want a constructor of child class for the thing we have already in parent class we need use super keyword

class TennisPlayer(Player):
    def __init__(self, fname, lname, birth_year):
        super().__init__(fname,lname,birth_year)
        self.aces=[]

    def add_ace(self,ace):
        self.aces.append(ace)

    def avg_ace(self):
        return sum(self.aces)/len(self.aces)

class CricketPlayer(Player):
    def __init__(self, fname, lname, birth_year):
        super().__init(fname,lname,birth_year)
        self.scores=[]

    def add_scores(self,scores):
        self.scores.append(scores)

    def avg_scores(self):
        return sum(self.scores)/len(self.scores)

roger=TennisPlayer("roger","federer",1985)
print(roger.fname)


