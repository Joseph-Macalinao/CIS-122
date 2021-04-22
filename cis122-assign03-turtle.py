'''
Name: Joseph Macalinao
Assignment: Assignment 3 CIS 122 Spring 2021
Credit: Me and Kaya Jang
Description: Make a drawing in python using Turtle
'''

import turtle

def draw_line(t, x, y, angle, length):
    '''
    This function draws a line using arguments: turtle name, starting x, starting y, the angle to draw, and the length of the line

    This function will start at (0, 0) and after lifting the pen up, go to the x and y set by the user.
    Then, it will set the pen down, turn to the user input angle, and draw the user input length.
    It will end in the pen up position

    t(Turtle): Drawing turtle
    x(int/float): initial x value
    y(int/float): initial y value
    angle(int/float): angle to draw line at
    length(int/float): length of line to draw

    Returns: None
    '''
    t.pu()
    t.setx(x)
    t.sety(y)
    t.pd()
    t.rt(angle)
    t.fd(length)
    t.pu()


#draw_line(morla, 100, 100, 0, 200)
#draw_line(morla, -100, -100, 270, 50)
#draw_line(morla, 200, -200, 45, 75)

def draw_radial_lines(t, x, y, length, num_lines):
    angle = 0
    for i in range(num_lines):
        draw_line(t, x, y, angle, length)
        angle = angle + (360 / num_lines)
        t.setheading(0)
    turtle.done()

morla = turtle.Turtle()

#draw_radial_lines(morla, -100, -100, 25, 8)
#draw_radial_lines(morla, -100, 100, 100, 4)
#draw_radial_lines(morla, 100, -100, 200, 16)
#draw_radial_lines(morla, 100, 100, 50, 32)

def draw_radials_in_quadrants(t, length, num_lines):
    lessgoooo


