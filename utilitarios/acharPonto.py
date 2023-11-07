from utilitarios.calculos import distancia
from utilitarios.calculos import tempoDeslocamento
from models.robo import Robo

def acharPonto(arrayPontos : list, robo : Robo):
    if(robo.coordenada.x > 9 or robo.coordenada.x < 0 or robo.coordenada.y > 6 or robo.coordenada.y < 0):
        raise Exception(f"Ponto inicial do robô inválido ({robo.coordenada.x},{robo.coordenada.y})\n Intervalos validos: X [0,9]; Y [0,6]")
    for ponto in arrayPontos:
        distTotal = distancia(ponto.x, ponto.y, robo.coordenada.x, robo.coordenada.y)
        if ponto.t <= 1:
            tempo = tempoDeslocamento(distTotal, robo.aceleracao)
        else:
            dist_aceleracao = 0.5 * robo.aceleracao * (1**2)
            dist_constante = distTotal - dist_aceleracao
            tempo = 1 + dist_constante / robo.velocidade
        if tempo <= ponto.t:
            print(f"INTERCEPTOU no ponto ({ponto.x};{ponto.y}) {tempo} < {ponto.t}")
            print(f"distTotal {distTotal}")
            return ponto
    return -1 # não foi encontrado nenhum ponto possivel de interceptacao
