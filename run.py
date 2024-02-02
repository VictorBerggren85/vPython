
from arena import Arena
from vpython import *
import numpy as np

runCanvas=canvas(background=color.white)
environment=Arena(l=30000,w=10000,h=5000)


while True:
    rate(50)
    keys=keysdown()
    if 'q' in keys:
        print('quit')
        break
    elif 'a' in keys and 'd' in keys:
        environment.moveCar('forward')
    elif 'a' in keys:
        environment.moveCar('left',.4)
    elif 'd' in keys:
        environment.moveCar('right',.4)
    keys=[]
