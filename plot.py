
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import matplotlib.animation as animation
import time

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    f=open("data.csv","r")
    ignore=f.readline()
    pullData = f.read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            _all = eachLine.split(',')
            x,y=_all[1],_all[3]
            xar.append(x)
            yar.append(y)
    ax1.clear()
    ax1.plot(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
fig.savefig("test.png")

