# Student ID  : 2555258
# Project Name: Guiding Center 2D
# Project ID  : S-MET-GuidingCenter2D
# Description : This code animates the guiding center motion for an electron in
#plasma.

# Note: Gyroradius (Larmor radius) gets larger as the animation continues.
# It should be constant according to the formula. However, the computation of the
# drift seems to be correct. Since I don't know the physics of it, I leaved it as it is.

import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML


m = 1 #mass
q = 1 #charge

E = [0,-1,0] #E field
B = [0,0,3] #B field
p0 = [0,0] #initial position
v0 = [0,-1,0] #initial velocity

gyro_f = abs(q)*math.sqrt(B[0]**2+B[1]**2+B[2]**2)/m #Gyrofrequency
gyro_r = abs(v0[1])/gyro_f                           #Larmor Radius


v = v0
p = p0

def lorentz(B,E,v):
  F = []
  F.append(q*(E[0]+ v[1]*B[2]-v[2]*B[1]))
  F.append(q*(E[1]+ v[2]*B[0]-v[0]*B[2])) #calculation of Lorentz force
  F.append(q*(E[2]+ v[0]*B[1]-v[1]*B[0])) # F = q*(E + vxB)
  return F


def guido_center(v,p):
  t = 0
  dt = .01
  px = []
  py = []
  while t <= 10:
      px.append(p[0])
      py.append(p[1])

      #get the Lorentz force
      F = lorentz(B,E,v)

      #update the velocity
      # v(t+delt) = v(t) + F(t)/m*dt
      v[0] += F[0]/m*dt
      v[1] += F[1]/m*dt

      #update the position
      p[0] += v[0]*dt
      p[1] += v[1]*dt

      t += dt
  return px,py

px, py = guido_center(v,p)

fig, ax = plt.subplots()
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)

trajectory, = ax.plot([],[],'b-') #returns a empty plot for initial animation
center, = ax.plot([],[],'r-')

def animation(frame):
  py0 = [0 for i in range(len(px))]
  trajectory.set_data(px[:frame],py[:frame]) #animation of trajectory
  center.set_data(px[:frame],py0[:frame]) #animation of guiding center
  return trajectory, center



animation = FuncAnimation(fig, animation, frames = 1000, interval = 20, blit = True)
plt.close()
HTML(animation.to_html5_video())