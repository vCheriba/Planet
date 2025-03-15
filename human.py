

class Human:

    generation_costs = {
        "food_costs" : 100,
        "wood_costs" : 0,
        "stone_costs" : 0,
        "gold_costs" : 0,
    }

    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation


    def __str__(self):
        return f"Name:{self.name} Alter:{self.alter} Beruf:{self.occupation}"
    
