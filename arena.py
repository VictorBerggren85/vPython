# py -3.11 -m venv ENVvPy
# from __future__ import absolute_import
# from __future__ import division
# from __future__ import print_function

from vpython import *
from objs import Car, Barrel
import abc
# import tensorflow as tf
import numpy as np

# from tf_agents.environments import py_environment
# from tf_agents.environments import tf_environment
# from tf_agents.environments import tf_py_environment
# from tf_agents.environments import utils
# from tf_agents.specs import array_spec
# from tf_agents.environments import wrappers
# from tf_agents.environments import suite_gym
# from tf_agents.trajectories import time_step as ts


# class Arena(py_environment.PyEnvironment):
class Arena():

    def __init__(self,l,w,h):
        self.l=l
        self.w=w
        self.h=h
        self.startingPos=(0,((-l*.1)*3))
        self.rightBoundary=vector(w/2,0,h/2)
        self.leftBoundary=vector(-w/2,0,h/2)
        self.frontBoundary=vector(0,-l/2,h/2)
        self.backBoundary=vector(0,l/2,h/2)
        self.goalBlue=box(pos=vector(0,(l*.5)-(w/2),.6),
                      color=color.blue,
                      size=vector(w/2,w/2,1)) 
        
        self.barrelGreen=Barrel(color.green,w*.025,w*.025,w*.025)
        
        self.car=Car(l*.1,w*.15,h*.1)
        self.car.setPos(0,(-l*.1)*3)

        # self._action_spec=array_spec.BoundedArraySpec(
        #     shape=(),dtype=np.int32,minimum=0,maximum=2,name='action')
        # self._observation_spec=array_spec.BoundedArraySpec(
        #     shape=(1,),dtype=np.int32,minimum=0,name='observation')
        # self._state=0
        # self._episode_ended=False
    
        box(size=vector(w,l,1),
            color=vector(.1,.1,.1))
        box(pos=self.rightBoundary,
            size=vector(1,l,h),
            color=vector(.1,.1,.1))
        box(pos=self.leftBoundary,
            size=vector(1,l,h),
            color=vector(.1,.1,.1))
        box(pos=self.frontBoundary,
            size=vector(w,1,h),
            color=vector(.1,.1,.1))
        box(pos=self.backBoundary,
            size=vector(w,1,h),
            color=vector(.1,.1,.1))

    def done(self):
        if self.barrelGreen.body.pos.x>self.goalBlue.pos.x-(self.w/2) and self.barrelGreen.body.pos.x<self.goalBlue.pos.x+(self.w/2):
            if self.barrelGreen.body.pos.y>self.goalBlue.pos.y-(self.w/2) and self.barrelGreen.body.pos.y<self.goalBlue.pos.y+(self.w/2):
                return True
        return False
    
    def checkCollisionWall(self,obj,x,y):
        if x>self.leftBoundary.x+obj.length/2 and x<self.rightBoundary.x-obj.length/2:
            pass
        else:
            x=obj.body.pos.x
        if y>self.frontBoundary.y+obj.length/2 and y<self.backBoundary.y-obj.length/2:    
            pass
        else: 
            y=obj.body.pos.y
        return (x,y)

    def carStartingPos(self):
        self.car.setPos(self.startingPos[0],self.startingPos[1])

    def moveCar(self,dir,speedMultiplier=1.0):
        x=self.car.body.pos.x+(
            self.car.speed*speedMultiplier*(((-self.car.body.axis.y))/(self.car.width)*self.car.rotationAngle))
        y=self.car.body.pos.y+(
            self.car.speed*speedMultiplier*(((self.car.body.axis.x))/(self.car.width)*self.car.rotationAngle))

        testedX,testedY=self.checkCollisionWall(self.car,x,y)
        self.car.move(dir,testedX,testedY)

    # def action_spec(self):
    #     return self._action_spec
    # def observation_spec(self):
    #     return self._observation_spec
    # def _reset(self):
    #     self._state=0
    #     self._episode_ended=False
    #     self.carStartingPos()
    #     return ts.restart(np.array([self._state],dtype=np.int32))

    # def _step(self,action):
    #     if self._episode_ended:
    #         return self._reset()
    #     if self.done():
    #         pass
