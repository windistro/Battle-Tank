from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import *
import random as rd 

x_alien = 0
y_alien = 0
w, h = 900,800
score = 0

def alien():
    glPushMatrix()
    global x_alien, y_alien
    y_alien -= 5*i
    if y_alien < -1500 :
        y_alien = 1200
        x_alien = rd.randint(-1500,650)
    glScale(0.3,0.3,0)
    glTranslated(x_alien, y_alien,0)
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

    #tangan kiri
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
    glColor3ub(191,0,255)
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

    #dahi
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

    #sebelah mata
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
    glPopMatrix()

i = 1
def speed():
    global y_alien, score, i
    if score >= i*1000:
        i += 1
    print(i, y_alien)

def wall():
    global score
    score += 1
    glPushMatrix()
    glColor3f(0.5,0.5,0.5)
    glBegin(GL_QUADS)
    glVertex2f(300,400)
    glVertex2f(450,400)
    glVertex2f(450,-400)
    glVertex2f(300,-400)
    glEnd()
    drawText("Score :", 325, 0, 255, 255, 255)
    drawText(str(score),350, -25, 255, 255, 255)
    glPopMatrix()

def drawText(text,xpos,ypos,r,g,b):
    color = (r,g,b)
    font_style = GLUT_BITMAP_9_BY_15
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in text:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i)) 