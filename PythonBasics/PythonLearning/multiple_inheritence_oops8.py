class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def get_details(self):
        return f"Name is {self.name} and salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod
    def alternative_constructor(cls, string, delim):
        # params = string.split(delim)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split(delim))

    @staticmethod
    def printstring(string):
        print("Your string was: " + string)


class Player:
    no_of_wins = 12

    def __init__(self, name, games):
        self.name = name
        self.games = games

    def get_details(self):
        return f"Name is {self.name} and game is {self.games}"
    
    def get_game(self):
        return self.games


class CoolProgrammer (Employee, Player): # Sequence of prent classes matters. The first one is more priority
    pass


sanjeev = CoolProgrammer("Sanjeev", 9, "Android Developer")
print(sanjeev.get_details())
print(sanjeev.get_game())
