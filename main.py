from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import *

pos_x = 0
pos_y = 0
pos_x_min_gun = 218
pos_x_max_gun = 221

def iterate():
    glViewport(0, 0, 900, 800) 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()
    glOrtho(0.0, 900, 0.0, 800, 0.0, 1.0) 
    glMatrixMode (GL_MODELVIEW) 
    glLoadIdentity()

def tank():
    global pos_x, pos_y
    glTranslatef(pos_x, pos_y, 0)
    glColor3f(1,1,0)
    glBegin(GL_POLYGON)
    glVertex2f(209,100)
    glVertex2f(200,100)
    glVertex2f(200,136)
    glVertex2f(209,136)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(209,103)
    glVertex2f(215,103)
    glVertex2f(215,133)
    glVertex2f(209,133)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(215,103)
    glVertex2f(224,103)
    glVertex2f(224,136)
    glVertex2f(215,136)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(224,103)
    glVertex2f(230,103)
    glVertex2f(230,133)
    glVertex2f(224,133)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(230,100)
    glVertex2f(239,100)
    glVertex2f(239,136)
    glVertex2f(230,136)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(218,136)
    glVertex2f(221,136)
    glVertex2f(221,148)
    glVertex2f(218,148)
    glEnd()
    #### Hiasan ####
    glColor3f(0,0,0)
    glBegin(GL_LINES)
    glVertex2f(209,100)
    glVertex2f(209,136)
    glVertex2f(230,100)
    glVertex2f(230,136)
    glVertex2f(215,115)
    glVertex2f(224,115)
    glVertex2f(224,115)
    glVertex2f(224,124)
    glVertex2f(224,124)
    glVertex2f(215,124)
    glVertex2f(215,124)
    glVertex2f(215,115)
    glEnd()

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

def bullet(pos):
    glColor3f(1,1,0)
    glBegin(GL_QUADS)
    glVertex2f()

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10,update,0)

def keyboard(key,x,y):
    global pos_x, pos_y
    if key == b'a':
        pos_x -= 10
    elif key == b'd':
        pos_x += 10
    elif key == b'w':
        pos_y += 10
    elif key == b's':
        pos_y -= 10
    elif key == b' ':
        bullet()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity()
    iterate()
    wall()
    hp()
    tank()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA) 
glutInitWindowSize(900, 800) 
glutInitWindowPosition(500, 100)

wind = glutCreateWindow("BattleCity") 
glutDisplayFunc(showScreen)
glutTimerFunc(1,update,0)
glutIdleFunc(showScreen)
glutKeyboardFunc(keyboard)
glutMainLoop()