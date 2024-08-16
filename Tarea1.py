from sympy.plotting import plot3d_parametric_line
from sympy import symbols, cos, sin , exp, pi
from sympy import plot_parametric

t = symbols('t')
radio = 1

#Curva 1: Circulo
def x(t):
    return radio * cos(t)
def y(t):
    return radio * sin(t)

def x_involute(t):
    return radio * (cos(t) + (t * sin(t)))
def y_involute(t):
    return radio * (sin(t) - (t * cos(t)))

circle = plot_parametric(x(t), y(t), (t, -pi, pi), show = False, line_color = "blue", label = "Circle", aspect_ratio = (1,1))
circle_involute = plot_parametric(x_involute(t), y_involute(t), (t, 0, 4*pi), show = False, line_color = "magenta", label = "Circle Involute", aspect_ratio = (1,1))

circle.extend(circle_involute)
circle.show()

#Curva 2: Catenaria
def x(t):
    return 
