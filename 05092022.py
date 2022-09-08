from enum import Enum

class TypePokemon(Enum):
    Agua = 0
    Fuego = 1
    Planta = 2
    Electrico = 3

class Pokemon():
    def __init__(self, name, ataque, defence, type):
        self.name = name
        self.type = type
        self.ataque = ataque
        self.defence = defence

    def __str__(self) -> str:
        return f'<Pokemon> {self.name} tipo => {self.type.name}'

def calculateDamage(atacante: Pokemon, defensor: Pokemon):
    tEficiencia = [
        [0.5, 2, 0.5, 1],
        [2, 0.5, 2, 1],
        [0.5, 2, 1, 0.5],
        [1, 1, 0.5, 1]
    ]
    efectividad = tEficiencia[atacante.type.value][defensor.type.value]
    damage = 50 * (atacante.ataque / defensor.defence) * efectividad
    return damage
    
pikachu = Pokemon("Pikachu", type=TypePokemon(3), ataque=100, defence=100)
charizard = Pokemon("Charizard", type=TypePokemon(1), ataque=100, defence=100)

print(calculateDamage(pikachu, charizard))

# https://twitter.com/MoureDev/status/1566780488307589123