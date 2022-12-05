from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import *

class Tank():
    def __init__(self,x_min, x_max, y_min, y_max) -> None:
        self._x_min = x_min
        self._x_max = x_max
        self._y_min = y_min
        self._y_max = y_max

    def player():
        glColor3f(1,1,0)
        glBegin(GL_POLYGON)
        
        glEnd()