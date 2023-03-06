import math

def x2(x):
    return -x**2

length = lambda dot : math.sqrt(dot[0]**2+dot[1]**2)

def getAngle(dot):
    length = math.sqrt(dot[0]**2+dot[1]**2)
    angle = math.acos(dot[0]/length) if math.asin(dot[1]/length) >= 0 else math.pi+(math.pi-math.acos(dot[0]/length))
    return angle

def dotByAngle(length,angle):
    return [length*math.cos(angle),length*math.sin(angle)]

def rotX2(x):
    dot = [x,x2(x)]
    return dotByAngle(length(dot),getAngle(dot)+math.pi/2)

def rootSquare(x):
    return math.log(x)+x*0.05

print(rotX2(64))