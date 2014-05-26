
# My implementation of RBF cannot match speed and goodness
# of in-built C libraries of scipy

from __future__ import division
from scipy.interpolate import Rbf

def train_rbf( x, y):
	return Rbf(x,y)

def calc_val(Rbf_obj, val):
	return Rbf_obj(val)

