import random


class Macaco:
    def __init__(self, x, y, pesos,raio_predador, raio_alarme):
        self.x = x
        self.y = y
        self.pesos = pesos
        self.raio_predador = raio_predador
        self.raio_alarme = raio_alarme
        
        pass 
    
        
    def mover(self, limite=50):
        self.x += random.uniform(-1, 1)
        self.y += random.uniform(-1, 1)
        
        # Garantir que o macaco permaneça dentro dos limites
        self.x = max(0, min(self.x, limite -1))
        self.y = max(0, min(self.y, limite -1))

    def perceber_predador(self, predadores):
        for predador in predadores:
            distancia = ((self.x - predador.x) ** 2 + (self.y - predador.y) ** 2) ** 0.5
            if distancia <= self.raio_predador:
                return predador
        return None  
    
    def emitir_alarme(self, predador):
            # escolher o melhor sinal com maior peso para esse predador
            id_pred = predador.id
            melhor_sinal = max(self.pesos, key=lambda s: self.pesos[s][id_pred])
            return melhor_sinal
        
    def ouvir_alarme(self, sinal, predador_id):
        # aprendizagem: aumenta o peso daquele sinal para aquele predador
        self.pesos[sinal][predador_id] += 0.1