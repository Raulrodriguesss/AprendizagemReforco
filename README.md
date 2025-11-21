Descrição do Projeto

Este projeto implementa uma simulação baseada em agentes para modelar o comportamento de macacos que aprendem a associar sinais (alarmes) a diferentes predadores.
A atividade faz parte do curso de Sistemas de Informação e envolve conceitos de modelagem computacional, inteligência distribuída e simulação de ambientes complexos.

A simulação ocorre em um ambiente 2D (matriz 50×50), no qual macacos e predadores se movimentam e interagem. A cada interação, os macacos atualizam seus pesos associados a sinais e predadores, modelando um processo de aprendizagem social.

 Arquitetura do Projeto

O projeto foi organizado em múltiplos arquivos Python, cada um representando uma entidade ou papel específico no sistema.


├── macaco.py ------- # Classe Macaco (agente principal)


├── predador.py ------- # Classe Predador


├── ambiente.py ------- # Classe Ambiente (controle da simulação)


├── utils.py ------- # Funções auxiliares (opcional)


├── main.py ------- # Arquivo principal que executa a simulação


└── README.md  ------- # Documentação do projeto

--- Classe Macaco ---  

Responsável por representar o agente que aprende.

Atributos principais

x, y → posição do macaco na matriz

pesos[s][p] → pesos associando símbolos a predadores

raio_predador → distância máxima para perceber um predador

raio_alarme → distância para ouvir um alarme

Métodos principais

mover() → deslocamento aleatório

perceber_predador() → identifica predadores próximos

emitir_alarme() → escolhe o sinal com maior peso

ouvir_alarme() → atualiza pesos (aprendizagem)

aprender() → regra de atualização dos pesos

---Classe Predador ---

Representa os predadores no ambiente.

Atributos

x, y → posição

id → identificador do tipo de predador

Métodos

mover() (opcional, dependendo do modelo)

--- Classe Ambiente 

Coordena toda a simulação.

Responsabilidades

Criar a matriz 50×50

Inicializar macacos e predadores

Controlar o loop de iterações

Atualizar movimentos

Gerenciar interações (detectar, emitir e ouvir alarmes)

Coletar dados para gráficos

 Arquivo Principal (main.py)

Responsável pela execução do programa.

Funções típicas

carregar parâmetros (quantidade de macacos, predadores, iterações etc.)

instanciar o ambiente

iniciar o loop de simulação

gerar gráficos e relatórios

Execução:

python main.py

Resultados Esperados

A simulação deve produzir:

--- Gráficos ---

Evolução dos pesos ao longo das iterações

Comparação sinal × predador

Aprendizado por macaco e por predador

--- Visualizações ---

Estado da matriz em momentos importantes

Movimentação dos agentes

Emissão de alarmes

--- Tecnologias Utilizadas ---

Python 3

Random (movimento aleatório)

Matplotlib (gráficos)

NumPy (opcional)

 --- Objetivo Acadêmico ---

Este trabalho reforça conhecimentos de:

Modelagem baseada em agentes

Simulação computacional

Programação orientada a objetos

Análise de comportamento emergente

Estruturação modular de código
