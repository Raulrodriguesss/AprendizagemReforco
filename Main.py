from Macaco import Macaco
from Predador import Predador
import random

def main():
    LIMITE = 50
    NUM_MACACOS = 10
    NUM_PREDADORES = 10
    TURNOS = 50

    # ----- Criar predadores -----
    predadores = []
    for i in range(NUM_PREDADORES):
        p = Predador(nome=f"Predador{i}", especie="Tigre")
        p.x = random.uniform(0, LIMITE)
        p.y = random.uniform(0, LIMITE)
        predadores.append(p)

    # ----- Criar macacos -----
    sinais = ["grito", "chiado", "latido"]

    macacos = []
    for _ in range(NUM_MACACOS):
        # pesos[sinal][predador_nome]
        pesos = {
            sinal: {p.nome: random.uniform(0, 1) for p in predadores}
            for sinal in sinais
        }

        x = random.uniform(0, LIMITE)
        y = random.uniform(0, LIMITE)

        macaco = Macaco(
            x=x,
            y=y,
            pesos=pesos,
            raio_predador=5,
            raio_alarme=10
        )
        macacos.append(macaco)

    # ----- Loop da simulação -----
    for t in range(TURNOS):
        print(f"\n=== TURNO {t} ===")

        # mover predadores
        for p in predadores:
            p.mover(limite=LIMITE)

        # mover macacos
        for m in macacos:
            m.mover(limite=LIMITE)

        # detectar predadores e emitir alarmes
        for m in macacos:

            if m.perceber_predador(predadores):
                # pega o predador mais próximo
                predador_proximo = min(
                    predadores,
                    key=lambda p: (m.x - p.x)**2 + (m.y - p.y)**2
                )

                sinal = m.emitir_alarme(predador_proximo)

                print(
                    f"Macaco ({m.x:.1f},{m.y:.1f}) "
                    f"emitiu '{sinal}' para {predador_proximo.especie} "
                )

                # outros macacos aprendem
                for outro in macacos:
                    if outro is not m:
                        outro.ouvir_alarme(sinal, predador_proximo.nome)


if __name__ == "__main__":
    main()
