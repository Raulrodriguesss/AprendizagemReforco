from macaco import Macaco
from predador import Predador
import random

def main():
    LIMITE = 50               # tamanho do ambiente
    NUM_MACACOS = 5
    NUM_PREDADORES = 2
    TURNOS = 50               # número de iterações
    
    # ----- Criar predadores -----
    predadores = []
    for i in range(NUM_PREDADORES):
        x = random.uniform(0, LIMITE)
        y = random.uniform(0, LIMITE)
        predadores.append(Predador(id_predador=i, x=x, y=y))

    # ----- Criar macacos -----
    # pesos[sinal][id_predador]
    sinais = ["grito", "latido", "chiado"]

    macacos = []
    for _ in range(NUM_MACACOS):
        pesos = {
            sinal: {p.id: random.uniform(0, 1) for p in predadores}
            for sinal in sinais
        }
        x = random.uniform(0, LIMITE)
        y = random.uniform(0, LIMITE)
        macacos.append(
            Macaco(x, y, pesos, raio_predador=5, raio_alarme=10)
        )

    # ----- Loop da simulação -----
    for t in range(TURNOS):
        print(f"\n=== TURNO {t} ===")
        
        # 1) Mover predadores
        for p in predadores:
            p.mover(limite=LIMITE)

        # 2) Mover macacos
        for m in macacos:
            m.mover(limite=LIMITE)

        # 3) Verificar percepções e alarmes
        for m in macacos:
            if m.perceber_predador(predadores):
                # pega o predador mais perto para escolher sinal
                predador_proximo = min(
                    predadores,
                    key=lambda p: ((m.x - p.x)**2 + (m.y - p.y)**2)
                )
                sinal = m.emitir_alarme(predador_proximo)
                print(f"Macaco em ({m.x:.1f},{m.y:.1f}) emitiu sinal:", sinal)

                # outros macacos aprendem
                for outro in macacos:
                    if outro is not m:
                        outro.ouvir_alarme(sinal, predador_proximo.id)

if __name__ == "__main__":
    main()
