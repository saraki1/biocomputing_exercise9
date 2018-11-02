#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 10:43:28 2018

@author: stephaniearaki
"""

#####################Exercise 9#############################

#Question1: find data, put in txt file, and write a script that produces a scatter plot with trend line


#Question2: given data.txt write a script that generates two figures that summarize the data
import pandas as pd
import numpy as np
from plotnine import *

data=pd.read_csv('data.txt',sep=',',header=0)

#barplot of means of 4 populations
a=ggplot(data,aes(x='region',y='observations'))+theme_classic()+xlab('Region')+ylab('Mean Observations')
a+geom_bar(stat='summary',fun_y=np.mean

#scatter plot of all observations
b=ggplot(data,aes(x='region',y='observations'))+theme_classic()+xlab('Region')+ylab('Observations')
b+geom_jitter()

#Do bar and scatter plot tell different stories? 