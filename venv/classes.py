class Player:

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

player_one = Player("Messi", 34)
print(player_one.name)
print(player_one.age)
