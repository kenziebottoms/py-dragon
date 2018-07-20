#SETUP
import pygame, time, sys

#ITERATE
def multiply(number_list,number):
  for i in range(len(number_list)):
    number_list[i] *= (number)
  return number_list

def iterate(turns_list):
  negated_flipped_turns_list = multiply(turns_list[::-1],-1)
  turns_list.append(1)
  turns_list += negated_flipped_turns_list
  return turns_list

#TURNS
#  north = 0
#  east = 1
#  south = 2
#  west = 3
#  right = 1
#  left = -1
def turn(cardinal,turn_direction):
  return (cardinal + 4 + turn_direction) % 4

def get_coords(cardinal,line_length):
  if cardinal % 2 == 0:
    return [(cardinal-1)*line_length,0]
  else:
    return [0,(cardinal-2)*line_length]

#PLOT POINTS
def generate_plot_points(x_initial,y_initial,turns_list,line_length):
  plot_points = [[x_initial,y_initial]]
  x = x_initial
  y = y_initial
  cardinal = 0
  coords = []
  for item in turns_list:
    cardinal = turn(cardinal,item)
    coords = get_coords(cardinal,line_length)
    x += coords[0]
    y += coords[1]
    plot_points.append([x,y])
  return plot_points

#DISPLAY
def display(plot_points):
  pygame.init()
  screen = pygame.display.set_mode([600,600])
  screen.fill([255,255,255])
  for i in range(2,len(plot_points)):
    pygame.draw.lines(screen,[0,0,0],False,plot_points[:i],1)
    pygame.display.flip()
    time.sleep(.002)

#EXECUTION
turns_list = []

for i in range(11):
  iterate(turns_list)

plot_points = generate_plot_points(200,400,turns_list,8)

display(plot_points)

#EXIT
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
