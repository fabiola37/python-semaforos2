import os
import random
import time
import threading

inicioPuente = 10
largoPuente = 20

cantVacas = 5

semaforoVaca = threading.Semaphore(1)

class Vaca(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.1, 0.9)

  def avanzar(self):
    time.sleep(1-self.velocidad)
    self.posicion += 1
    

  def dibujar(self):
    print(' ' * self.posicion + 'V') # si no funciona, cambiá por 'V' 

  def run(self):
    while(True):
      self.avanzar()
      while self.posicion == inicioPuente - 2:
        semaforoVaca.acquire()
        self.avanzar()
      while self.posicion == inicioPuente + largoPuente + 2:
        semaforoVaca.release() 
        self.avanzar()
      while self.posicion == 70:
          self.posicion = 0
 
vacas = []
for i in range(cantVacas):
  v = Vaca()
  vacas.append(v)
  v.start() # si la clase hereda de Thread, el .start() siempre corre run() de la clase.

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

class Puente():
    def __init__(self,inicioPuente,largoPuente,cantidadDePuentes):
        self.inicioPuente = inicioPuente
        self.largoPuente = largoPuente
        self.cantidadDePuentes = cantidadDePuentes

    def dibujarPuente(self):
        p1 = ''
        while self.cantidadDePuentes > 0:
            p1 = p1 + (' ' * 3 + '=' * self.largoPuente)
            self.cantidadDePuentes -= 1
        print (p1)

puente1 = Puente(10,20,3)

while(True):
  cls()
  print('Apretá Ctrl + C varias veces para salir...')
  print()
  puente1.dibujarPuente()
  for v in vacas:
    v.dibujar()
  puente1.dibujarPuente()
  time.sleep(0.2)