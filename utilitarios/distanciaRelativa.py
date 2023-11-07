from utilitarios.calculos import distancia

def distanciaRelativa(robo_x, robo_y, pontoFinal):
    arrayDist = []
    for x in range(len(robo_x)):
        dist = distancia(robo_x[x], robo_y[x], pontoFinal.x, pontoFinal.y)
        arrayDist.append(dist)
    return arrayDist