from utilitarios.acharPonto import acharPonto
from utilitarios.carregar import carregar
from models.ponto import Ponto
from models.robo import Robo
from graficos.trajetorias import gerarGraficoTrajetoria
from graficos.trajetoriasTempo import gerarGraficoTrajetoriasTempo
from graficos.distanciaRelativa import gerarGraficoDistanciaRelativa
from utilitarios.calculos import coeficienteAngular, distancia, media_pontos
from utilitarios.exportarRobo import exportarRobo
from utilitarios.distanciaRelativa import distanciaRelativa
from graficos.velocidadeTempo import gerarGraficoVelocidadeTempoRobo, gerarGraficoVelocidadeTempoBola
from graficos.aceleracaoTempo import gerarGraficoAceleracaoTempoBola, gerarGraficoAceleracaoTempoRobo
from utilitarios.popularArrayRobo import calcular_velocidade
from utilitarios.calcularDeslocamento import calcular_deslocamento

array = carregar("trajetoria_bola.txt") #carrega o arquivo da bola

# logica de interceptacao

ponto = Ponto(9, 6, 0)
robo = Robo(ponto, 2.8, 2.8, 0.09)
pontofinal = acharPonto(array, robo) # acha o ponto de interceptacao considerando as limitacoes
print(pontofinal.x, pontofinal.y)
if(pontofinal == -1):
    raise Exception("A bola não pode ser interceptada dentre os pontos válidos (campo 9x6 metros)") # impossivel, fecha programa
print(pontofinal.t, "eh o tempo", pontofinal.x, pontofinal.y)

robo_vx, robo_vy = calcular_velocidade(ponto, pontofinal, pontofinal.t, 2.8, 2.8)
robo_x, robo_y = calcular_deslocamento(robo_vx, robo_vy, ponto, pontofinal)
robo_ax, robo_ay = media_pontos(robo_vx, robo_vy)

bola_x = [ponto.x for ponto in array]
bola_y = [ponto.y for ponto in array]

bola_vx, bola_vy = media_pontos(bola_x, bola_y)
bola_ax, bola_ay = media_pontos(bola_vx, bola_vy)
robo_ax, robo_ay = media_pontos(robo_vx, robo_vy)

distRelativa = distanciaRelativa(robo_x, robo_y, pontofinal)
print(distRelativa[len(distRelativa)-1])

gerarGraficoTrajetoria(robo_x, robo_y, bola_x, bola_y, ponto, pontofinal)
gerarGraficoVelocidadeTempoRobo(robo_vx, robo_vy)
gerarGraficoVelocidadeTempoBola(bola_vx, bola_vy)
gerarGraficoAceleracaoTempoRobo(robo_ax, robo_ay)
gerarGraficoAceleracaoTempoBola(bola_ax, bola_ay)
gerarGraficoDistanciaRelativa(distRelativa)

exportarRobo(robo_x, robo_y)