import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_points():
    glPointSize(2)
    glBegin(GL_POINTS)
    x = [np.random.randint(100, 500) for i in range(0, 50)]
    x.sort()
    y = [np.random.randint(200, 400) for i in range(0, 50)]
    y.sort()
    for i in range(0, 50):
        glVertex2f(x[i], y[i])
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0)

    draw_points()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(720, 640)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab1 - Task1")
glutDisplayFunc(showScreen)

glutMainLoop()