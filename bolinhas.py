import random as ra
import pygame as pyg
from pygame import *
from time import *
import sys

class bolinha():
  def __init__(self, coords = [0,0], vel = [0, 0]) -> None:
    self.coords = coords
    self.status = [0, 0]
    self.vel = vel
  
def move(bolinha, Vx, Vy):
  #Vx
  if bolinha.coords[0] < 1200 and bolinha.status[0] == 0:
    bolinha.coords[0] += Vx
  elif bolinha.status[0] == 0:
    bolinha.status[0] = 1
  elif bolinha.coords[0] > 0 and bolinha.status[0] == 1:
    bolinha.coords[0] -= Vx
  elif bolinha.status[0] == 1:
    bolinha.status[0] = 0
  #Vy
  if bolinha.coords[1] < 0:
    bolinha.coords[1] = 550
  if bolinha.coords[1] < 600 and bolinha.status[1] == 0:
    bolinha.coords[1] += Vy
  elif bolinha.status[1] == 0:
    bolinha.status[1] = 1
  elif bolinha.coords[1] > 0 and bolinha.status[1] == 1:
    bolinha.coords[1] -= Vy
  elif bolinha.status[1] == 1:
    bolinha.status[1] = 0
  
def vel_(bolinha, max, min):
  if bolinha.vel[1] <= max:
      if bolinha.vel[1] == max:
        bolinha.vel[1] = -min
      bolinha.vel[1] +=1


def main ():
  Preto = (0, 0, 0)
  Branco = (255, 255, 255)
  Vermelho = (255, 0, 0)
  Verde = (0, 255, 0)
  Amarelo = (255, 215, 0)
  Azul = (0, 0, 255)
  Azul_ceu = (173, 216, 230)
  cores = [Preto, Branco, Vermelho, Verde, Amarelo, Azul, Azul_ceu]
  pyg.init()
  mopos = []
  win = pyg.display.set_mode((1200, 600))
  display.set_caption('Bolinhas', 'None')
  win_open = True
  win.fill(Azul_ceu)
  Vx = 15
  Vy = -10
  cont = 0
  bolinhas = []
  bolinhas2 = []
  maxi = 10
  mini = -9
  while win_open:
    pyg.time.delay(80)
    win.fill(Azul_ceu)
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
          win.fill(Azul_ceu)
        if event.key == K_c:
          win.fill(Azul_ceu)
        if event.key == K_a:
          for bol in bolinhas:
            bolinhas.pop(0)
          for bol in bolinhas2:
            bolinhas2.pop(0)
      if event.type == MOUSEBUTTONDOWN:
        #1 - left click
        #2 - middle click
        #3 - right click
        #4 - scroll up
        #5 - scroll down
        mopos = mouse.get_pos()
        joao = list(mopos)
        
        if event.button == 3:
          print(mopos)
          if len(bolinhas) < 7:
            bolinhas.append(bolinha(joao, [Vx, Vy]))
          elif len(bolinhas2) < 7:
            bolinhas2.append(bolinha(joao, [Vx, Vy]))
          else:
            pass
          Vx += 2
          Vy += 1
          maxi += 1
          mini += 1
        if event.button == 4:
          for bol in bolinhas:
            if (bolinhas[cont].coords[1] - 20) > 15:
              bolinhas[cont].coords[1] = bolinhas[cont].coords[1] - 20
            cont += 1
          cont = 0
          for bol in bolinhas2:
            if (bolinhas2[cont].coords[1] - 20) > 15:
              bolinhas2[cont].coords[1] = bolinhas2[cont].coords[1] - 20
            cont += 1
        cont = 0
        if event.button == 5:
          for bol in bolinhas:
            if (bolinhas[cont].coords[1] + 20) < 590:
              bolinhas[cont].coords[1] = bolinhas[cont].coords[1] + 20
            cont += 1
          cont = 0
          for bol in bolinhas2:
            if (bolinhas2[cont].coords[1] + 20) < 590:
              bolinhas2[cont].coords[1] = bolinhas2[cont].coords[1] + 20
            cont += 1
        cont = 0
    for bol in bolinhas:
      pyg.draw.circle(win, cores[cont], bolinhas[cont].coords, 9)
      move(bolinhas[cont], bolinhas[cont].vel[0], bolinhas[cont].vel[1])
      vel_(bolinhas[cont], maxi, mini)
      cont += 1
    cont = 0
    for bol in bolinhas2:
      pyg.draw.circle(win, cores[cont], bolinhas2[cont].coords, 9)
      move(bolinhas2[cont], bolinhas2[cont].vel[0], bolinhas2[cont].vel[1])
      vel_(bolinhas2[cont], maxi, mini)
      cont += 1
    cont = 0
    pyg.display.update()

if __name__ == "__main__":
  main()
