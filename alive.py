class creature:
    def __init__(self,aliveness = 1):
        self.aliveness = aliveness

def getFunction(gen):
    gen = gen.split('x')
    gen[1] = int(gen[1])
    return gen

def getGenom(genom):
    return [getFunction(genom[x]) for x in range(len(genom))]

class dp:
    def func(self,c):
        if self.g[0] == "A":
            c.aliveness -= self.g[1]
    
    def __init__(self,gen):
        self.g = getFunction(gen)
        



genom = ["Ax13","Bx9"]



print(getGenom(genom))
