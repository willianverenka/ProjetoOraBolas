import matplotlib.pyplot as plt

def gerarGraficoAceleracaoTempoRobo(robo_ax, robo_ay):
    t = 0
    tempo_bola = []
    while(t < 0.02* len(robo_ax)):
        tempo_bola.append(t)
        t+=0.02
    plt.plot(tempo_bola, robo_ax, color='blue', marker='o', label='Robo Ax(t)')
    plt.plot(tempo_bola, robo_ay, color='red', marker='o', label='Robo Ay(t)')
    plt.xlabel('t (segundos)')
    plt.ylabel('Aceleração (metros/segundo²)')
    plt.title('Aceleração do Robô em função do tempo')
    plt.legend()
    salvar = "imagensGeradas/aceleracaoTempoRobo.png"
    plt.savefig(salvar)
    plt.show()
    plt.close()
    return

def gerarGraficoAceleracaoTempoBola(bola_ax, bola_ay):
    t = 0
    tempo_bola = []
    while(t < 0.02* len(bola_ax)-0.02):
        tempo_bola.append(t)
        t+=0.02
    plt.plot(tempo_bola, bola_ax, color='blue', marker='o', label='Bola Ax(t)')
    plt.plot(tempo_bola, bola_ay, color='red', marker='o', label='Bola Ay(t)')
    plt.xlabel('t (segundos)')
    plt.ylabel('Aceleração (metros/segundo²)')
    plt.title('Aceleração da bola em função do tempo')
    plt.legend()
    salvar = "imagensGeradas/aceleracaoTempoBola.png"
    plt.savefig(salvar)
    plt.close()
    return