import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, colormaps
from matplotlib.animation import FuncAnimation
import random

TorusRes=300

pointNum = 50

R,r = 2,1 #radi of the torus


AnimationNormalization = 1/1000 #speed of animation - less is slower and more accurate.
dx = 1/1000000  #used to calculate derivative - less is more accurate.

GradMode = True #if this is on, HamFlow uses the function GradH for the gradient of H which should be written directly, otherwise estimates the gradient automatically.

# Hamiltonian
def H(q,p):
    return np.sin(2*np.pi * p) + np.cos( 2*np. pi * q)

def GradH(q,p):
    return -AnimationNormalization*2*np.pi * np.sin(2*np.pi * q), AnimationNormalization    *2*np.pi * np.cos(2*np.pi * p)
def Hamflow(q,p):
    if(GradH):
        dHdq,dHdp = GradH(q,p)
    else:
        dHdq = AnimationNormalization*(H(q+dx,p) - H(q,p))/dx
        dHdp = AnimationNormalization*(H(q,p+dx) - H(q,p))/dx
    return q+dHdp,p-dHdq
def xyz(q,p):
    return (R + r*np.cos(2*np.pi*q)) * np.cos(2*np.pi*p), (R + r*np.cos(2*np.pi*q)) * np.sin(2*np.pi*p),r * np.sin(2*np.pi*q) 




# Coordinates for the torus
qLocPlot =np.linspace(0, 1, TorusRes)
pLocPlot =np.linspace(0, 1, TorusRes)
qLocPlot, pLocPlot = np.meshgrid(qLocPlot, pLocPlot)
xPlot,yPlot,zPlot = (R + r*np.cos(2*np.pi*qLocPlot)) * np.cos(2*np.pi*pLocPlot), (R + r*np.cos(2*np.pi*qLocPlot)) * np.sin(2*np.pi*pLocPlot),r * np.sin(2*np.pi*qLocPlot)


fig = plt.figure(figsize=(4, 4))
pointsObj = [0]*pointNum
ax1 = plt.axes(projection='3d',computed_zorder=False)
points = []

# Define initial points randomly
for i in range(pointNum):
    point = {
        "q": random.uniform(0,1),
        "p": random.uniform(0,1),
        "color": colormaps["hsv"](i/pointNum)
    }
    points.append(point)

def init():
    # plot the torus
    ax1.set_box_aspect((1, 1, 1))
    f=2.1
    ax1.set_xlim3d(-f,f)
    ax1.set_ylim3d(-f,f)
    ax1.set_zlim3d(-f,f)

    ax1.view_init(36, 36)
    sf = ax1.plot_surface(xPlot, yPlot, zPlot, rstride=15, cstride=15, cmap=cm.winter, edgecolors='w',alpha = 0.7)
    ax1.set_axis_off()

    # plot the points    
    for i in range(pointNum):
        x,y,z = xyz(points[i]["q"],points[i]["p"])
        pointsObj[i] = ax1.plot(x,y,z,markerfacecolor=points[i]["color"], markeredgecolor='k', marker='o', markersize=5, alpha=1)
    
 

def update(frame):
    for i in range(pointNum):
        pointsObj[i][0].remove() #remove old points

        newq,newp = Hamflow(points[i]["q"],points[i]["p"])
        points[i]["q"],points[i]["p"]=newq,newp
        x,y,z = xyz(points[i]["q"],points[i]["p"])
        pointsObj[i] = ax1.plot(x,y,z,markerfacecolor=points[i]["color"], markeredgecolor='k', marker='o', markersize=5, alpha=1)
        # add points with adjusted coords. 

    # print(H(points[0]["q"],points[0]["p"]))
    return pointsObj

ani = FuncAnimation(fig, update,init_func=init, interval=20)
plt.show()