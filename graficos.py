import matplotlib.pyplot as plt

# ============================================================
# 1. GRÁFICOS ITERAÇÕES × PESOS PARA ALGUNS MACACOS
# ============================================================

def plotar_evolucao_pesos_macaco(historico, id_macaco, filename):
    sinais = list(historico[0]["pesos"].keys())
    predadores = list(historico[0]["pesos"][sinais[0]].keys())

    for especie in predadores:
        plt.figure(figsize=(8,5))
        
        for sinal in sinais:
            x = [h["iteracao"] for h in historico]
            y = [h["pesos"][sinal][especie] for h in historico]
            plt.plot(x, y, label=sinal)

        plt.title(f"Macaco {id_macaco} — Evolução dos Pesos para predador '{especie}'")
        plt.xlabel("Iteração")
        plt.ylabel("Peso f")
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.savefig(f"{filename}_{especie}.png")
        plt.close()



# ============================================================
# 2. GRÁFICOS AGRUPADOS POR PREDADOR
# ============================================================

def plotar_evolucao_por_predador(historicos, predador, filename):
    plt.figure(figsize=(8,5))

    for id_macaco, hist in historicos.items():
        x = [h["iteracao"] for h in hist]
        y = [h["pesos"]["chiado"][predador] for h in hist]  # pode escolher outro sinal
        plt.plot(x, y, label=f"Macaco {id_macaco}")

    plt.title(f"Evolução do peso 'chiado' para predador '{predador}'")
    plt.xlabel("Iteração")
    plt.ylabel("Peso f")
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{filename}.png")
    plt.close()



# ============================================================
# 3. GRÁFICO FINAL DOS PESOS PARA CADA MACACO (estado final)
# ============================================================

def plotar_pesos_finais(historicos, filename):
    sinais = ["grito", "latido", "chiado"]
    predadores = ["tigre", "aguia", "cobra"]

    for especie in predadores:
        plt.figure(figsize=(8,5))

        for sinal in sinais:
            valores = [
                historicos[i][-1]["pesos"][sinal][especie]
                for i in historicos.keys()
            ]
            plt.plot(list(historicos.keys()), valores, marker="o", label=sinal)

        plt.title(f"Pesos finais para predador '{especie}'")
        plt.xlabel("ID do Macaco")
        plt.ylabel("Peso f")
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.savefig(f"{filename}_{especie}.png")
        plt.close()



# ============================================================
# 4. IMAGEM DO AMBIENTE (MACACOS E PREDADORES)
# ============================================================

def plotar_ambiente(macacos, predadores, filename):
    plt.figure(figsize=(6,6))

    # macacos
    xs = [m.x for m in macacos]
    ys = [m.y for m in macacos]
    plt.scatter(xs, ys, c="green", label="Macacos")

    # predadores
    px = [p.x for p in predadores]
    py = [p.y for p in predadores]
    plt.scatter(px, py, c="red", marker="X", s=100, label="Predadores")

    plt.title("Ambiente final dos agentes")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
