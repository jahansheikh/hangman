# collin giometti - hangman

import pygame
import sys

black = (0,0,0)
background = (166,191,188)
button_light = (218,224,224)
button_dark = (193,199,199)

width = 800
height = 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

def get_word():
  import random
  lines = []
  f = open('words.txt', 'r')
  for x in f:
    x = x.strip('\n')
    lines.append(x)
  randnumber = random.randint(0,len(lines) - 1)
  lines.pop(len(lines) - 1)
  return lines[randnumber].upper()

def button(word,x,y,w,h,ic,ac,action=None):
  mouse = pygame.mouse.get_pos()
  click = pygame.mouse.get_pressed()
  
  if x+w > mouse[0] > x and y+h > mouse[1] > y:
    pygame.draw.rect(screen,ac,(x,y,w,h))
    if click[0] == 1 and action != None:
      action()
  else:
    pygame.draw.rect(screen,ic,(x,y,w,h))

  text = pygame.font.SysFont("Corbel",40)
  text_surface = text.render(word, True, black)
  text_rect = text_surface.get_rect()
  text_rect.center = ((x+(w/2)), (y+(h/2)))
  screen.blit(text_surface, text_rect)

def gamechoice():
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
    screen.fill(background)
    button("1 Player",(width/5),(height/2),200,50,button_light,button_dark,one_player)
    button("2 Player",((width/5)*3),(height/2),200,50,button_light,button_dark,two_player)
    pygame.display.update()
    clock.tick(20)

def one_player():
  hangman(get_word())

def two_player():
  word = ""
  def return_word():
    hangman(word)
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      elif event.type == pygame.KEYDOWN:
        if pygame.key.name(event.key) == "backspace":
          word = word.rstrip(word[-1])
        else:
          word += pygame.key.name(event.key)
    
    screen.fill(background)
    text = pygame.font.SysFont("Corbel",40)
    text_surface = text.render(word, True, black)
    text_rect = text_surface.get_rect()
    text_rect.center = ((width/2),(height/2))
    screen.blit(text_surface, text_rect)
    button("Start Game",((width/2)-100),((height/3)*2),200,50,button_light,button_dark,return_word)
    pygame.display.update()
    clock.tick(20)

def hangman(word):
  print(word)

pygame.init()
gamechoice()
