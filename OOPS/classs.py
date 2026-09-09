class CricketPlayer():
    team_size=11

    # Constructor
    # This method runs automatically when we create an object
    def __init__(self,fname,lname,age,team):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.team=team
        self.scores=[]

    # Normal method to add a new score to the scores list
    def add_score(self,score):
            self.scores.append(score)

    # Method to calculate the player's average score
    def get_avg(self):
        return sum(self.scores)/len(self.scores)

    # __str__() is a special method.
    # It is automatically called when we use print(object).
    # It tells Python what text should be displayed for the object.
    def __str__(self):
        return f"{self.fname},{self.lname},is {self.age} years old and he plays for team{self.team}"

    #operator overloading
    #its a less than operator form which we can compare objects of the classes
    def __lt__(self,other):
        self_avg=self.get_avg()
        other_avg=other.get_avg()
        return self_avg<other_avg

    #eqaul to operator just like less than
    def __eq__(self, other):
        return self.age==other.age

#calling object
dhoni=CricketPlayer("Mahendra SIngh","Dhoni",44,'India')
print(dhoni.fname)
print(dhoni) #__str__ function is called
dhoni.add_score(100)
dhoni.add_score(68)
dhoni.add_score(70)
print(dhoni.get_avg())

virat=CricketPlayer("Virat","Kohli",37,"India")
virat.add_score(34)
virat.add_score(95)
virat.add_score(69)

print(virat.get_avg())

print(virat<dhoni)#can we do thiis? yes we can do yhis by defining __lt__(less than) function in the class

print(virat==dhoni) #__eq__ method is called
