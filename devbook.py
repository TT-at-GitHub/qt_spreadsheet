#In[0]
import os, sys
from random import randint
import random
import string
from PySide2.QtWidgets import QApplication
from PySide2 import QtWidgets, QtCore, QtGui
from numpy.core.fromnumeric import repeat
from numpy.core.memmap import memmap

from enum import auto

from pandas._libs.tslibs import Timestamp
from six import Iterator

from qspreadsheet import *
from datetime import datetime, timedelta, time as dtime
import time
from typing import Any, DefaultDict, Dict
import numpy as np
from numpy.core.defchararray import center, upper 
import pandas as pd
import string
import random
import collections
from IPython.display import display
pd.options.display.max_rows = 10
pd.options.display.max_columns = 15
pd.options.display.float_format = '{:,.2f}'.format

def rnd_txt(num_letters): return "".join(
    [random.choice(string.ascii_letters[:26]) for i in range(num_letters)])

#In[0]
num_rows = 10
df = pd.DataFrame(np.random.randn(num_rows,3))
df
#In[0]
rand_lines = [rnd_txt(3) for i in range(num_rows)]
df['B'] = rand_lines
df['C'] = pd.Timestamp('20130101')
df['C'] = df['C'].apply(lambda x: x + timedelta(days=randint(-30000, 30000)))
df.columns = df.columns.astype(str)
#In[0]
df.B[::2] = df.B[::2].apply(str.upper)
df
#In[0]
df.B[::2] = df.B[1::2]
df
#In[0]
df.C[:] = df.C.sort_values()
df
#In[0]
df.to_pickle('.ignore/data/{}rows.pkl'.format(num_rows))
#In[0]
df.to_excel('.ignore/data/{}rows.xlsx'.format(num_rows))
#In[0]
df = pd.read_pickle('.ignore/data/{}rows.pkl'.format(num_rows))
df = pd.DataFrame(df)
df
#In[0]
df.loc[4, 'B'] = df.loc[3, 'B']
df.loc[8, 'B'] = df.loc[3, 'B']
df.loc[4, '0'] = df.loc[3, '0']
df.loc[8, '0'] = df.loc[3, '0']
df.loc[4, '2'] = df.loc[3, '2']
df.loc[8, '2'] = df.loc[3, '2']
