import pygame
from sys import exit
from random import choice

class Button():
  def __init__(self, rect, colour):
    self.rect = pygame.Rect(rect)
    self.on_colour = colour
    self.off_colour = (colour[0]*0.5, colour[1]*0.5, colour[2]*0.5)
    self.colour = self.off_colour

def makename(name, c, fontname, colour):
  name = fontname.render(name, True, colour)
  name_rect = name.get_rect(center = c)
  screen.blit(name, name_rect)

pygame.init()
screen = pygame.display.set_mode((500, 400))
clock = pygame.time.Clock()
pygame.display.set_caption("Memory game")

butfonts = pygame.font.Font("anton.ttf", 18)
butfontm = pygame.font.Font("anton.ttf", 21)
butfont = pygame.font.Font("anton.ttf", 30)
deadfontm = pygame.font.Font("rowdies.ttf", 60)
deadfont = pygame.font.Font("rowdies.ttf", 30)

ne = pygame.transform.scale(pygame.image.load("ne.png"), (58, 68))
ner = ne.get_rect(topleft = (20,10))

background = pygame.Surface((500, 400))
background.fill((40, 40, 40))
buttonback = pygame.transform.scale(pygame.image.load("button background.png"), (100, 400))
buttonbackr = buttonback.get_rect(topleft = (400, 0))
buttonsprite = pygame.transform.scale(pygame.image.load("button.png"), (85, 60))
undobut = pygame.transform.scale(pygame.image.load("undobut.png"), (30, 30))
undobutr = undobut.get_rect(topleft = (463, 362))
sprites = (
  (buttonsprite, buttonsprite.get_rect(topleft = (408, 40))),
  (buttonsprite, buttonsprite.get_rect(topleft = (408, 105))),
  (buttonsprite, buttonsprite.get_rect(topleft = (408, 170))),
  (buttonsprite, buttonsprite.get_rect(topleft = (408, 235))),
  (buttonsprite, buttonsprite.get_rect(topleft = (408, 300)))
)

colours = {
  "red": (255, 0, 0),
  "brown": (133, 51, 0),
  "orange": (255, 145, 0),
  "lorange": (255, 173, 107),
  "yellow": (255, 255, 0),
  "green": (0, 255, 0),
  "lgreen": (102, 255, 102),
  "cyan": (0, 255, 255),
  "sky": (0, 162, 255),
  "blue": (0, 0, 255),
  "banana": (255, 255, 89),
  "purple": (179, 3, 255),
  "lpurple": (210, 105, 255),
  "pink": (255, 92, 211),
  "white": (255, 255, 255),
  "coral": (255, 87, 87)
}

diff1 = (
  Button((10, 10, 185, 380), colours["red"]),
  Button((205, 10, 185, 380), colours["blue"])
)
diff2 = (
  Button((10, 10, 185, 185), colours["red"]),
  Button((205, 10, 185, 185), colours["blue"]),
  Button((10, 205, 185, 185), colours["green"]),
  Button((205, 205, 185, 185), colours["yellow"])
)
diff3 = (
  Button((10, 10, 120, 185), colours["red"]),
  Button((140, 10, 120, 185), colours["blue"]),
  Button((270, 10, 120, 185), colours["cyan"]),
  Button((10, 205, 120, 185), colours["green"]),
  Button((140, 205, 120, 185), colours["yellow"]),
  Button((270, 205, 120, 185), colours["purple"])
)
diff4 = (
  Button((10, 10, 120, 120), colours["red"]),
  Button((140, 10, 120, 120), colours["blue"]),
  Button((270, 10, 120, 120), colours["cyan"]),
  Button((10, 140, 120, 120), colours["green"]),
  Button((140, 140, 120, 120), colours["yellow"]),
  Button((270, 140, 120, 120), colours["purple"]),
  Button((10, 270, 120, 120), colours["pink"]),
  Button((140, 270, 120, 120), colours["brown"]),
  Button((270, 270, 120, 120), colours["orange"])
)
diff5 = (
  Button((10, 10, 87.5, 87.5), colours["red"]),
  Button((107.5, 10, 87.5, 87.5), colours["blue"]),
  Button((205, 10, 87.5, 87.5), colours["cyan"]),
  Button((302.5, 10, 87.5, 87.5), colours["white"]),
  Button((10, 107.5, 87.5, 87.5), colours["green"]),
  Button((107.5, 107.5, 87.5, 87.5), colours["yellow"]),
  Button((205, 107.5, 87.5, 87.5), colours["purple"]),
  Button((302.5, 107.5, 87.5, 87.5), colours["coral"]),
  Button((10, 205, 87.5, 87.5), colours["pink"]),
  Button((107.5, 205, 87.5, 87.5), colours["brown"]),
  Button((205, 205, 87.5, 87.5), colours["orange"]),
  Button((302.5, 205, 87.5, 87.5), colours["lgreen"]),
  Button((10, 302.5, 87.5, 87.5), colours["lorange"]),
  Button((107.5, 302.5, 87.5, 87.5), colours["sky"]),
  Button((205, 302.5, 87.5, 87.5), colours["banana"]),
  Button((302.5, 302.5, 87.5, 87.5), colours["lpurple"])
)
diffs = {
  40: diff1,
  105: diff2,
  170: diff3,
  235: diff4,
  300: diff5
}
buttons = []
moves = []
flash = pygame.USEREVENT
ftimer = pygame.USEREVENT + 1
ftimer2 = pygame.USEREVENT + 2
score = 0
dead = False
c = (0,0,0)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    if event.type == ftimer:
      pygame.time.set_timer(ftimer, 0)
      moves[index].colour = moves[index].off_colour
      index += 1
    if event.type == ftimer2:
      pygame.time.set_timer(ftimer2, 0)
      cbutton.colour = cbutton.off_colour
    if event.type == flash and moves and index != len(moves):
      pygame.time.set_timer(ftimer, 200)
      moves[index].colour = moves[index].on_colour
    if event.type == pygame.MOUSEBUTTONUP:
      if undobutr.collidepoint(pygame.mouse.get_pos()):
        buttons = []
      for sprite in sprites:
        if sprite[1].collidepoint(pygame.mouse.get_pos()):
          buttons = diffs[sprite[1].y]
          moves = [choice(buttons)]
          index = 0
          index2 = 0
          pygame.time.set_timer(flash, 600)
          dead = False
          score = 0
      for button in buttons:
        if button.rect.collidepoint(pygame.mouse.get_pos()):
          pygame.time.set_timer(ftimer2, 200)
          cbutton = button
          cbutton.colour = cbutton.on_colour
          if button == moves[index2]:
            index2 += 1
            if index2 == len(moves):
              score += 1
              moves.append(choice(buttons))
              index = 0
              index2 = 0
              pygame.time.set_timer(flash, 800)
          else:
            buttons = []
            dead = True
  
  screen.blit(background, (0, 0))
  if dead:
    makename("YOU DIED", (200, 200), deadfontm, (255,0,0))
    makename(f"Score: {str(score)}", (200, 238), deadfont, (255,0,0))
  screen.blit(buttonback, buttonbackr)
  for sprite in sprites:
    screen.blit(sprite[0], sprite[1])

  makename("Difficulty", (450, 22), butfonts, c)
  makename("Very Easy", (450, 70), butfonts, c)
  makename("Easy", (450, 135), butfont, c)
  makename("Medium", (450, 200), butfontm, c)
  makename("Hard", (450, 265), butfont, c)
  makename("Very Hard", (450, 330), butfonts, c)
  screen.blit(ne, ner)
  #255,179,82
  screen.blit(undobut, undobutr)
  for button in buttons:
    pygame.draw.rect(screen, button.colour, button.rect)
  
  pygame.display.update()
  clock.tick(60)