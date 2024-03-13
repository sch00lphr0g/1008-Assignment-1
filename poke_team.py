from pokemon import *
import random
from typing import List

class PokeTeam:
    random.seed(20)
    TEAM_LIMIT = 6
    POKE_LIST = get_all_pokemon_types()


    def __init__(self):
        self.length = 0
        self.team = ArrayR[self.TEAM_LIMIT]
        self.referenceTeam = ArrayR[self.TEAM_LIMIT]

    def choose_manually(self):
        if self.length < 6:
            for i in range(0,len(self.POKE_LIST)):
                print(f"{i}: {self.POKE_LIST[i]}")
            choice = input("Choose your pokemon:\n")
            self.team[len(self.TEAM)] = self.POKE_LIST[choice]
            self.referenceTeam[len(self.TEAM)] = self.POKE_LIST[choice]
            self.length += 1
            return
        else:
            print("team is already full")
            return

    def choose_randomly(self) -> None:
        choice = random.randint(0,len(self.POKE_LIST))
        if self.length < 6:
            self.team[len(self.TEAM)] = self.POKE_LIST[choice]
            self.referenceTeam[len(self.TEAM)] = self.POKE_LIST[choice]
            self.length += 1

    def regenerate_team(self, battle_mode, criterion=None) -> None:
        for i in range(len(self)):
            self.team[i] = self.referenceTeam[i]
    
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
        raise NotImplementedError

    def pick_team(self, method: str) -> None:
        raise NotImplementedError

    def get_team(self) -> PokeTeam:
        raise NotImplementedError

    def get_name(self) -> str:
        raise NotImplementedError

    def register_pokemon(self, pokemon: Pokemon) -> None:
        raise NotImplementedError

    def get_pokedex_completion(self) -> float:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

if __name__ == '__main__':
    t = Trainer('Ash')
    print(t)
    t.pick_team("Random")
    print(t)
    print(t.get_team())