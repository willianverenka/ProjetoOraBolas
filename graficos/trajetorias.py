import matplotlib.pyplot as plt

def gerarGraficoTrajetoria(robo_x, robo_y, bola_x, bola_y, pontoInicial, pontofinal):
    plt.plot(bola_x, bola_y, color='blue', marker='o', label='Trajetoria da bola')
    plt.plot(robo_x, robo_y, color='red', marker='o', label='Trajetoria do robo')
    plt.xlabel('X (metros)')
    plt.ylabel('Y (metros)')
    plt.title('Trajetorias até a interceptação')
    plt.legend()
    salvar = "imagensGeradas/trajetorias.png"
    plt.savefig(salvar)
    plt.close()