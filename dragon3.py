# MUST ENTER 'python2.7-32 dragon3.py' to work

# IMPORTS
import pygame, time, sys

#what needs to happen:
#pygame.draw.lines(surface,color,False,point_list,width)

# CONSTANTS
START_X = 200               #pixels
START_Y = 400               #pixels
START_DIRECTION = 3         #west
SCREEN_WIDTH = 1200         #pixels
SCREEN_HEIGHT = 1200        #pixels
LINE_LENGTH = 8             #pixels
LINE_WIDTH = 1              #pixels
DRAGON_COLOR = [0,0,0]      #black
BG_COLOR = [255,255,255]    #white
ITERATIONS = 12
RIGHT = 1                   #90 degree rotations
LEFT = -1                   #90 degree rotations

# INITIATE
def init():
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
    screen.fill(BG_COLOR)
    return screen

# GENERATE TURN LIST
def inverse(list):
    inverse_list = []
    for item in list:
        inverse_list.append(item * -1)
    return inverse_list

def get_next_iteration(last_iteration):
    first_half = list(last_iteration)
    second_half = list(first_half)
    second_half.reverse()
    second_half = inverse(second_half)
    next_iteration = list(first_half)
    next_iteration.append(RIGHT)
    next_iteration.extend(second_half)
    return next_iteration

def map(iterations):
    turn_list = []
    for i in range(iterations+1):
        turn_list = get_next_iteration(turn_list)
    return turn_list

# GENERATE POINT LIST
def turns_to_points(turn_list):
    cardinal = START_DIRECTION
    point_list = [[START_X,START_Y],add_point(START_X,START_Y,cardinal)]
    current_x = add_point(START_X,START_Y,cardinal)[0]
    current_y = add_point(START_X,START_Y,cardinal)[1]
    for turn in turn_list:
        cardinal += turn
        pair = add_point(current_x,current_y,cardinal)
        point_list.append(pair)
        current_x = pair[0]
        current_y = pair[1]
    return point_list

def add_point(x,y,cardinal):
    if cardinal % 2 == 0:   # if cardinal is N/S/vertical
        y += ((cardinal % 4) - 1) * LINE_LENGTH
    else:                   # if cardinal is E/W/horizontal
        x -= ((cardinal % 4) - 2) * LINE_LENGTH
    return [x,y]

# PLOT POINTS
def plot(point_list,screen):
    pygame.draw.lines(screen,DRAGON_COLOR,False,point_list,LINE_WIDTH)
    pygame.display.flip()

# EXECUTE
def draw_dragon(iterations):
    plot(turns_to_points(map(ITERATIONS)),init())

# TESTS
def test():
    if inverse([1,-1,-1,1]) == [-1,1,1,-1]:
        print 'inverse() works'
    else:
        print 'INVERSE() IS BROKEN:\n\t'+str(inverse([1,-1,-1,1]))

    if get_next_iteration([RIGHT,RIGHT,LEFT]) == [1, 1, -1, 1, 1, -1, -1]:
        print 'get_next_iteration() works'
    else:
        print 'GET_NEXT_ITERATION() IS BROKEN:\n\t'+str(get_next_iteration([1,1,-1]))

    if map(3) == [1, 1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1]:
        print 'map() works'
    else:
        print 'MAP() IS BROKEN:\n\t'+str(map(3))

init()
#test()
draw_dragon(ITERATIONS)

# EXIT EVENT LISTENER
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
