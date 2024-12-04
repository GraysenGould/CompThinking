import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy.stats as stats

def residual_plot(actual, pred):
    #Calculate residual
    residual = actual -  pred
    fig, ax = plt.subplots(2,2,figsize=(10,10))
    
    #plot residual vs order plot
    ax[0,0].plot(actual.index,residual,'o')
    ax[0,0].axhline(y = 0, color ='r', linestyle="--")
    ax[0,0].set_xlabel(actual.name)
    ax[0,0].set_ylabel("Residual")
    ax[0,0].set_title('Residual vs Order Plot')
    
    #residual vs predictor plot
    ax[0,1].plot(pred,residual,'o')
    ax[0,1].axhline(y = 0, color ='r', linestyle="--")
    ax[0,1].set_xlabel(actual.name)
    ax[0,1].set_ylabel("Residual")
    ax[0,1].set_title('Residual vs Predictor Plot')
    
    #check for normality 1
    sm.qqplot(pred, stats.t, fit=True, line="45",ax=ax[1,0])
    ax[1,0].set_title("Check for Normality with QQplot");

    #check for normality 2
    ax[1,1].hist(residual)
    ax[1,1].set_xlabel("residual")
    ax[1,1].set_ylabel("count")
    ax[1,1].set_title("Check for Normality with Histogram");
    
    #Residual vs new predictor plot
    #ax[1,1].plot(newvar,residual,'o')
    #ax[1,1].axhline(y = 0, color ='r', linestyle="--")
    #ax[1,1].set_xlabel(newvar.name)
    #ax[1,1].set_ylabel("Residual")
    #ax[1,1].set_title('Residual vs New Predictor Plot')

    return