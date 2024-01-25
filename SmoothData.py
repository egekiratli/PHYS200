# Student ID  : 2555258
# Project Name: Smooth Data
# Project ID  : S-GEN-SmoothData
# Description : This code calculates moving average for N neighboring points,
# resulting in a smoothed plot of a noisy data.


import math as m
import random as r
import matplotlib.pyplot as plt

#DATA SET
l = 100
x = [ i for i in range(l)]
y = [ i/2 + r.randint(-5,5) for i in x] #make a noisy function

#MOVING AVERAGE FUNCTION
def moving_average(N):
  ylist = list(y)
  ysmooth = []
  yavg = 0
  for i in range(N,len(y)-N):                       #using quotient makes the
      ysmooth.append(sum(ylist[i-N//2:i+N//2+1])/N) #code work with both pair &
  return ysmooth                                    #nonpair numbers

#CHI SQUARE TEST FUNCTION
def chi_square():
  ytest = moving_average(N)
  exp = [i/2 for i in x]
  exp_test = exp[N:len(y)-N]
  chi2 = 0
  for i in range(len(exp_test)):
    if exp_test[i] == 0:
      exp_test[i] += 1                    #preventing float division by zero
      chi2 += (ytest[i]-exp_test[i])**2/exp_test[i] #chi-square formula
    else:
      chi2 += (ytest[i]-exp_test[i])**2/exp_test[i]
  return chi2

N = 5
ys = moving_average(N)
chi_val = chi_square()
print('Chi square value:',chi_val)

#PLOTTING PART
plt.plot(x,y, 'b-', markersize = 2)               #I've found it meaningless to
plt.plot(x[N:len(y)-N],ys, 'r-', markersize = 2)  #include end points since they wouldn't be
plt.legend(['Original Data','Moving Average'])    #calculated with moving average