#STARTERS
import pygame, time, random, sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
direction = 'north'
current = [0,0,1]
increment = 5
sleep = .0025
xx = 60
yy = 120-increment
plotPoints = [[xx,yy+increment],[xx,yy]]

#DIRECTIONS
def rightTurn():
  global sleep
  global increment
  global direction
  global xx
  global yy
  if direction == 'north':
    xx += increment
    direction = 'east'
  elif direction == 'south':
    xx -= increment
    direction = 'west'
  elif direction == 'west':
    yy -= increment
    direction = 'north'
  elif direction == 'east':
    yy += increment
    direction = 'south'
  plotPoints.append([xx,yy])
  pygame.draw.lines(screen,[0,0,0],False,plotPoints,1)
  pygame.display.flip()
  time.sleep(sleep)

def leftTurn():
  global sleep
  global increment
  global direction
  global xx
  global yy
  if direction == 'north':
    xx -= increment
    direction = 'west'
  elif direction == 'south':
    xx += increment
    direction = 'east'
  elif direction == 'west':
    yy += increment
    direction = 'south'
  elif direction == 'east':
    yy -= increment
    direction = 'north'
  plotPoints.append([xx,yy])
  pygame.draw.lines(screen,[0,0,0],False,plotPoints,1)
  pygame.display.flip()
  time.sleep(sleep)

#ITERATIONS
def Iterate():
  global current
  second = current[:]
  second.reverse()
  third = []

  for element in second:
    if element == 0:
      third.append(1)
    elif element == 1:
      third.append(0)

  current.append(0)
  current.extend(third)
  return current

for i in range(0,9):
  Iterate()

for element in current:
  if element == 0:
    rightTurn()
  elif element == 1:
    leftTurn()

#EXIT
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
