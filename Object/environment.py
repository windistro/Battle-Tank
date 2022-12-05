from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import *

def hp():
    glColor3f(1,0,0.2)
    glTranslatef(150,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(700, 615)
    glVertex2f(665, 665)
    glVertex2f(665, 675)
    glVertex2f(675, 700)
    glVertex2f(690, 700)
    glVertex2f(700, 675)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(700, 615)
    glVertex2f(735, 665)
    glVertex2f(735, 675)
    glVertex2f(725, 700)
    glVertex2f(710, 700)
    glVertex2f(700, 675)
    glEnd()

def wall():
    glColor3f(0.5,0.5,0.5)
    glBegin(GL_QUADS)
    glVertex2f(800,800)
    glVertex2f(900,800)
    glVertex2f(900,0)
    glVertex2f(800,0)
    glEnd()
