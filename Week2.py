n= 123
print  ((n-n%10)*100)%10
print 'asdfasd'

import random
print random.randint(0, 10)
print random.randrange(0, 10) 

def fx(x):
    return -5 * x ** 5 + 69 * x ** 2 - 47 
print fx(0)
print fx(1)
print fx(2)
print fx(3)
print 2 ** 4

def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    
    # Put your code here.
    FV = present_value * (1 + rate_per_period) ** periods
    return FV

print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)

print future_value(500, .04, 10, 10)

import math
def polygon(sides_n, length_s):
    return 0.25 * sides_n * (length_s ** 2) / math.tan(math.pi/sides_n)

print polygon(5,7)
print polygon(7,3)

def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b

def max_of_3(a, b, c):
    return max_of_2(a, max_of_2(b, c))

print max_of_3(4,5,6)


def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)    
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale
    
project_to_distance(2, 7, 4)


# Example of a simple event-driven program

# CodeSkulptor GUI module
import simplegui

# Event Handler
Def tick():
    print "tick!"

# Register handler
timer = simplegui.create_timer(1000, tick)

# Start timer
timer.start()

# global vs local examples

# num1 is a global variable

num1 = 1
print num1

# num2 is a local variable

def fun():
    num1 = 2
    num2 = num1 + 1
    print num2
    
fun()


# the scope of global num1 is the whole program, num 1 remains defined
print num1

# the scope of the variable num2 is fun(), num2 is now undefined
# print num2


# why use local variables?
# give a descriptive name to a quantity
# avoid computing something multiple times

def fahren_to_kelvin(fahren):
    celsius = 5.0 / 9 * (fahren - 32)
    zero_celsius_in_kelvin = 273.15
    return celsius + zero_celsius_in_kelvin

print fahren_to_kelvin(212)





# the risk/reward of using global variables

# risk - consider the software system for an airliner
#		critical piece - flight control system
#		non-critical piece - in-flight entertainment system

# both systems might use a variable called "dial"
# we don't want possibility that change the volume on your audio
# causes the plane's flaps to change!



# example
num = 4

def fun1():
    global num
    num = 5
    
def fun2():
    global num
    num = 6

# note that num changes after each call with no obvious explanation    
print num
fun1()
print num
fun2()
print num

# global variables are an easy way for event handlers
# to communicate game information.

# safer method - but they required more sophisticated
# object-programming techniques

