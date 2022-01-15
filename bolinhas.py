from operator import invert
import random as ra
import pygame as pyg
from pygame import *
from time import *
import sys

class bolinha():
  def __init__(self, coords) -> None:
    if coords[0] == 0:
      self.coords = [ra.randint(0, 1200), ra.randint(0, 600)]
    else:
      self.coords = coords
    self.status = [0, 0]
  
def min_list(list):
  cont = 0
  mini = list[0]
  for i in list:
    if list[cont] < mini:
      mini = list[cont]
    cont += 1
  return mini

def transform_list(list):
  x1 = []
  y1 = []
  newcon = [x1, y1]
  x_min = list[0] -10
  x_max = list[0] +10
  y_min = list[1] -10
  y_max = list[1] +10
  temp = x_min
  cont = 0
  for i in range(x_max - x_min):
    x1.append(temp)
    temp += 1
    cont += 1
  cont = 0
  temp = y_min
  for i in range(y_max - y_min):
    y1.append(temp)
    temp += 1
    cont += 1
  return newcon

def chinese_interseccion(list1, list2):
  x = min_list(list1)
  for i in range(20):
    if x in list1 and x in list2:
      print("it is true")
      x = x +1
      return True
  return False
  

def colision_report(conj_a, conj_b):
  list1 = transform_list([conj_a[0], conj_b[0]])
  list2 = transform_list([conj_a[1], conj_b[1]])
  if chinese_interseccion(list1, list2):
    print("Hello guys")
    return True
  return False

def move(coords, status, vel):
  if coords[0] < 1200 and status[0] == 0:
    coords[0] += vel
  elif status[0] == 0:
    status[0] = 1
  if coords[1] < 600 and status[1] == 0:
    coords[1] += vel
  elif status[1] == 0:
    status[1] = 1
  if status[1] == 1 and coords[1] > 0:
    coords[1] -= vel
  elif status[1] == 1:
    status[1] = 2
  if status[0] == 1 and coords[0] > 0:
    coords[0] -= vel
  elif status[0] == 1:
    status[0] = 2
  if status[0] == 2 and coords[0] < 1200:
    coords[0] += vel
  elif status[0] == 2:
    status[0] = 1
  if status[1] == 2 and coords[1] < 600:
    coords[1] += vel
  elif status[1] == 2:
    status[1] = 1
  return [coords[0], coords[1], status[0], status[1]]

def inv_move(coords, status, vel):
  if status[1] == 0 and coords[1] > 0:
    coords[1] -= vel
  elif status[1] == 0:
    status[1] = 1
  if status[0] == 0 and coords[0] > 0:
    coords[0] -= vel
  elif status[0] == 0:
    status[0] = 1
  if coords[0] < 1200 and status[0] == 1:
    coords[0] += vel
  elif status[0] == 1:
    status[0] = 2
  if coords[1] < 600 and status[1] == 1:
    coords[1] += vel
  elif status[1] == 1:
    status[1] = 2
  if coords[0] > 0 and status[0] == 2:
    coords[0] -= vel
  elif status[0] == 2:
    status[0] = 1
  if coords[1] > 0 and status[1] == 2:
    coords[1] -= vel
  elif status[1] == 2:
    status[1] = 1
  return [coords[0], coords[1], status[0], status[1]]

def ajeitador(coords, status, modo, vel):
  if modo:
    tudojunto = inv_move(coords, status, vel)
    coords[0] = tudojunto[0]
    coords[1] = tudojunto[1]
    status[0] = tudojunto[2]
    status[1] = tudojunto[3]
  else:
    tudojunto = move(coords, status, vel)
    coords[0] = tudojunto[0]
    coords[1] = tudojunto[1]
    status[0] = tudojunto[2]
    status[1] = tudojunto[3]

def c_handler(bola1, bola2):
  if colision_report(bola1.coords, bola2.coords):
    if bola1.status[0] == 0:
      bola1.status[0] = 1
    if bola1.status[1] == 0:
      bola1.status[0] = 1
    if bola1.status[0] == 1:
      bola1.status[0] = 2
    if bola1.status[1] == 1:
      bola1.status[0] = 2
    if bola2.status[0] == 0:
      bola2.status[0] = 1
    if bola2.status[1] == 0:
      bola2.status[0] = 1
    if bola2.status[1] == 1:
      bola2.status[0] = 2
    if bola2.status[1] == 1:
      bola2.status[0] = 2
    
Preto = (0, 0, 0)
Branco = (255, 255, 255)
Vermelho = (255, 0, 0)
Amarelo = (255, 215, 0)
Azul = (0, 0, 255)
Azul_ceu = (173, 216, 230)
pyg.init()
win = pyg.display.set_mode((1200, 600))
display.set_caption('Bolinhas', 'None')
win_open = True
#tudojunto = [0, 0, 0, 0] coords = [100, 100] status = [0, 0]
bol1 = bolinha([100, 120])
bol2 = bolinha([60, 80])
bol3 = bolinha([0, 0])
while win_open:
  pyg.time.delay(50)  
  #win.fill(Azul_ceu)
  for event in pyg.event.get():
    if event.type == QUIT:
      win_open = False
      pyg.quit()
      sys.exit()
    if event.type == KEYDOWN:
      if event.key == K_ESCAPE:
        win_open = False
      if event.key == K_f:
        win = pyg.display.set_mode((0, 0), pyg.FULLSCREEN)
  pyg.draw.circle(win, Vermelho, bol2.coords, 5)
  pyg.draw.circle(win, Amarelo, bol1.coords, 5)
  pyg.draw.circle(win, Azul, bol3.coords, 5)
  ajeitador(bol1.coords, bol1.status, 1, 10)
  ajeitador(bol2.coords, bol2.status, 0, 10)
  ajeitador(bol3.coords, bol3.status, 1, 10)
  c_handler(bol1, bol2)
  c_handler(bol1, bol3)
  c_handler(bol2, bol3)
  pyg.display.update()