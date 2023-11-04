from app.players.player import Player
from abc import ABC


class Dwarf(Player, ABC):
    def __init__(self, favourite_dish: str, nickname: str) -> None:
        super().__init__(nickname=nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        return print(f"{self.nickname} is eating {self._favourite_dish}")