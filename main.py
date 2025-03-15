from planet import Planet
from human import Human
from threading import Thread
from structures import Structures
import time
import os
import sys


class Menu:
    planets = []
    
    def __init__(self):
        os.system('cls')
        self.game_is_running = True
        self.start_human_food_consumption()
        self.main()

    def set_cursor_position(self, row, col):
        sys.stdout.write(f"\033[{row};{col}H")
        sys.stdout.flush()

    def update_line(self,line, text):
        sys.stdout.write(f"\033[{line};0H{text}\033[K")
        sys.stdout.flush()

    def show_planets(self):
        self.update_line(1, "=" * 100)
        self.update_line(2, "Deine Planeten")
        self.update_line(3, "=" * 100)
        
        if not self.planets:
            self.update_line(4, "Es sind noch keine Planeten vorhanden!")
            self.set_cursor_position(len(self.planets) + 13, 0)
        else:
            for index, planet in enumerate(self.planets):
                self.update_line(
                    index + 4,
                    f"Planet:{planet.name}, Bevölkerung:{len(planet.inhabitants)}, Nahrung:\033[31m{planet.food}\033[0m, Holz:{planet.wood}, Stein:{planet.stone}, Gold:{planet.gold}"
                    )
                self.update_line(len(self.planets) + 4, "-" * 100)
        self.set_cursor_position(len(self.planets) + 13, 0)
        
    def start_human_food_consumption(self):
        def update_food():
            while self.game_is_running:
                self.show_planets()
                for planet in self.planets:
                    planet.population_consume()     
                time.sleep(1)
        Thread(target=update_food, daemon=True).start()

    def choose_planet(self):
        os.system('cls')
        if len(self.planets) > 0:
            self.update_line(len(self.planets) + 6, "Bitte wähle einen Planeten aus: \n" )
            for index, planet in enumerate(self.planets):
                print(f"{index}:{planet.name}")     
            try:    
                self.set_cursor_position(len(self.planets) + 7, 0)
                choice = int(input())
                choosen_planet = self.planets[choice]
                return choosen_planet
            except (ValueError, IndexError):
                print("Fehler bei der Planeten auswahl")
                self.choose_planet()
        else:
            print("Es sind noch keine Planeten vorhanden!")
            time.sleep(2)
            self.main()

    def create_planet(self):
        self.update_line(len(self.planets) + 12, "Wie soll der neue Planet heißen ?")
        self.set_cursor_position(len(self.planets) + 14, 0)
        new_planet_name = input()
        new_planet = Planet(new_planet_name)
        self.planets.append(new_planet)
        self.update_line(len(self.planets) + 14, f"Der Planet {new_planet.name} wurde erfolgreich erstellt")
        self.main()

    def create_human(self):
        try: 
            choosen_planet = self.choose_planet()
        except: 
            print("Es ist ein Fehler aufgetreten!")
            self.create_human()
        if choosen_planet.check_planet_population():
            self.update_line(len(self.planets) + 9,f"Planet {choosen_planet.name} ausgewählt")
            self.update_line(len(self.planets) + 10,f"Wie soll der Mensch heißen ?")
            self.set_cursor_position(len(self.planets) +11, 0)
            human_name = input()
            self.set_cursor_position(len(self.planets) +11, 0)
            self.update_line(len(self.planets) + 10,f"Wie alt ist der Mensch ?")
            self.set_cursor_position(len(self.planets) +13, 0)
            human_age = input()
            self.set_cursor_position(len(self.planets) +14, 0)
            self.update_line(len(self.planets) + 10,f"Welchen Beruf soll der Mensch haben?")
            self.set_cursor_position(len(self.planets) +15, 0)
            human_occupation = input()
            new_human = Human(human_name, human_age, human_occupation)
            choosen_planet.add_human(new_human, new_human.generation_costs)
            time.sleep(3)
            self.main()
        else:
            print(f"Der Planet {choosen_planet.name} hat die Maximale Bevölkerung erreicht!")
            time.sleep(3)
            self.main()
            
    def build_structure(self):
        os.system('cls')
        choosen_planet = self.choose_planet()
        self.update_line(len(self.planets) + 6, f"Wähle ein Gebäude für den Planeten {choosen_planet.name} aus, welches du bauen möchtest:\n")
        available_structures = Structures.get_available_structures()
        for index, structure in enumerate(available_structures):
            print(f"{index}:{structure["name"]} Kosten: Holz:{structure["wood_costs"]} Stein:{structure["stone_costs"]} Gold:{structure["gold_costs"]}")
        try: 
            self.set_cursor_position(len(self.planets) + len(available_structures) + 9, 0)
            choice = int(input())
            choosen_planet.add_building(available_structures[choice])
            time.sleep(3)
            self.main()
        except (ValueError, IndexError):
            print("Fehler bei der Auswahl des Gebäudes!")
            time.sleep(2)
            self.build_structure()
            
    def main(self):
        os.system("cls")
        menu_start_line = len(self.planets) + 6
        while self.game_is_running:
            self.update_line(menu_start_line, "1: Neuen Planet erstellen")
            self.update_line(menu_start_line + 1, "2: Neuen Menschen erschaffen")
            self.update_line(menu_start_line + 2, "3: Gebäude bauen")
            self.update_line(menu_start_line + 3, "4: Programm beenden")
            self.update_line(menu_start_line + 4, "Bitte wähle eine Option aus:")
            self.set_cursor_position(menu_start_line + 12, 0)
            try:
                choice = int(input())
                if choice == 1:
                    self.create_planet()
                    break
                elif choice == 2:
                    self.create_human()
                    break
                elif choice == 3:
                    self.build_structure()
                    break
                elif choice == 4:
                    self.update_line(menu_start_line + 6, "Programm beendet")
                    self.game_is_running = False
            except ValueError:
                self.update_line(menu_start_line + 6, "Ungültige Eingabe!")
                time.sleep(2)


if __name__ == "__main__":
    Menu()


