
import random

# condition [v1,v2,c]
    # c == 0: should be equal, c == 1: v1 should greater than v2, c == 2: v1 should be greater or equal, (c == 3: v1 can divided by v2?)

def reselectInCondition(vars,dA):
    nonchange = 0
    for condition in dA["condition"]:
        if condition[2] == 0 and not vars[condition[0]] == vars[condition[1]]: vars[condition[0]] = vars[condition[1]]
        elif condition[2] == 1 and not vars[condition[0]] > vars[condition[1]]: vars[condition[0]] = random.randrange(vars[condition[1]],dA["vars"][condition[0]]["val"][1])
        elif condition[2] == 2 and not vars[condition[0]] >= vars[condition[1]]: vars[condition[0]] = random.randrange(vars[condition[1]]-1,dA["vars"][condition[0]]["val"][1])
        else: nonchange += 1
    print(len(dA["condition"]),"???",nonchange)
    return vars, nonchange==len(dA["condition"])
            
        

def selector(dA):
    result = {}
    for var in dA["vars"]:
        result[var] = random.randrange(dA["vars"][var]["val"][0],dA["vars"][var]["val"][1])
    condt = False
    while not condt:
        result, condt = reselectInCondition(result,dA)
        print(result)
    return result
    


a = {
    "vars":{
        "t":{"val":[0,10]},
        "a":{"val":[0,20]},
        "b":{"val":[0,150]}
        },
    "condition":[["a","t",0],["b","a",1],["t","a",2]]
    }

print(selector(a))