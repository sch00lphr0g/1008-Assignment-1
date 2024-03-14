from poke_team import Trainer, PokeTeam
from typing import Tuple
from battle_mode import BattleMode
from data_structures.queue_adt import CircularQueue as CQ
from data_structures.referential_array import ArrayR as AR
from data_structures.array_sorted_list import ArraySortedList as ASL


class Battle:

    def __init__(self, trainer_1: Trainer, trainer_2: Trainer, battle_mode: BattleMode, criterion = "health") -> None:
        self.trainers = (trainer_1, trainer_2)
        self.mode = battle_mode
        self.criterion = criterion

    def commence_battle(self) -> Trainer | None:
        return

    def _create_teams(self) -> Tuple[PokeTeam, PokeTeam]:
        teams = AR(2)
        if self.mode == BattleMode(0) | BattleMode(1):
            for i in range(2):
                team = self.trainers[i].get_team()
                queue = CQ(len(team))
                for j in team:
                    queue.append(j)
                teams[i] = queue
        elif self.mode == BattleMode(2):
            for i in range(2):
                team = self.trainers[i].get_team()
                
                sortedList = ASL(len(team))
                for j in team:
                    sortedList


        return (teams[0], teams[1])   
        

    def set_battle(self) -> PokeTeam | None:
        raise NotImplementedError

    def rotate_battle(self) -> PokeTeam | None:
        raise NotImplementedError

    def optimise_battle(self) -> PokeTeam | None:
        raise NotImplementedError


if __name__ == '__main__':
    t1 = Trainer('Ash')
    t1.pick_team("random")

    t2 = Trainer('Gary')
    t2.pick_team('random')
    b = Battle(t1, t2, BattleMode.ROTATE)
    winner = b.commence_battle()

    if winner is None:
        print("Its a draw")
    else:
        print(f"The winner is {winner.get_name()}")
