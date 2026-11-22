class Player:
    def __init__(self, name, health, kills):
        self.name = name
        self.health = health
        self.kills = kills

    def __str__(self):
        return f"{self.name}: {self.health}"

    def get_kills(self):
        return self.kills
    
    def get_health(self):
            return self.health


player1 = Player("Kinda", 100, 5)
player2 = Player("Eric", 80, 3)
player3 = Player("Yasmin", 90, 6)
player4 = Player("Zahraa", 92,7)

print(player1)
print(player2)
print(player1.get_kills())

print(player4.get_kills())
print(player3.get_health())

print(player2)