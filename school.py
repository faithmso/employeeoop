class School():
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def getName(self):
    return self.name

  def getLevel(self):
    return self.level

  def getNumberOfStudents(self):
    return self.numberOfStudents

  def setNumberOfStudents(self, newNumberOfStudents):
    self.numberOfStudents = newNumberOfStudents

  def __repr__(self):
    return "A {}school named {} with {} students".format(self.level, self.name, self.numberOfStudents)


a = School("Codecademy", "high", 100)
print(a)
print(a.getName())
print(a.getLevel())
a.setNumberOfStudents(200)
print(a.getNumberOfStudents())

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    self.pickupPolicy = pickupPolicy
    super().__init__(name, "Primary", numberOfStudents)

  def getPickupPolicy(self):
      return self.pickupPolicy

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + "The pickup Policy is {}".format(self.pickupPolicy)


b = PrimarySchool("Codeacademy", 300, "Pickup Allowed")
print(b.getPickupPolicy())
print(b)

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, "High", numberOfStudents)
    self.sportsTeams = sportsTeams

  def getSportsTeams(self):
    return self.sportsTeams

  def __repr__(self):
    parentrepr = super().__repr__()
    return parentrepr + "The sports Teams are {}".format(",".join(self.sportsTeams))


c = HighSchool("Codeacademy High",500, ["Tennis", "Basketball"])

print(c.getSportsTeams())
print(c)