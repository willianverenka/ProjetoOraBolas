import matplotlib.pyplot as plt
from utilitarios.calculos import intervaloOtimo

def gerarGraficoTrajetoriasTempo(arrayBola, pontoInicial, pontoFinal, arrayRobo_x, arrayRobo_y):
    # *if* filtra os pontos, apenas os pontos anteriores
    # a interceptacao sao contados no grafico
    if pontoInicial.x >= pontoFinal.x: #sentido anti horario, direita p/esquerda
        bola_x = [ponto.x for ponto in arrayBola if ponto.x >= pontoFinal.x and ponto.x <= pontoInicial.x]
        bola_y = [ponto.y for ponto in arrayBola if ponto.x >= pontoFinal.x and ponto.x <= pontoInicial.x]
        bola_x.reverse()
        bola_y.reverse()
    else:
        bola_x = [ponto.x for ponto in arrayBola if ponto.x <= pontoFinal.x and ponto.x >= pontoInicial.x]
        bola_y = [ponto.y for ponto in arrayBola if ponto.x <= pontoFinal.x and ponto.x >= pontoInicial.x]
    tempo_bola = []
    intervalo = intervaloOtimo(pontoFinal.t, len(bola_x))
    t = 0
    for x in range(len(bola_x)):
        t += intervalo
        tempo_bola.append(t)    
    plt.plot(tempo_bola, bola_x, color='blue', marker='o', label='Bola X(t)')
    plt.plot(tempo_bola, bola_y, color='red', marker='o', label='Bola Y(t)')
    plt.plot(tempo_bola, arrayRobo_x, color='green', marker='o', label='Robo X(t)')
    plt.plot(tempo_bola, arrayRobo_y, color='yellow', marker='o', label='Robo Y(t)')
    plt.xlabel('t (segundos)')
    plt.ylabel('ponto no eixo (metros)')
    plt.title('Trajetorias em função do tempo até a interceptação')
    plt.legend()
    salvar = "imagensGeradas/trajetoriasTempo.png"
    plt.savefig(salvar)
    plt.show()
    plt.close()