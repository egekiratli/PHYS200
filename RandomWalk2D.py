# Student ID  : 2555258
# Project Name: Random Walk 2D
# Project ID  : S-GEN-RandomWalk2D
# Description : This code generates a 2D randomwalk function in which average &
# rms values of each number of walks (K) is computed. As it is seen from the graphs,
# average distance converges to square root of number of steps (N) which is
# the most likely path


import math as m
import random as r
import matplotlib.pyplot as plt

def randomwalk(steps):
  rwx = 0
  rwy = 0
  rwc = 0
  for i in range(steps):
    R = r.randint(1,4)
    if R == 1:
      rwx -= 1
    elif R == 2:
      rwy -= 1
    elif R == 3:
      rwx += 1
    else:
      rwy += 1
  rwc = [rwx,rwy]
  return rwc


def multirun(walkers):
  c = []
  d = []
  for j in range(walkers):
    c.append(randomwalk(steps))
  for i in c:
    d.append(m.sqrt(i[0]**2+i[1]**2))
  return d

def getRMS():  #calculate RMS value for each distance walked by each K walker
  rms = []
  for i in range(walkers):
    val_rms = []
    dret = multirun(i+1)
    for d in dret:
      val_rms.append(d**2/(i+1))
    rms.append(m.sqrt(sum(val_rms)))
  return rms

def getAVG(): #calculate average value for each distance walked by each K walker
  avg = []
  for i in range(walkers):
    val_avg = []
    dret = multirun(i+1)
    for d in dret:
      val_avg.append(sum(dret)/(i+1))
    avg.append(sum(val_avg)/len(val_avg))
  return avg

steps = 100
walkers = 100

ret_avg = getAVG()
ret_rms = getRMS()
ret_walks = [i for i in range(walkers)]
ret_d = multirun(walkers)
sqrtN = [m.sqrt(steps) for i in range(walkers)]


#PLOTTING
  #WALKERS PLOT
plt.subplot(2,1,1)
plt.scatter(ret_walks,ret_d, c = 'r', s = 2)
plt.xlabel('Number of Walks')
plt.ylabel('Distance Traveled')
plt.legend(['Distance'])
  #RMS, AVG, SQRT(N) PLOT
plt.subplot(2,1,2)
plt.plot(ret_walks,ret_rms, 'c-', markersize = .2,)
plt.plot(ret_walks,ret_avg,'m-')
plt.plot(ret_walks,sqrtN, 'g--')
plt.xlabel('Number of Walks')
plt.ylabel('Average Distance traveled')
plt.legend(['RMS','Average','sqrt(N)'])

plt.subplots_adjust(hspace = 0.4) #adjusting the plots so that the xlabel of
plt.show()                        #the first plot can be seen