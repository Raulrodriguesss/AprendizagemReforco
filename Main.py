from Macaco import Macaco
from Tigre import Tigre
from Aguia import Aguia
from Cobra import Cobra
import random
from graficos import (
    plotar_evolucao_pesos_macaco,
    plotar_evolucao_por_predador,
    plotar_pesos_finais,
    plotar_ambiente
)

def main():

    # === PESOS INICIAIS PARA CADA MACACO ===
    pesos_base = {
    "grito":  {"tigre": 3, "aguia": 1, "cobra": 1},
    "latido": {"tigre": 1, "aguia": 3, "cobra": 1},
    "chiado": {"tigre": 1, "aguia": 1, "cobra": 3}
}

    # === CRIAR MACACOS ===
    macacos = [
        Macaco(10, 20, {k: v.copy() for k, v in pesos_base.items()}, 12, 15),
        Macaco(25, 10, {k: v.copy() for k, v in pesos_base.items()}, 12, 15),
        Macaco(40, 35, {k: v.copy() for k, v in pesos_base.items()}, 12, 15),
        Macaco(30, 40, {k: v.copy() for k, v in pesos_base.items()}, 12, 15),
        Macaco(15, 30, {k: v.copy() for k, v in pesos_base.items()}, 12, 15),
        Macaco(10, 20, {k: v.copy() for k, v in pesos_base.items()}, 12, 15)
    ]

    # === CRIAR PREDADORES ===
    predadores = [
        Aguia(25, 25, 1),
        Cobra(45, 10, 2),
        Tigre(12, 25, 0),
        Aguia(10, 4, 1),
        Cobra(30, 25, 2),
        Aguia(25, 16, 4),
    ]

    historico_macacos = {i: [] for i in range(len(macacos))}
    # === LOOP DA SIMULAÇÃO ===
    for turno in range(1, 50):
        print(f"\n=== TURNO {turno} ===")

        for i, m in enumerate(macacos):
            m.registrar_estado(historico_macacos[i], turno)
        
        # mover predadores
        for p in predadores:
            p.mover()

        # mover macacos
        for m in macacos:
            m.mover()

        # cada macaco olha ao redor
        for m in macacos:
            predador_visto = m.perceber_predador(predadores)

            if predador_visto:
                # emite alarme
                sinal = m.emitir_alarme(predador_visto)
                print(f"Macaco ({m.x:.1f},{m.y:.1f}) emitiu '{sinal}' ao ver {predador_visto.especie}")

                # os outros macacos aprendem
                for outro in macacos:
                    if outro is not m:
                        # distância entre macacos
                        dist = ((m.x - outro.x)**2 + (m.y - outro.y)**2)**0.5
                        if dist <= outro.raio_alarme:
                            outro.ouvir_alarme(sinal, predador_visto.especie)
                            print(f" → Macaco em ({outro.x:.1f},{outro.y:.1f}) aprendeu sobre {predador_visto.especie} pelo sinal '{sinal}'")

    

    # === GRÁFICOS DOS MACACOS (primeiros 3 macacos) ===
    for i in range(3):
        plotar_evolucao_pesos_macaco(historico_macacos[i], i, f"macaco_{i}")

    # === GRÁFICOS POR PREDADOR ===
    for especie in ["tigre", "aguia", "cobra"]:
        plotar_evolucao_por_predador(historico_macacos, especie, f"predador_{especie}")

    # === GRÁFICOS FINAIS ===
    plotar_pesos_finais(historico_macacos, "pesos_finais")

    # === AMBIENTE FINAL ===
    plotar_ambiente(macacos, predadores, "ambiente_final.png")



if __name__ == "__main__":
    main()
