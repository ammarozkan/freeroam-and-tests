import matplotlib.pyplot as plt
import numpy as np


def factoriel(x):
    if int(x) >= 1:
        return factoriel(int(x)-1)*int(x)
    else:
        return 1

def dFunction(x,a=-1,k=1):
    if a == -1: a = int(x/0.36)
    result = 0
    for n in range(0,a):
        result += ((x**n)*k)/factoriel(n)
    return result


def test(forx,toa = 5,k=1):
    xs = []
    ys = []
    fig, ax = plt.subplots()
    for i in range(0,toa):
        print(forx,":by ",i,":",dFunction(forx,i,k))
        xs.append(i)
        ys.append(dFunction(forx,i,k))

    ax.plot(xs, ys, linewidth=2.0)

    plt.show()


xs = []
ys = []
xs2 = []
ys2 = []

plt.style.use('_mpl-gallery')

dividition = 0.5
maxVal = 60.5
print(maxVal/dividition)
for n in range(0,int(maxVal/dividition)):
    print(n*dividition,":",dFunction(n*dividition))
    xs.append(n*dividition)
    ys.append(dFunction(n*dividition))

# plot
fig, ax = plt.subplots()

ax.plot(xs, ys, linewidth=2.0)

print(maxVal/dividition)
for n in range(0,int(maxVal/dividition)):
    print(n*dividition,":",dFunction(n*dividition,a=60))
    xs2.append(n*dividition)
    ys2.append(dFunction(n*dividition,a=60))

# plot
fig2, ax2 = plt.subplots()

ax2.plot(xs2, ys2, linewidth=2.0)
plt.show()