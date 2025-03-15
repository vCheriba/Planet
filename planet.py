import random

class Planet:

    city_hall = False
    max_inhabitants = 20

    def __init__(self, name):
        self.name = name
        self.population = 0
        self.inhabitants = []
        self.food = random.randint(300, 2000)
        self.wood = random.randint(1500,2000)
        self.stone = random.randint(1500,2000)
        self.gold = 200

    def check_planet_population(self):
        if self.population < self.max_inhabitants:
            return True
        else:
            return False
        
    def check_resources(self, structure):
        if (
            self.food > structure["food_costs"] and 
            self.wood > structure["wood_costs"] and
            self.stone > structure["stone_costs"] and
            self.gold > structure["gold_costs"]
            ):
            return True
        else:
            return False

    def calculate_human_generation_resources(self, generation_costs):
        if  (self.food >= generation_costs["food_costs"] and
             self.wood >= generation_costs["wood_costs"] and 
             self.stone >= generation_costs["stone_costs"] and
             self.gold >= generation_costs["gold_costs"]):

            self.food -= generation_costs["food_costs"]
            self.wood -= generation_costs["wood_costs"]
            self.stone -= generation_costs["stone_costs"]
            self.gold -= generation_costs["gold_costs"]
            return True
        else:
            return False

    def calculate_structure_resources(self, structure):
        self.food -= structure["food_costs"]
        self.wood -= structure["wood_costs"]
        self.stone -= structure["stone_costs"]
        self.gold -= structure["gold_costs"]

    def add_building(self, structure):
        if not self.city_hall and structure["name"] != "Rathaus":
            print("Du musst erst ein Rathaus bauen!")
        elif not self.city_hall and structure["name"] == "Rathaus":
            if self.check_resources(structure):
                self.city_hall = True
                self.calculate_structure_resources(structure)
                print("Dein Rathaus wurde erfolgreich errichtet")

    def add_human(self, human, generation_costs):
        if self.city_hall and self.calculate_human_generation_resources(generation_costs):
            self.inhabitants.append(human)
            self.population += 1
            print(f"Der neue Mensch {human.name} wurde dem Planeten {self.name} hinzugefügt")
        else:
            print("Es ist noch kein Rathaus vorhanden")

    def population_consume(self):
        consumption = self.population * 3
        if self.food >= consumption:
            self.food -= consumption
        else:
            print(f"WARNUNG: Nicht genug Nahrung auf {self.name}")
            self.food = max(0, self.food)

    def show_status(self):
        print(f"Planet:{self.name} Bevölkerung:{self.population} Nahrung:{self.food} Holz:{self.wood} Stein:{self.stone} Gold:{self.gold}")



    def __str__(self):
        return f"{self.name}: Bevölkerung:{self.population} Nahrung:{self.food} Holz:{self.wood} Stein:{self.stone} Gold:{self.gold}"
    

erde = Planet("Erde")
print(erde)