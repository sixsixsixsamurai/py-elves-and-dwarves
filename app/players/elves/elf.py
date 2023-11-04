from app.players.player import Player
from abc import ABC


class Elf(Player, ABC):
    def __init__(self, musical_instrument: str, nickname: str) -> None:
        super().__init__(nickname=nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        return print(f"{self.nickname}"
                     f" is playing a song on the {self._musical_instrument}")