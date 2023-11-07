from models.ponto import Ponto

def carregar(arquivo: str):
    if(type(arquivo) != str):
        raise Exception("nome do arquivo invalido, deve ser uma string com o final .txt ou .dat")
    arrayPontos = []
    f = open(arquivo, "r")  
    c = 1 #contagem de linhas para indicar em que ponto o arquivo.txt falha
    for linha in f:
        array = linha.split('\t')
            # no formato da trajetoria, ha tres colunas separadas por um tab
        if len(array)!= 3:
            raise Exception("Erro ao carregar o arquivo: as colunas possuem diferentes tamanhos\nou algum dado esta faltando na linha %d" %c)
        for x in range(0, 3):
            array[x] = array[x].replace(",", ".")
        if c != 1: #ignora a primeira linha (cabecalho)
            x = float(array[1])
            y = float(array[2])
            if x <= 9 and y <= 6: # adiciona somente coordenadas validas em relacao as dimensoes do campo
                ponto = Ponto(float(x), float(y), float(array[0]))
                arrayPontos.append(ponto)
        c+=1
    return arrayPontos