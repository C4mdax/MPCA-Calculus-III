from sympy import symbols, cos, sin, cosh, tanh, sech, pi
from sympy.plotting import plot_parametric

# Definir la variable simbólica
t = symbols('t')
radio = 1

def plot(x, y, interval):
    return plot_parametric(x, y, interval, show=False, line_color="black", aspect_ratio=(1,1))

def plot_involute(x, y, interval):
    return plot_parametric(x, y, interval, show=False, line_color="red", aspect_ratio=(1,1))

# Curva 1: Círculo
def x_circle(t):
    return radio * cos(t)

def y_circle(t):
    return radio * sin(t)

def x_involute_circle(t):
    return radio * (cos(t) + t * sin(t))

def y_involute_circle(t):
    return radio * (sin(t) - t * cos(t))

circle = plot(x_circle(t), y_circle(t), (t, -pi, pi))
circle_involute = plot_involute(x_involute_circle(t), y_involute_circle(t), (t, 0, 4*pi))
circle.extend(circle_involute)
circle.show() 

# Curva 2: Catenaria
def x_catenaria(t):
    return t

def y_catenaria(t):
    return cosh(t)

def x_involute_catenaria(t):
    return t - tanh(t)

def y_involute_catenaria(t):
    return sech(t)

catenaria = plot(x_catenaria(t), y_catenaria(t), (t, -pi, pi))
catenaria_involute = plot_involute(x_involute_catenaria(t), y_involute_catenaria(t), (t, -5, 5))
catenaria.extend(catenaria_involute)
catenaria.show()

# Curva 3: Deltoid
def x_deltoid(t):
    return (1/3) * (2 * cos(t) - cos(2*t))

def y_deltoid(t):
    return (1/3) * (2 * sin(t) - sin(2*t))

def x_involute_deltoid(t):
    return (1/9) * (2 * cos(t) - cos(2*t))

def y_involute_deltoid(t):
    return (1/9) * (2 * sin(t) + sin(2*t))

deltoid = plot(x_deltoid(t), y_deltoid(t), (t, -pi, pi))
deltoid_involute = plot_involute(x_involute_deltoid(t), y_involute_deltoid(t), (t, -pi, pi))
deltoid.extend(deltoid_involute)
deltoid.show()

# Curva 4: Astroid
def x_astroid(t):
    return cos(t) * cos(t) * cos(t)
def y_astroid(t):
    return sin(t) * sin(t) * sin(t)
def x_involute_astroid(t):
    return (1/8) * (3*cos(t)-(cos(3*t)))
def y_involute_astroid(t):
    return (1/8) * (3*sin(t)+(sin(3*t)))
astroid = plot(x_astroid(t), y_astroid(t), (t,-pi,pi))
astroid_involute = plot_involute(x_involute_astroid(t), y_involute_astroid(t), (t,-pi,pi))
astroid.extend(astroid_involute)
astroid.show()

# Curva 5: Cicloid
def x_cicloid(t):
    return radio * (t-sin(t))
def y_cicloid(t):
    return radio * (1-cos(t))
def x_involute_cicloid(t):
    return radio * (t+sin(t))
def y_involute_cicloid(t):
    return radio * (3 + cos(t))

cicloid = plot(x_cicloid(t), y_cicloid(t), (t,-4*pi,4*pi))
cicloid_involute = plot_involute(x_involute_cicloid(t), y_involute_cicloid(t), (t, -4*pi, 4*pi))
cicloid.extend(cicloid_involute)
cicloid.show()
