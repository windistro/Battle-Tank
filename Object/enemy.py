from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import *

def alien():
    glScalef(.3,.3,0)
    #bibir
    glColor3ub(255,0,0)
    glBegin(GL_QUADS)
    glVertex2f(100,220)
    glVertex2f(100,140)
    glVertex2f(100,140)
    glVertex2f(360,140)
    glVertex2f(360,140)
    glVertex2f(360,220)
    glVertex2f(360,220)
    glVertex2f(100,220)
    glEnd()
    #dalem mulut
    glColor3ub(0,0,0)
    glBegin(GL_QUADS)
    glVertex2f(120,200)
    glVertex2f(120,160)
    glVertex2f(120,160)
    glVertex2f(340,160)
    glVertex2f(340,160)
    glVertex2f(340,200)
    glVertex2f(340,200)
    glVertex2f(120,200)
    glEnd()
    #gigi1
    glColor3ub(255,255,255)
    glBegin(GL_QUADS)
    glVertex2f(160,160)
    glVertex2f(160,180)
    glVertex2f(160,180)
    glVertex2f(180,180)
    glVertex2f(180,180)
    glVertex2f(180,160)
    glVertex2f(180,160)
    glVertex2f(160,160)
    glEnd()
    #gigi2
    glColor3ub(255,255,255)
    glBegin(GL_QUADS)
    glVertex2f(220,160)
    glVertex2f(220,180)
    glVertex2f(220,180)
    glVertex2f(240,180)
    glVertex2f(240,180)
    glVertex2f(240,160)
    glVertex2f(240,160)
    glVertex2f(220,160)
    glEnd()
    #GIGI 3
    glColor3ub(255,255,255)
    glBegin(GL_QUADS)
    glVertex2f(280,160)
    glVertex2f(280,180)
    glVertex2f(280,180)
    glVertex2f(300,180)
    glVertex2f(300,180)
    glVertex2f(300,160)
    glVertex2f(300,160)
    glVertex2f(280,160)
    glEnd()
    #kepala alien
    glColor3ub(191,0,255)
    glBegin(GL_POLYGON)
    glVertex2f(80,220)
    glVertex2f(380,220)
    glVertex2f(380,220)
    glVertex2f(380,260)
    glVertex2f(380,260)
    glVertex2f(80,260)
    glEnd()
    glColor3ub(191,0,255)
    glBegin(GL_QUADS)
    glVertex2f(80,220)
    glVertex2f(80,200)
    glVertex2f(80,200)
    glVertex2f(100,200)
    glVertex2f(100,200)
    glVertex2f(100,220)
    glVertex2f(100,220)
    glVertex2f(80,220)
    glEnd()
    glColor3b(191,0,255)
    glBegin(GL_QUADS)
    glVertex2f(80,220)
    glVertex2f(60,220)
    glVertex2f(60,220)
    glVertex2f(60,160)
    glVertex2f(60,160)
    glVertex2f(80,160)
    glVertex2f(80,160)
    glVertex2f(80,220)
    glEnd()
    #tangan kanan
    glColor3ub(191,0,255)
    glBegin(GL_QUADS)
    glVertex2f(360,220)
    glVertex2f(360,200)
    glVertex2f(360,200)
    glVertex2f(380,200)
    glVertex2f(380,200)
    glVertex2f(380,220)
    glVertex2f(380,220)
    glVertex2f(360,220)
    glEnd()
    glColor3ub(191,0,255)
    glBegin(GL_QUADS)
    glVertex2f(380,220)
    glVertex2f(380,160)
    glVertex2f(380,160)
    glVertex2f(400,160)
    glVertex2f(400,160)
    glVertex2f(400,220)
    glVertex2f(400,220)
    glVertex2f(380,220)
    glEnd()

    glColor3ub(255,255,0)
    glBegin(GL_QUADS)
    glVertex2f(120,260)
    glVertex2f(340,260)
    glVertex2f(340,260)
    glVertex2f(340,280)
    glVertex2f(340,280)
    glVertex2f(120,280)
    glVertex2f(120,280)
    glVertex2f(120,260)
    glEnd()
    #mata kiri
    glColor3ub(0,0,0)
    glBegin(GL_QUADS)
    glVertex2f(160,260)
    glVertex2f(200,260)
    glVertex2f(200,260)
    glVertex2f(200,220)
    glVertex2f(200,220)
    glVertex2f(160,220)
    glVertex2f(160,220)
    glVertex2f(160,260)
    glEnd()
    #mata kanan
    glColor3ub(0,0,0)
    glBegin(GL_QUADS)
    glVertex2f(260,260)
    glVertex2f(300,260)
    glVertex2f(300,260)
    glVertex2f(300,220)
    glVertex2f(300,220)
    glVertex2f(260,220)
    glVertex2f(260,220)
    glVertex2f(260,260)
    glEnd()
    #antena kiri
    glColor3ub(255,255,255)
    glBegin(GL_QUADS)
    glVertex2f(120,280)
    glVertex2f(140,280)
    glVertex2f(140,280)
    glVertex2f(140,300)
    glVertex2f(140,300)
    glVertex2f(120,300)
    glVertex2f(120,300)
    glVertex2f(120,280)
    glEnd()
    #antena kanan
    glColor3ub(255,255,255)
    glBegin(GL_QUADS)
    glVertex2f(320,300)
    glVertex2f(340,300)
    glVertex2f(340,300)
    glVertex2f(340,280)
    glVertex2f(340,280)
    glVertex2f(320,280)
    glVertex2f(320,280)
    glVertex2f(320,300)
    glEnd()
    #kaki kiri
    glColor3ub(191,0,255)
    glBegin(GL_QUADS)
    glVertex2f(140,140)
    glVertex2f(80,140)
    glVertex2f(80,140)
    glVertex2f(80,120)
    glVertex2f(80,120)
    glVertex2f(140,120)
    glVertex2f(140,120)
    glVertex2f(140,140)
    glEnd()
    #kaki kanan
    glColor3ub(191,0,255)
    glBegin(GL_QUADS)
    glVertex2f(320,140)
    glVertex2f(320,120)
    glVertex2f(320,120)
    glVertex2f(380,120)
    glVertex2f(380,120)
    glVertex2f(380,140)
    glVertex2f(380,140)
    glVertex2f(320,140)
    glEnd()
    #dahi
    glColor3ub(255,127,0)
    glBegin(GL_QUADS)
    glVertex2f(200,260)
    glVertex2f(200,220)
    glVertex2f(200,220)
    glVertex2f(260,220)
    glVertex2f(260,220)
    glVertex2f(260,260)
    glVertex2f(260,260)
    glVertex2f(200,260)
    
    glEnd()