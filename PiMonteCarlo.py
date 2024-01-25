# Student ID  : 2555258
# Project Name: Pi Monte Carlo
# Project ID  : S-PiMonteCarlo
# Description : This code approximates pi by placing random points in an 1x1 square
# & deciding which ones are in and out of the quarter circle in that square. Ratio of
# points in and out are equated to the ratio of areas (circle and square), hence pi is computed.

import math as m
import random as rnd
import matplotlib.pyplot as plt

Ndots = int(input('Enter # of dots:'))

#QUARTER CIRCLE
r = 1
x = []
y = []
ang = 0
for i in range(100):
  ang += m.pi/200
  x.append(r*m.cos(ang))
  y.append(r*m.sin(ang))

#DOTS INSIDE & OUTSIDE OF THE QUARTER CIRCLE
def invsout(Ndots):
  dots = [[rnd.random(),rnd.random()] for i in range(Ndots)]
  idotx = []
  idoty = [] #empty arrays specified by inside vs outside dots &
  odotx = [] #their x and y coordinates
  odoty = []
  ci = 0
  co = 0

  for i in dots:
    dist = m.sqrt(i[0]**2 + i[1]**2) #distance between the point and the circle
    if dist <= r:
      ci += 1 #inside dot counter
      idotx.append(i[0])
      idoty.append(i[1])
    else:
      co += 1 #outside dot counter
      odotx.append(i[0])
      odoty.append(i[1])

  pi = 4*ci/(ci+co) #calculation of pi with respect to the ratio of points
                    #inside to total points which is equal to the ratio of the
                    #area of the quarter circle to total area
  return idotx, idoty, odotx, odoty, pi



#PI PERCENT ERROR CALCULATOR
def percent_error():
  num_err = [i for i in range(1,Ndots+1)]
  percent_err = []
  for i in num_err:
    if i%10 == 0: #calculating for each 10 steps for sake of simplicity
      ix, iy, ox, oy, pi_err = invsout(i)   #calling the function for extracting
                                            #calculated pi for i number of dots
      percent_err.append(abs(pi_err-m.pi)/m.pi*100) #percent error
  return num_err[0::10], percent_err

#PLOTTING PART
  #DOTS & QUARTER CIRCLE PLOT
ix, iy, ox, oy, pi = invsout(Ndots)
plt.subplot(2,1,1)
plt.plot(x,y, 'k')
plt.scatter(ix,iy, s = 3, c='b')
plt.scatter(ox,oy, s = 3, c='r', marker = '^')
plt.legend(['Quarter Circle','Points Inside','Points Inside'])
plt.xlim(0.0,1.0)
plt.ylim(0.0,1.0)

  #PERCENT ERROR PLOT
plt.subplot(2,1,2)
ret_num_err , ret_percent_er = percent_error()
plt.plot(ret_num_err , ret_percent_er, c='g', markersize = .25)
plt.ylim(0)
plt.ylabel('% error')
plt.xlabel('Number of Points')

print('pi =', pi)
plt.show()