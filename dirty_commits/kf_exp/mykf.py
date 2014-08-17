# Implemening MaKaPREM Filter
from __future__ import division

import numpy as np
import numpy.linalg as lin
from numpy import array, matrix, concatenate
from numpy import linspace, eye

from math import pow, exp
from math import pi

from random import random, randint

import matplotlib.pyplot as plt



# Time duration of Kalman Filter
# Meta variables
duration = 10
dt = 0.1

#### Cofficient Matrices ####
# Defining Update Equations
A = np.array([[1, 0], [0, 1-pow( dt%2 ,-1)]])
# Since input is zero
B = 0 
# c1 is % of crime reported | Estimated from reports
c1 = 0.3 # Only 30% of crimes are reported
C = array([ c1, 0])
## Slope
m = 2

#### Defining Main Variables ###
# Initialization of state : V and N
X = array([[0], [0]])
X_est = X

StateNoiseMag = 0.02
Sigma_ZMag = 0.01  # Assumed 10% of Reports are bogus
Ez = Sigma_ZMag ** 2
Ex = StateNoiseMag # No Control Variable hence random Noise
P = Ex

#### Initialize the result variables ###
# Actual No. of Victims
V_act = array([])
# Actual Age group of victims
N_act = array([])
# No. of Victims estimated
V_meas = array([])


## Simulate 
for t in linspace(0, dt, duration):
    
    # Generate State Noise
    StateNoise = StateNoiseMag * random()
    X = A.dot(X) + StateNoise

    # Generate Measurement Noise
    Sigma_Z = Sigma_ZMag * random()
    Z = C.dot(X) + Sigma_Z
    
    V_act = concatenate((V_act, X[0]), axis=0)
    V_meas = concatenate((V_meas, Z), axis=0)

#Iteratively plot
plt.plot(linspace(0, dt, duration), V_act, '-r')
plt.plot(linspace(0, dt, duration), V_meas, '-k.')
    
#plt.show()

### DO KALMAN FILTERING ###

# Initialize variables Estimation
V_est = array([]) # Estimating victims
N_est = array([]) # Estimating Age years

# Re-init
X = array([[0], [0]])
P_est = P
P_estMag = array([])
predict_state = array([])
predict_var = array([])

for t in range(len(V_act)):
    X_est = A.dot(X_est) + array([m, 0]).T
    predict_state = concatenate((predict_state, X_est[0]), axis=0)

    # Predict Next Covariance
    P = (A.dot(P)).dot(A.T) + Ex
    # Measure covariance
    #predict_var = concatenate((predict_var, P), axis=0)
    
    # Kalman Gain
    K = (P.dot(C.T)).dot( pow( ((C.dot(P)).dot(C.T) + Ez),-1) )

   # print K, V_meas[t] - C.dot(X_est)
    # Update State estimate
    X_est = X_est + K.dot( V_meas[t] - C.dot(X_est))

    # Update Covariance estimation
    P = (eye(2)-(K.dot(C))).dot(P)
    
    # STore for plotting
    V_est = concatenate((V_est, X_est[0]), axis=0)
    N_est = concatenate((N_est, X_est[1]), axis=0)
    P_estMag = concatenate((P_estMag, P[0]), axis=0)

# Plotting
tt  = linspace(0, dt, duration)

print 'State ', X_est

'''
print V_act
print '------------'
print V_meas
print '------------'
print V_est
'''

plt.plot( tt, V_act, '-r.')
plt.plot( tt, V_meas, '-g.')
plt.plot( tt, V_est[:10], '-k.')

plt.show()
