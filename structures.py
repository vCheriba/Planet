

class Structures:

    available_structures = [
        {
            "name": "Rathaus",
            "food_costs": 50,
            "stone_costs": 1200,
            "wood_costs": 1200,
            "gold_costs": 80,
        },
        {
            "name": "Jagdhütte",
            "food_costs": 10,
            "stone_costs": 10,
            "wood_costs": 200,
            "gold_costs": 30,
        },
        {
            "name": "Bauernhof",
            "food_costs": 20,
            "stone_costs": 400,
            "wood_costs": 1200,
            "gold_costs": 50,
        },
        {
            "name": "Holzfällerhütte",
            "food_costs": 10,
            "stone_costs": 100,
            "wood_costs": 300,
            "gold_costs": 25,
        },
        {
            "name": "Steinbruch",
            "food_costs": 15,
            "stone_costs": 100,
            "wood_costs": 1200,
            "gold_costs": 25,
        },
        {
            "name": "Goldmine",
            "food_costs": 40,
            "stone_costs": 1500,
            "wood_costs": 1500,
            "gold_costs": 30,
        }
    ]


    def __init__(self, name, wood_costs, stone_costs, gold_costs):
        self.name = name
        self.wood_costs = wood_costs
        self.stone_costs = stone_costs
        self.gold_costs = gold_costs
        self.built = False


    @staticmethod
    def get_available_structures():
        return Structures.available_structures


    def build(self, planet):
        pass