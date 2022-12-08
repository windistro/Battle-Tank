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
    if y_alien < -500 :
        y_alien = 400
        x_alien = rd.randint(-525,110)
    glTranslated(x_alien, y_alien,0)
    print(x_alien)
    #bibir
    glColor3ub(255,0,0)
    glBegin(GL_QUADS)
    glVertex2f(100,136)
    glVertex2f(100,112)
    glVertex2f(100,112)
    glVertex2f(178,112)
    glVertex2f(178,112)
    glVertex2f(178,136)
    glVertex2f(178,136)
    glVertex2f(100,136)
    glEnd()

    #dalem mulut
    glColor3ub(0,0,0)
    glBegin(GL_QUADS)
    glVertex2f(106,130)
    glVertex2f(106,118)
    glVertex2f(106,118)
    glVertex2f(172,118)
    glVertex2f(172,118)
    glVertex2f(172,130)
    glVertex2f(172,130)
    glVertex2f(106,130)
    glEnd()

    #gigi1
    glColor3ub(255,255,255)
    glBegin(GL_QUADS)
    glVertex2f(118,118)
    glVertex2f(118,124)
    glVertex2f(118,124)
    glVertex2f(124,124)
    glVertex2f(124,124)
    glVertex2f(124,118)
    glVertex2f(124,118)
    glVertex2f(118,118)
    glEnd()

    #gigi2
    glColor3ub(255,255,255)
    glBegin(GL_QUADS)
    glVertex2f(136,118)
    glVertex2f(136,124)
    glVertex2f(136,124)
    glVertex2f(142,124)
    glVertex2f(142,124)
    glVertex2f(142,118)
    glVertex2f(142,118)
    glVertex2f(136,118)
    glEnd()
    #GIGI 3
    glColor3ub(255,255,255)
    glBegin(GL_QUADS)
    glVertex2f(154,118)
    glVertex2f(154,124)
    glVertex2f(154,124)
    glVertex2f(160,124)
    glVertex2f(160,124)
    glVertex2f(160,118)
    glVertex2f(160,118)
    glVertex2f(154,118)
    glEnd()
    #kepala alien
    glColor3ub(191,0,255)
    glBegin(GL_POLYGON)
    glVertex2f(94,136)
    glVertex2f(184,136)
    glVertex2f(184,136)
    glVertex2f(184,148)
    glVertex2f(184,148)
    glVertex2f(94,148)
    glEnd()

    #tangan kiri
    glColor3ub(191,0,255)
    glBegin(GL_QUADS)
    glVertex2f(94,136)
    glVertex2f(94,130)
    glVertex2f(94,130)
    glVertex2f(100,130)
    glVertex2f(100,130)
    glVertex2f(100,136)
    glVertex2f(100,136)
    glVertex2f(94,136)
    glEnd()
    glColor3ub(191,0,255)
    glBegin(GL_QUADS)
    glVertex2f(94,136)
    glVertex2f(88,136)
    glVertex2f(88,136)
    glVertex2f(88,118)
    glVertex2f(88,118)
    glVertex2f(94,118)
    glVertex2f(94,118)
    glVertex2f(94,136)
    glEnd()
    
    #tangan kanan
    glColor3ub(191,0,255)
    glBegin(GL_QUADS)
    glVertex2f(178,136)
    glVertex2f(178,130)
    glVertex2f(178,130)
    glVertex2f(184,130)
    glVertex2f(184,130)
    glVertex2f(184,136)
    glVertex2f(184,136)
    glVertex2f(178,136)
    glEnd()
    glColor3ub(191,0,255)
    glBegin(GL_QUADS)
    glVertex2f(184,136)
    glVertex2f(184,118)
    glVertex2f(184,118)
    glVertex2f(190,118)
    glVertex2f(190,118)
    glVertex2f(190,136)
    glVertex2f(190,136)
    glVertex2f(184,136)
    glEnd()

    #dahi
    glColor3ub(255,255,0)
    glBegin(GL_QUADS)
    glVertex2f(106,148)
    glVertex2f(172,148)
    glVertex2f(172,148)
    glVertex2f(172,154)
    glVertex2f(172,154)
    glVertex2f(106,154)
    glVertex2f(106,154)
    glVertex2f(106,148)
    glEnd()

    #mata kiri
    glColor3ub(0,0,0)
    glBegin(GL_QUADS)
    glVertex2f(118,148)
    glVertex2f(130,148)
    glVertex2f(130,148)
    glVertex2f(130,136)
    glVertex2f(130,136)
    glVertex2f(118,136)
    glVertex2f(118,136)
    glVertex2f(118,148)
    glEnd()

    #mata kanan
    glColor3ub(0,0,0)
    glBegin(GL_QUADS)
    glVertex2f(148,148)
    glVertex2f(160,148)
    glVertex2f(160,148)
    glVertex2f(160,136)
    glVertex2f(160,136)
    glVertex2f(148,136)
    glVertex2f(148,136)
    glVertex2f(148,148)
    glEnd()

    #antena kiri
    glColor3ub(255,255,255)
    glBegin(GL_QUADS)
    glVertex2f(106,154)
    glVertex2f(112,154)
    glVertex2f(112,154)
    glVertex2f(112,160)
    glVertex2f(112,160)
    glVertex2f(106,160)
    glVertex2f(106,160)
    glVertex2f(106,154)
    glEnd()

    #antena kanan
    glColor3ub(255,255,255)
    glBegin(GL_QUADS)
    glVertex2f(166,160)
    glVertex2f(172,160)
    glVertex2f(172,160)
    glVertex2f(172,154)
    glVertex2f(172,154)
    glVertex2f(166,154)
    glVertex2f(166,154)
    glVertex2f(166,160)
    glEnd()

    #kaki kiri
    glColor3ub(191,0,255)
    glBegin(GL_QUADS)
    glVertex2f(112,112)
    glVertex2f(94,112)
    glVertex2f(94,112)
    glVertex2f(94,106)
    glVertex2f(94,106)
    glVertex2f(112,106)
    glVertex2f(112,106)
    glVertex2f(112,112)
    glEnd()
    
    #kaki kanan
    glColor3ub(191,0,255)
    glBegin(GL_QUADS)
    glVertex2f(166,112)
    glVertex2f(166,106)
    glVertex2f(166,106)
    glVertex2f(184,106)
    glVertex2f(184,106)
    glVertex2f(184,112)
    glVertex2f(184,112)
    glVertex2f(166,112)
    glEnd()

    #sebelah mata
    glColor3ub(255,127,0)
    glBegin(GL_QUADS)
    glVertex2f(130,148)
    glVertex2f(130,136)
    glVertex2f(130,136)
    glVertex2f(148,136)
    glVertex2f(148,136)
    glVertex2f(148,148)
    glVertex2f(148,148)
    glVertex2f(130,148)
    
    glEnd()
    glPopMatrix()

i = 1
def speed():
    global y_alien, score, i
    if score >= i*1000:
        i += 1
    if score == 500:
        winning()

def winning():
    drawText("Congratulations you Win", 0,0,255,255,255)

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