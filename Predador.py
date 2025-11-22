import random


class Predador: 
    def __init__(self, x, y, especie, id):
        self.x = x
        self.y = y
        self.especie = especie
        self.id = id
    
    def mover(self, limite=50):
        self.x += random.uniform(-1, 1)
        self.y += random.uniform(-1, 1)
        
        # Garantir que o predador permaneça dentro dos limites
        self.x = max(0, min(self.x, limite -1))
        self.y = max(0, min(self.y, limite -1))    
    