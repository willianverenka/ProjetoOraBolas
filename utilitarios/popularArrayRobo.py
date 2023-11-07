from models.ponto import Ponto
from utilitarios.calculos import coeficienteAngular
import math


def calcular_velocidade(ponto_inicial, ponto_final, tempo_total, aceleracao, velocidade_max):
    velocidade_x = []
    velocidade_y = []
    sinalX = 1 if ponto_final.x > ponto_inicial.x else -1
    sinalY = 1 if ponto_final.y > ponto_inicial.y else -1
    angulo = math.atan2((ponto_final.y - ponto_inicial.y), (ponto_final.x - ponto_inicial.x))
    tempo = 0
    while(tempo <= tempo_total):
        if tempo <= 1:
            velocidade = aceleracao * tempo
            vx = velocidade * math.cos(angulo) * sinalX
            vy = velocidade * math.sin(angulo) * sinalY
        else:
            velocidade = velocidade_max
            vx = velocidade * math.cos(angulo) * sinalX
            vy = velocidade * math.sin(angulo) * sinalY
        velocidade_x.append(vx)
        velocidade_y.append(vy)
        tempo += 0.02
    return velocidade_x, velocidade_y