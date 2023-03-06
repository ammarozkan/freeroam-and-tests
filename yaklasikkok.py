import math # for difference testing
import functools

def moreGreaterMoreLower(number,m,n):
    x = 0
    val = ((x+m)/(x+n))*x

@cache
def algoritmicSqrt(number):
    counter = 0
    while counter**2 < number: # we just need 2 square number that comes before and after from our value
        counter+=1
    
    low,up = counter-1,counter
    diff = (number-low**2)
    return (low + diff / (up**2-low**2))*(1/diff)
                                    # logic in that :   difference between low(square number that comes before from our value) and the value(number) original will be more effective if difference 
                                    #                   between up(square number that comes after from our value) and low is "low". But if difference between up and low is not low, and goes greater when 
                                    #                   value goes greater, value(number) will be more uneffective. So when you do a ratio like diff/(up**2-low**2) and add to lower square number value, 
                                    #                   that will be logical.


if "__main__" == __name__:
    while True:
        val = int(input(":"))
        s = algoritmicSqrt(val)
        if val >= 0: m = math.sqrt(val)
        print("sqrtWithoutSqrt:",s)
        if m : 
            print("math.sqrt:",m)
            print("difference:",abs(s-m))