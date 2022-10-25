import numpy as np 
import pandas as pd 

serie = pd.Series(np.random.random(7), name = 'coluna 01')
serie
serie[5]
from pandas_datareader import data as wb
PETR4 = wb.DataReader('PETRA.SA', data_source = 'yahoo', start='2010-1-1')
PETR4