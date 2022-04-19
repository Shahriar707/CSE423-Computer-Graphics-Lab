from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_points():
    glPointSize(2)
    glBegin(GL_POINTS)

    # for the door handle
    glVertex2f(265, 190)
    glVertex2f(250, 550)

    glEnd()

def draw_lines():
    glPointSize(2)
    glBegin(GL_LINES)

    # for the outer walls
    glVertex2f(100, 150)
    glVertex2f(400, 150)
    glVertex2f(400, 150)
    glVertex2f(400, 450)
    glVertex2f(400, 450)
    glVertex2f(100, 450)
    glVertex2f(100, 450)
    glVertex2f(100, 150)

    # for the door
    glVertex2f(225, 150)
    glVertex2f(225, 250)
    glVertex2f(225, 250)
    glVertex2f(275, 250)
    glVertex2f(275, 250)
    glVertex2f(275, 150)

    # for the window 1
    glVertex2f(125, 400)
    glVertex2f(200, 400)
    glVertex2f(200, 400)
    glVertex2f(200, 340)
    glVertex2f(200, 340)
    glVertex2f(125, 340)
    glVertex2f(125, 400)
    glVertex2f(125, 340)

    # for the window 2
    glVertex2f(375, 400)
    glVertex2f(375, 340)
    glVertex2f(375, 400)
    glVertex2f(300, 400)
    glVertex2f(300, 400)
    glVertex2f(300, 340)
    glVertex2f(300, 340)
    glVertex2f(375, 340)

    glVertex2f(100, 450)
    glVertex2f(250, 500)
    glVertex2f(250, 500)
    glVertex2f(400, 450)

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
    draw_lines()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(720, 640)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab1 - Task2")
glutDisplayFunc(showScreen)

glutMainLoop()