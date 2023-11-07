def calcular_deslocamento(arrayVelocidadeX, arrayVelocidadeY, pontoInicial, pontoFinal):
    X = []
    Y = []
    sinalX = 1 if pontoFinal.x > pontoInicial.x else -1
    sinalY = 1 if pontoFinal.y > pontoInicial.y else -1
    aceleracaoConstanteX = (arrayVelocidadeX[1] - arrayVelocidadeX[0])/0.02
    deslocamentoAceleradoX =  aceleracaoConstanteX * 0.5 * 1**2
    aceleracaoConstanteY = (arrayVelocidadeY[1] - arrayVelocidadeY[0])/0.02
    deslocamentoAceleradoY = aceleracaoConstanteY * 0.5 * 1**2
    #print(aceleracaoConstanteY, aceleracaoConstanteX)
    for x in range(len(arrayVelocidadeX)-1):
        if x < 50: # ponto 50 -> 0,02 * 50 = 1s, divisao entre aceleracao constante e velocidade constante
            t = x * 0.02
            # eixo x
            aceleracaoX = (arrayVelocidadeX[x+1] - arrayVelocidadeX[x])/0.02
            deslocamentoX = 0.5 * aceleracaoX * t**2
            pontoX = pontoInicial.x + deslocamentoX * sinalX
            #eixo y
            aceleracaoY = (arrayVelocidadeY[x+1] - arrayVelocidadeY[x])/0.02
            deslocamentoY = 0.5 * aceleracaoY * t**2
            pontoY = pontoInicial.y + deslocamentoY * sinalY
        else:
            t = x * 0.02
            #eixo x
            deslocamentoX = arrayVelocidadeX[x] * (t - 1)
            deslocamentoX += deslocamentoAceleradoX
            pontoX = pontoInicial.x + deslocamentoX * sinalX
            #eixo y
            deslocamentoY = arrayVelocidadeY[x] * (t - 1)
            deslocamentoY += deslocamentoAceleradoY
            pontoY = pontoInicial.y + deslocamentoY * sinalY
        X.append(pontoX)
        Y.append(pontoY)
    return X, Y