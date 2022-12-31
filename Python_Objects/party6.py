from party import PartyAnimal

class CricketFan(PartyAnimal):
   points = 0
   def six(self):
      self.points = self.points + 6
      self.party()
      print(self.name,"points",self.points)

class RugbyFan(PartyAnimal):
   points = 0
   def topscore(self):
      self.points += 21
      self.party()
      print(self.name,"points",self.points)

   ages = 0
   def age(self):
      self.ages += 26
      self.party()
      print(self.name,"age",self.ages)

s = PartyAnimal("Sally")
s.party()
j = CricketFan("Jim")
j.party()
j.six()
print(dir(j))
q = RugbyFan("Q")
q.party()
q.topscore()
q.age()
print(dir(q))
