from dataclasses import dataclass


@dataclass(frozen=True)
class Player:
    name: str
    sign: str


if __name__ == '__main__':
    player1 = Player("Bunmi", "X")

    print(player1.name)
    print(player1.sign)
    