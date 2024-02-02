from vpython import *
import numpy as np

class obj:
    def __init__(self,l,w,h,x,y):
        self.length=l
        self.width=w
        self.height=h
        self.rotationAngle=np.pi/16
        self.body=box()
        self.x=x 
        self.y=y

    def setPos(self,x,y):
        self.x=self.x
        self.y=self.y
        self.body.pos=vector(x,y,self.height)
        self.body.axis=vector(1500,0,0)
       
    def move(self,direction,newX,newY):
        self.body.pos.x=newX
        self.body.pos.y=newY
        if direction=='left':
            self.body.rotate(axis=vector(0,0,1),angle=self.rotationAngle,origin=self.body.pos)
        elif direction=='right':
            self.body.rotate(axis=vector(0,0,1),angle=-self.rotationAngle,origin=self.body.pos)
        
class Car(obj):
    def __init__(self,l,w,h,x=0,y=0) -> None:
        super().__init__(l,w,h,x,y)
        self.speed=2500

        self.body=box(
            pos=vector(x,y,h),
            size=vector(w,l,h),
            color=color.red)

class Barrel(obj):
    def __init__(self,c,l,w,h,x=0,y=0) -> None:
        super().__init__(l,w,h,x,y)
        self.body=cylinder(
            pos=vector(x,y,h),
            size=vector(l,w,h),
            axis=vector(0,0,1),
            color=c
        )