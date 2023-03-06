import numpy

def avarage(array):
    sum = 0
    for arr in array:
        sum+=arr
    return sum/len(array)

def standart_deviation(array):
    avr = avarage(array)
    array = numpy.power(array-avr,2)
    return numpy.sqrt(avarage(array))

def deviation(array):
    d = standart_deviation(array)
    print(d)
    return d*array

def connected_bubble_sort(baseArray,*connected):
    for i in range(len(baseArray)):
        #print("SORT:",i)
        for j in range(0,len(baseArray)-i-1):
            if baseArray[j] > baseArray[j+1]:
                temp = baseArray[j]
                baseArray[j] = baseArray[j+1]
                baseArray[j+1] = temp
                
                for x in range(0,len(connected)):
                    temp = connected[x][j]
                    connected[x][j] = connected[x][j+1]
                    connected[x][j+1] = temp
    return (baseArray,)+tuple(connected)

import random
personCount = 1500
myman = [29.5,16.75,21.50,17.75,616161]
maxpoint = 550
tr1 = numpy.array([random.randint(15,40) for x in range(0,personCount)]+[myman[0]])
mat1 = numpy.array([random.randint(10,40) for x in range(0,personCount)]+[myman[1]])
sos1 = numpy.array([random.randint(12,20) for x in range(0,personCount)]+[myman[2]])
fen1 = numpy.array([random.randint(6,20) for x in range(0,personCount)]+[myman[3]])
ids = numpy.array([random.randint(0,99999999999) for x in range(0,personCount)]+[myman[4]])

dev_tr1 = standart_deviation(tr1)
dev_mat1 = standart_deviation(mat1)
dev_sos1 = standart_deviation(sos1)
dev_fen1 = standart_deviation(fen1)

std_ar_tr1 = dev_tr1*tr1
std_ar_mat1 = dev_mat1*mat1
std_ar_sos1 = dev_sos1*sos1
std_ar_fen1 = dev_fen1*fen1
#print(*list(ar),*list(std_ar),sep="\t")
top_d = maxpoint*(std_ar_mat1+std_ar_tr1+std_ar_sos1+std_ar_fen1)/max(std_ar_mat1+std_ar_tr1+std_ar_sos1+std_ar_fen1)
top = tr1+mat1+sos1+fen1

top_d,std_ar_tr1,std_ar_mat1,std_ar_sos1,top,tr1,mat1,sos1,fen1,ids = connected_bubble_sort(top_d,std_ar_tr1,std_ar_mat1,std_ar_sos1,top,tr1,mat1,sos1,fen1,ids)

for j in range(0,len(tr1)):
    i = j
    print(str(len(tr1)-i)+"th ID:"+str(ids[i]),"tr1:"+str(tr1[i]),"mat1:"+str(mat1[i]),"sos1:"+str(sos1[i]),"fen1:"+str(fen1[i]),"topd:"+str(top_d[i]),"top:"+str(top[i]),sep="\t\t\t\t")

print("tr1:",dev_tr1," mat1:",dev_mat1," sos1:",dev_sos1," fen1:",dev_fen1)
manindex = list(ids).index(616161)
print("Your Man:",len(ids)-manindex," with point of:",top_d[manindex])
guess = 1000000
print("In ",guess," man your man would be in: (",int(guess*((len(ids)-manindex-1)/personCount)),",",int(guess*((len(ids)-manindex)/personCount)),") range.")
