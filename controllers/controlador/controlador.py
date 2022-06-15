#tirar camera, sensores proximidade, renomear variáveis, mudar cores e tamanhos, velocidades diferentes nas rodas
# de acordo com os sensores.

from controller import Robot
import math
import socket
import struct
import sys

TIME_STEP = 20

      

class MeuRobot:
    def __init__(self, robo):   #inicializacao dos componentes do robo (sensores, rodas, etc) 
        self.robo = robo
        
        self.baixo_e = self.robo.getDevice("sensoresq")
        self.baixo_e.enable(TIME_STEP)
        
        self.baixo_d = self.robo.getDevice("sensordir")
        self.baixo_d.enable(TIME_STEP)
        
        self.rodas = []
        self.nomesRodas = ['rodafrontesq', 'rodafrontdir', 'rodatrasesq', 'rodatrasdir']
        for i in range(4):
            self.rodas.append(self.robo.getDevice(self.nomesRodas[i]))
            self.rodas[i].setPosition(float('inf'))
            self.rodas[i].setVelocity(0.0)
       
        #declaracao de variaveis a serem utilizadas     
        self.segundo = 0
        
        self.contador = 0
        self.dir = False
        self.esq = False
        
        self.velEsq = 0.0
        self.velDir = 0.0
        
class TI502(MeuRobot):   #classe do robo
    def run(self):        #metodo de controle do robo
        while self.robo.step(TIME_STEP) != -1:
            
            self.rodas[0].setVelocity(self.velEsq) #setta as velocidades atravez de variaveis que serao mudadas durante o codigo
            self.rodas[1].setVelocity(self.velDir)
            self.rodas[2].setVelocity(self.velEsq)
            self.rodas[3].setVelocity(self.velDir)	
            
            # estou na linha               
            self.velEsq = 12.5
            self.velDir = 12.5
            self.cor2_d = self.baixo_d.getValue()
            self.cor2_e = self.baixo_e.getValue()
            print("d", self.cor2_d)
            print("e", self.cor2_e)
            
            if self.cor2_d < 700:
                self.velEsq = 35
            
            if self.cor2_e < 700:
                self.velDir = 35
                
            if self.cor2_e > 940 and self.cor2_d > 940: 
                self.rodas[0].setVelocity(0) 
                self.rodas[1].setVelocity(0)
                self.rodas[2].setVelocity(0)
                self.rodas[3].setVelocity(0)
                break
                
        
            #if self.cor1_m != self.cor2_m: #verifica se a cor registrada antes eh a mesma de agora
                #if self.cor1_d != 0.0 and self.cor2_e == 0.0: #se a da direita for diferente e a esquerda for preta, vira para direita
                   # self.velEsq = -1.0
                   # self.velDir = 1.0
                   # self.cor1_m = self.cor2_m
                   # self.cor1_d = self.cor2_d
                #elif self.cor1_e != 0.0 and self.cor2_d == 0.0:  #se a da esquerda for diferente e a direita for preta, vira para esquerda
                   # self.velEsq = 1.0
                   # self.velDir = -1.0
                   # self.cor1_m = self.cor2_m
                   # self.cor1_e = self.cor2_e
             
robo = Robot() #cria o robo
robot_controler = TI502(robo) #instancia o robo
robot_controler.run() #roda o robo            
