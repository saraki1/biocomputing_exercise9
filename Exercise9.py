#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 10:43:28 2018

@author: stephaniearaki
"""

#####################Exercise 9#############################

###Question1: find data, put in txt file, and write a script that produces a scatter plot with trend line
import pandas as pd
import numpy as np
from plotnine import *

gpa=pd.read_csv('GPA.txt',sep=',',header=0)
c=ggplot(gpa,aes(x='CREDITS',y='GPA'))+theme_classic()+xlab('Credits Completed')+ylab('GPA')
c+geom_point()+geom_smooth(method='lm')+ggtitle('Notre Dame Students: Credits Completed vs GPA')


###Question2: given data.txt write a script that generates two figures that summarize the data
import pandas as pd
import numpy as np
from plotnine import *

data=pd.read_csv('data.txt',sep=',',header=0)

#barplot of means of 4 populations
a=ggplot(data,aes(x='region',y='observations'))+theme_classic()+xlab('Region')+ylab('Mean Observations')
a+geom_bar(stat='summary',fun_y=np.mean)

#scatter plot of all observations
b=ggplot(data,aes(x='region',y='observations'))+theme_classic()+xlab('Region')+ylab('Observations')
b+geom_jitter()

#Do bar and scatter plot tell different stories? 
    #Yes, the bar and scatter tell different stories because the bar plot is 
    #showing the mean number of observations for each of the four regions. 
    #The bar graph also shows each population as being almost the same (about
    #15 observations per population). The scatter plot gives a clearer picture
    #of the distribution of the different observations in each region. The east
    #and west populations have wide distributions, the north has a small
    #distribution and the south has a split (bimodal) distribution. Therefore,
    #even though all populations had around the same mean, they have very
    #different distributions which provides different information than the
    #bar graph provided.