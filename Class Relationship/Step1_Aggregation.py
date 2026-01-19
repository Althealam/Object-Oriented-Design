# Aggregation is a “has-a” relationship where the whole references the part, but does NOT own the part’s lifecycle.

# Example 1: Classic Aggregation (Team&Developer)
# A Team has developers
# Developers exist independently
# Developers can move between teams
class Developer:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self, name, developers):
        self.name = name
        self.developers = developers
    
    def show_team(self):
        print(f"Team {self.name}")
        for dev in self.developers:
            print(dev.name)

dev1 = Developer("Alice")
dev2 = Developer("Bob")

team_a = Team("Platform", [dev1, dev2])
team_a.show_team()

# Example 2: Aggregation with Sharing (Professor & Department)
# Professors can belong to multiple departments
# Departments do not own professors

class Professor:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name):
        self.name = name
        self.professors = [] # Aggregation
    
    def add_professor(self, professor: Professor):
        self.professors.append(professor)

p1 = Professor("Dr. Smith")
cs = Department("cs")
math = Department("Math")

cs.add_professor(p1)
math.add_professor(p1)
# ✅ Same Professor instance is shared
# ✅ No department controls professor’s lifecycle
# ✅ Strong evidence of aggregation, not composition