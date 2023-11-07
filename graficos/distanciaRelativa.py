import matplotlib.pyplot as plt
from utilitarios.calculos import coeficienteAngular
from utilitarios.calculos import calcularY
from utilitarios.calculos import equacao
from utilitarios.calculos import distancia

def gerarGraficoDistanciaRelativa(arrayDist):
    tempo = []
    t = 0
    while(t < 0.02* len(arrayDist)):
        tempo.append(t)
        t+=0.02
    plt.plot(tempo, arrayDist, color='purple', marker='o', label='D(t)')
    plt.xlabel('Tempo (segundos)')
    plt.ylabel('Distância (metros)')
    plt.title('Distância relativa entre o robô e a interceptação')
    plt.legend()
    salvar = "imagensGeradas/distanciaRelativa.png"
    plt.savefig(salvar)
    plt.close()