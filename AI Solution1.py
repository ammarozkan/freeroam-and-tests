import numpy as np
import matplotlib.pyplot as plt 
import random

randominv = lambda dist: (random.random()-0.5)*2*dist
randompinv = lambda dist: random.random()*dist

GRFA = lambda arr,dist: [arr[x]+randominv(dist) for x in range(0,len(arr))] # getRandomFromArray

SUM = lambda arr,arr2: [arr[i]+arr2[i] for i in range(0,len(arr))]
DIV = lambda arr, constant : [arr[i]/constant for i in range(0,len(arr))]
MUL = lambda arr,constant : [arr[i]*constant for i in range(0,len(arr))]

def AVR_ARRAYS(arrays):
    mega_array = arrays[0]
    for array in arrays:
        mega_array = SUM(mega_array,array)
    return DIV(mega_array,len(arrays))

def EFFECTED_AVR_ARRAYS(arrays):
    mega_array = arrays[0]
    sum_counts = 0
    for counter in range(0,len(arrays)):
        mega_array = MUL(SUM(mega_array,arrays[counter]),(len(arrays)-counter))
        sum_counts+=(len(arrays)-counter)
    return DIV(mega_array,sum_counts)

# greater is at the end
def order_by_array(array,ordering_base_index):
    ordered = False
    while not ordered:
        ordered = True
        for counter in range(0,len(array)-1):
            if array[len(array)-counter-2][ordering_base_index] > array[len(array)-counter-1][ordering_base_index]:
                ddrd = array[len(array)-counter-2]
                array[len(array)-counter-2] = array[len(array)-counter-1]
                array[len(array)-counter-1] = ddrd
                ordered=False
    return array
def order_by_array2(array,ordering_base_index,extra_array):
    ordered = False
    while not ordered:
        ordered = True
        for counter in range(0,len(array)-1):
            if array[len(array)-counter-2][ordering_base_index] > array[len(array)-counter-1][ordering_base_index]:
                ddrd = array[len(array)-counter-2]
                array[len(array)-counter-2] = array[len(array)-counter-1]
                array[len(array)-counter-1] = ddrd

                
                ddrd_extra = extra_array[len(extra_array)-counter-2]
                extra_array[len(extra_array)-counter-2] = extra_array[len(extra_array)-counter-1]
                extra_array[len(extra_array)-counter-1] = ddrd_extra
                ordered=False
    return array,extra_array

def order_by2(values,extra_array):
    ordered = False
    while not ordered:
        ordered = True
        for counter in range(0,len(values)-1):
            if values[len(values)-counter-2] > values[len(values)-counter-1]:
                ddrd = values[len(values)-counter-2]
                values[len(values)-counter-2] = values[len(values)-counter-1]
                values[len(values)-counter-1] = ddrd

                ddrd_extra = extra_array[len(extra_array)-counter-2]
                extra_array[len(extra_array)-counter-2] = extra_array[len(extra_array)-counter-1]
                extra_array[len(extra_array)-counter-1] = ddrd_extra
                ordered=False
    return values,extra_array

def array_equal(array1,array2,depth):
    result = True
    for counter in range(0,len(array1)):
        if depth>1: result = result and array_equal(array1[counter],array2[counter],depth-1)
        else: result = result and array1[counter] == array2[counter]
    return result

class Function:
    def __init__(self, bc): # power count, base constants
        self.bc = bc
        self.mysuccess = []

    def f(self, x):
        val = 0
        for power in range(0,len(self.bc)):
            val+=self.bc[len(self.bc)-power-1]*(x**power)
        return val
    def fn(self,xmin,xmax,r=1): # numpy range
        val = np.arange(xmin,xmax,r)*0
        for power in range(0,len(self.bc)):
            x = np.arange(xmin,xmax,r)
            val+=self.bc[len(self.bc)-power-1]*(x**power)
        return val
    def plot(self,xmin,xmax,name = "Plot tha' Function",r=0.1):
        x = np.arange(xmin,xmax,r)
        y = self.f(x)

        # Plot the points using matplotlib 
        plt.title(name) 
        plt.plot(x, y) 
        plt.show()
    
    def get_textic(self):
        text = str(self.bc[0])
        for power in range(1,len(self.bc)):
            text = str(self.bc[power])+"x^"+str(power)+" + "+text
        return text

class GeneralManager:
    def __init__(self,dist): # distance constant,
        self.dist = dist
    
    def test_value(self,value):
        for i in range(0,len(self.funcs)):
            print(i,":",self.funcs[i].f(value))
    
    def generatefrombase(self,hmf, bf): # how many functions,  base function
        self.funcs = [Function(GRFA(bf.bc,self.dist)) for x in range(0,hmf)]
    
    def generateanfunctionfrombase(self,fId,fBase):
        self.funcs[fId] = Function(GRFA(fBase.bc,self.dist))
    
    def generateanrandomtoadd(self,max):
        self.funcs.append(Function([randominv(max) for i in range(0,len(self.funcs[0].bc))]))
    
    def generateanfunctionfrombaseconstants(self,fId,fBaseConstant):
        self.funcs[fId] = Function(GRFA(fBaseConstant,self.dist))
    
    def copyanfunctionfrombaseconstants(self,fId,fBaseConstant):
        self.funcs[fId] = Function(fBaseConstant)
    
    def generaterandom(self,hmf, pc,max): # how many functions, power count, maximum constant value
        self.funcs = [ Function([randominv(max) for i in range(0,pc)]) for x in range(0,hmf)]
    
    def getallplot(self,xmin,xmax,r=0.1):
        for c in range(0,len(self.funcs)):
            print(str(c)+":"+self.funcs[c].get_textic())
            self.funcs[c].plot(xmin,xmax,str(c),r=r)
    
    def getPoints(self,requiredValues): # required values -> [[x,y],[x,y],[x,y]]
        points = [0 for x in range(0,len(self.funcs))]
        for i in range(0,len(self.funcs)):
            for j in range(0,len(requiredValues)):
                points[i] = abs(self.funcs[i].f(requiredValues[j][0])-requiredValues[j][1])
        return points
    
    def getOrderedPoints(self,points):
        points, func_ids = order_by2(points,[c for c in range(0,len(self.funcs))])
        return [[func_ids[i],points[i]] for i in range(0,len(points))]
    
    def removeWorst(self,points,removing_last_counts, avr_first_best):
        points, func_ids = order_by2(points,[c for c in range(0,len(self.funcs))])
        avr_best = AVR_ARRAYS([self.funcs[func_ids[i]].bc for i in range(0,avr_first_best)])
        for i in range(0,removing_last_counts):
            self.generateanfunctionfrombaseconstants(func_ids[len(func_ids)-1-i],avr_best)
    
    def changeAll(self,points):
        points, func_ids = order_by2(points,[c for c in range(0,len(self.funcs))])
        for i in range(1,len(func_ids)):
            constants = EFFECTED_AVR_ARRAYS([ self.funcs[func_ids[j]].bc for j in range(0,i)])
            self.copyanfunctionfrombaseconstants(func_ids[i],constants)

    



if __name__ == "__main__":
    trueVals = [[20.72,0],[20.54,0],[20.44,100],[20.48,60],[20.23,0],[20.24,0],[20.16,0],[20.11,100]]
    gm = GeneralManager(5)
    gm.generaterandom(15,20,10)
    counter = 0
    control_range = 10000
    gen_function_range = 10000
    pre_bests = gm.getOrderedPoints(trueVals)[0:3]
    Xcalculation, Ypoint = [],[]
    Xfuncs,Yfuncs = [[] for i in range(0,len(gm.funcs))],[[] for i in range(0,len(gm.funcs))]
    while True:
        print("calculation for "+str(len(gm.funcs))+" function:"+str(counter%control_range)+",",*gm.getOrderedPoints(gm.getPoints(trueVals))[0:3],sep='\t')
        gm.removeWorst(gm.getPoints(trueVals),2,3)
        if counter % gen_function_range == 0:
            if array_equal(pre_bests,gm.getOrderedPoints(gm.getPoints(trueVals))[0:3],2): 
                gm.changeAll(gm.getPoints(trueVals))
                #gm.generateanrandomtoadd(5)
            pre_bests = gm.getOrderedPoints(gm.getPoints(trueVals))[0:3]
        if counter % control_range == 0: 
            input_text = "a"
            while input_text != "":
                input_text = input("gmsmthng:")
                if input_text == "control_range": control_range = int(input("control_range:"))
                elif input_text == "gen_function_range": gen_function_range = int(input("control_range:"))
                elif input_text == "show_me": 
                    vals = input("xmin xmax r:").split(" ")
                    vals = [float(vals[i]) for i in range(0,len(vals))]
                    gm.getallplot(vals[0],vals[1],vals[2])
                elif input_text == "test_function":
                    while True:
                        input_text = input("value:")

                        testICall = input_text.split(".")
                        if len(testICall) and testICall[0].isnumeric() and testICall[1].isnumeric():gm.test_value(float(input_text))
                        else:
                            break ; continue
                elif input_text == "XYGraph":
                    plt.title("calculation_point graph")
                    plt.plot(Xcalculation,Ypoint,color="black")
                    plt.show()
                elif input_text == "success":
                    for i in range(0,len(gm.funcs)):
                        plt.title(""+str(i)+"th function's calculation_point graph")
                        plt.plot(Xcalculation,Ypoint,color="black")
                        plt.show()

        Xcalculation.append(counter)
        Ypoint.append(gm.getOrderedPoints(gm.getPoints(trueVals))[0][1])
        for i in range(0,len(gm.funcs)):
            Xfuncs = counter
            Yfuncs[i].append(gm.getPoints(trueVals)[i])
                        
                        
        counter+=1


