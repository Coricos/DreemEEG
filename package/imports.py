# DINDIN Meryll
# April 17th, 2018
# Dreem Headband Sleep Phases Classification Challenge

# Core packages

import h5py, multiprocessing, tqdm

import numpy as np
import scipy.signal as sg

from functools import partial
from scipy.interpolate import interp1d

from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Graphical imports

try: 
	import matplotlib.pyplot as plt
	import matplotlib.gridspec as gs
except:
	pass