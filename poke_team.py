from pokemon import *
import random
from typing import List
from data_structures.stack_adt import ArrayStack as AS


class PokeTeam:
    random.seed(20)
    TEAM_LIMIT = 6
    POKE_LIST = get_all_pokemon_types()

    def __init__(self):
        self.length = 0
        self.team = AR[self.TEAM_LIMIT]
        self.order = AR[self.TEAM_LIMIT]
        self.reset_order()
        
        
    def choose_manually(self):
        if self.length < 6:
            for i in range(0,len(self.POKE_LIST)):
                print(f"{i}: {self.POKE_LIST[i]}")
            choice = input("Choose your pokemon:\n")
            self.team[len(self.TEAM)] = self.POKE_LIST[int(choice)]()
            self.length += 1
            return
        else:
            print("team is already full")
            return

    def choose_randomly(self) -> None:
        choice = random.randint(0,len(self.POKE_LIST))
        if self.length < 6:
            self.team[len(self.TEAM)] = self.POKE_LIST[int(choice)]()
            self.length += 1
        return

    def regenerate_team(self, battle_mode, criterion=None) -> None:
        for i in range(len(self)):
            self.team[i].set_hp(self.team[i].get_health())

    def sort(self, criterion, order):
        values = AR(len(self))
        self.reset_order()
        for i in range(len(self)):
            pokemon = self.team[i]
            if criterion == "health":
                values[i] = pokemon.get_hp()
            elif criterion == "speed":
                values[i] = pokemon.get_speed()
            elif criterion == "attack":
                values[i] = pokemon.get_battle_power()
            elif criterion == "level":
                values[i] = pokemon.get_level()
            elif criterion == "defence":
                values[i] = pokemon.get_defence()
        #values list create, now sort list
        operations = None
        while operations != 0:
            operations = 0
            #bubble sorting values in ascending order, but also changes self.order the same way its sorted
            for i in range(len(self)-1):
                if values[i] > values[i+1]:
                    hold = values[i+1]
                    values[i+1] = values[i]
                    values[i] = hold
                    self.order[i] = i+1
                    self.order[i+1] = i
                    operations += 1
        #using a stack to reverse self.order if the parameter is descending
        if order == "descending":
            reverser = AS(len(self))
            for i in range(len(self)):
                reverser.push(self.order[i])
            for i in range(len(self)):
                self.order[i] = reverser.pop()


    def get_order(self):
        return self.order
    
    def reset_order(self):
        for i in range(self.TEAM_LIMIT):
            self.order[i] = i

    def special():
        pass


    def __getitem__(self, index: int):
        if index in range(len(self)):
            return self.team[index]

    def __len__(self):
        return self.length

    def __str__(self):
        out = ""
        for i in self.team:
            out += self.team[i] + "\n"
        return out

class Trainer:
    
    def __init__(self, name) -> None:
        self.name = name
        self.team = PokeTeam()
        self.pokedex = BSet()

    def pick_team(self, method: str) -> None:
        if method == "Manual":
            self.team.choose_manually()
        elif method == "Random":
            self.team.choose_randomly()
        self.team.regenerate_team()

    def get_team(self) -> PokeTeam:
        return self.team

    def get_name(self) -> str:
        return self.name

    def register_pokemon(self, pokemon: Pokemon) -> None:
        index = PokeType[str(pokemon.poketype)] + 1
        self.pokedex.add(index)

    def get_pokedex_completion(self) -> float:
        return round(len(self.pokedex)/len(PokeType),2)

    def __str__(self) -> str:
        out = ""
        completion = self.get_pokedex_completion()
        out += f"Trainer: {self.name}\n"
        out += f"Pokedex: {completion}"
        return out

if __name__ == '__main__':
    t = Trainer('Ash')
    print(t)
    t.pick_team("Random")
    print(t)
    print(t.get_team())
