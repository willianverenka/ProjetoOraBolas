import matplotlib.pyplot as plt

def gerarGraficoVelocidadeTempoBola(bola_vx, bola_vy):
    print("tamanho:", len(bola_vx), len(bola_vy))
    t = 0
    tempo_bola = []
    while(t < 0.02 * len(bola_vx) - 0.02):
        tempo_bola.append(t)
        t+=0.02
    plt.plot(tempo_bola, bola_vx, color='blue', marker='o', label='Bola Vx(t)')
    plt.plot(tempo_bola, bola_vy, color='red', marker='o', label='Bola Vy(t)')
    plt.xlabel('t (segundos)')
    plt.ylabel('Velocidade (metros/segundo)')
    plt.title('Velocidade da bola em função do tempo')
    plt.legend()
    salvar = "imagensGeradas/velocidadeTempoBola.png"
    plt.savefig(salvar)
    plt.show()
    plt.close()
    return

def gerarGraficoVelocidadeTempoRobo(robo_vx, robo_vy):
    t = 0
    tempo_bola = []
    while(t < 0.02* len(robo_vx)):
        tempo_bola.append(t)
        t+=0.02
    plt.plot(tempo_bola, robo_vx, color='blue', marker='o', label='Robo Vx(t)')
    plt.plot(tempo_bola, robo_vy, color='red', marker='o', label='Robo Vy(t)')
    plt.xlabel('t (segundos)')
    plt.ylabel('Velocidade (metros/segundo)')
    plt.title('Velocidade do Robô em função do tempo')
    plt.legend()
    salvar = "imagensGeradas/velocidadeTempoRobo.png"
    plt.savefig(salvar)
    plt.show()
    plt.close()
    return