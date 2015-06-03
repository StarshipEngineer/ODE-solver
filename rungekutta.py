# this is a numerical ODE solver based on the 4th-order Runge-Kutta
# method, capable of solving with good precision 1st-order ODEs of
# form y'(x)+p(x)y(x)=q(x)

# Function definitions for the functions appearing in dy/dx,
# and a function for calculating dy/dx

def q(x):
    q = 0 # enter the functional form of the inhomogeneity
    return q

def p(x):
    p = 0 # enter the functional form of the coefficient of y(x)
    return p

def f(x, y):
    f = q(x) - p(x) * y # f(x,y) = dy/dx
    return f

x_0 = float(input("Initial value of x = ")) # initial value of x
y_0 = float(input("Initial value of y = ")) # initial value of y
delta_x = float(input("Step size = ")) # step size
n_max = float(input("Number of steps = ")) # number of steps desired

x_list = [] # A list for storing independent variable values
y_list = [] # A list for storing dependent variable values

# Set initial conditions
x_n = x_0
y_n = y_0
x_list.append(x_n) # adds first value of x to storage
y_list.append(y_n) # ditto y
n = 0 # initializes step-counting variable at 0

while n < n_max:
    k_1 = f(x_n,y_n) * delta_x
    k_2 = f(x_n + delta_x / 2, y_n + k_1 / 2) * delta_x
    k_3 = f(x_n + delta_x / 2, y_n + k_2 / 2) * delta_x
    k_4 = f(x_n, y_n + k_3) * delta_x
    y_n += (1 / 6) * (k_1 + 2 * k_2 + 2 * k_3 + k_4)
    x_n += delta_x
    x_list.append(x_n)
    y_list.append(y_n)
    n += 1

output = open("output.csv", "w")
for a, b in zip(x_list, y_list):
    output.write(str(round(a, 3)) + ", " + str(round(b, 3)) + "\n")
output.close()
