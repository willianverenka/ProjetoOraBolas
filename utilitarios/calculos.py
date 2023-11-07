from math import sqrt
from models.robo import Robo

def distancia(x1 : float, y1 : float, x2 : float, y2 : float):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def tempoDeslocamento(dist : float, a : float):
    return sqrt((2*(dist))/a) 

def tempoDeslocamentoConstante(dist, vo): # s = s0 + v0t -> t = (s - s0)/v0
    return (dist)/vo

def coeficienteAngular(x1:float, y1:float, x2:float, y2:float):
    return (y2-y1)/(x2-x1)

def calcularY(coeficienteAngular, pontoInicialRobo):
    """
    Calcular o valor de y para um x especifico dado dois pontos (uma reta).
    Funciona a partir da equação da reta y = mx + b
    """
    y = coeficienteAngular * pontoInicialRobo.x + pontoInicialRobo.y
    return y

def equacao(x1, y1, x2, y2):
    m=((y2-y1)/(x2-x1))
    b=y1-(m*x1)
    return m, b

def velocidadeMedia(a, b, intervalo):
    return abs(b - a)/intervalo

def intervaloOtimo(intervalo : float, qtdPontos : int):
    return intervalo/(qtdPontos-1)

def deslocamento(tempo, aceleracao, v0):
    return v0 * tempo + 1/2 * aceleracao * tempo**2

def media_pontos(arrayX, arrayY):
    arrayNovaX = []
    arrayNovaY = []
    for x in range(len(arrayX)-1):
        itemY = (arrayY[x+1] - arrayY[x])/0.02
        itemX = (arrayX[x+1] - arrayX[x])/0.02
        arrayNovaX.append(abs(itemX))
        arrayNovaY.append(abs(itemY))
    return arrayNovaX, arrayNovaY