from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import *
from main import drawText
from random import randint

w,h = 900,800

def comet(x,y):
    glColor3f(1,1,0)
    glTranslatef(10,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(x,y+4)
    glVertex2f(x+2.33,y+4)
    glVertex2f(x+3,y+6)
    glVertex2f(x+3.66,y+4)
    glVertex2f(x+6,y+4)
    glVertex2f(x+4.15,y+2.52)
    glVertex2f(x+5,y)
    glVertex2f(x+3,y+1.6)
    glVertex2f(x+1,y)
    glVertex2f(x+1.82,y+2.52)
    glEnd()

def initial():
    drawText("Press Space to Play", -100 , 0, 255, 255, 255)
    for i in range(100):
        comet(-w/2,randint(-h,h))
    