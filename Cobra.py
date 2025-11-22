from Predador import Predador

class Cobra(Predador):
    def __init__(self, x, y, id):
        super().__init__(x, y, "cobra", id)
