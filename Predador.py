import random


class Predador: 
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
        self.x = 0
        self.y = 0
    
    def mover(self, limite=50):
        self.x += random.uniform(-1, 1)
        self.y += random.uniform(-1, 1)
        
        # Garantir que o predador permaneça dentro dos limites
        self.x = max(0, min(self.x, limite -1))
        self.y = max(0, min(self.y, limite -1))    
    