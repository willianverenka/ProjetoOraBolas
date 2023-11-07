def modularArrayBola(bola_x, bola_y, pontoInicial, pontoFinal):
    novoX = []
    novoY = []
    XPositivo = pontoFinal.x > pontoInicial.x
    YPositivo = pontoFinal.y > pontoInicial.y
    if XPositivo:
        for ponto in bola_x:
            if ponto > pontoInicial and ponto < pontoFinal:
                novoX.append(ponto)
    else:
        for ponto in bola_x:
            if ponto > pontoFinal and ponto < pontoInicial:
                novoX.append(ponto)
    if YPositivo:
        for ponto in bola_y:
            if ponto > pontoInicial and ponto < pontoFinal:
                novoY.append(ponto)
    else:
        for ponto in bola_y:
            if ponto > pontoFinal and ponto < pontoInicial:
                novoY.append(ponto)
    return novoX, novoY