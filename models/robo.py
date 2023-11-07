from .ponto import Ponto

class Robo:
    def __init__(self, ponto:Ponto, velocidade:float, aceleracao:float, raio:float):
        self.coordenada = ponto
        self.velocidade = velocidade
        self.aceleracao = aceleracao
        self.raio = raio