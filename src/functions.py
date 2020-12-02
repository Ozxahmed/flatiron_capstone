import pandas as pd
from statsmodels.tsa.stattools import adfuller

def i_n(series):
    i = 0
    dftest = adfuller(np.diff(series,i), autolag='AIC')
    test_stat = dftest[0]
    critical_val_5 = dftest[4]['5%']
    while test_stat > critical_val_5:
        i+=1
        dftest = adfuller(np.diff(series,i), autolag='AIC')
        test_stat = dftest[0]
        critical_val_5 = dftest[4]['5%']
    return(i)