#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:55:52 2017

@author: julianissen
"""

import discharge_model_vardp
import matplotlib.pyplot as plt

fig = plt.figure(figsize = (16,8))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)


x_lim_benthic = [0.012,0.063] 
y_lim_benthic = [-25, -12] 

x_lim_planktonic = [0.03, 0.1]
y_lim_planktonic = [-25, -12] 



wb1 = discharge_model_vardp.discharge_model_vardp(ax1, x_lim_benthic, y_lim_benthic)

wb1.discharge_benthic_dp()

wb2 = discharge_model_vardp.discharge_model_vardp(ax2, x_lim_planktonic, y_lim_planktonic)

wb2.discharge_planktonic_dp()



d18o = r'$\delta^{18}\!O$'

ax1.set_title("Discharge increase from melting LIS for benthic anomaly", fontsize = 14)
ax1.set_ylabel(d18o + " of Laurentide meltwater", fontsize = 12)
ax1.set_xlabel("Sv", fontsize = 12)
ax1.tick_params(labelsize = 12)
ax1.annotate("Increasing " + d18o + "p", xy=(0.0528, -22.85), xytext=(0.035, -23), 
             arrowprops = dict(arrowstyle = "->"), fontsize = 12) 
handles, labels = ax1.get_legend_handles_labels()
ax1.legend(handles, labels, loc = 4, prop = {'size': 10})


ax2.set_title("Discharge increase from melting LIS for planktonic anomaly", fontsize = 14)
ax2.set_ylabel(d18o + " of Laurentide meltwater", fontsize = 12)
ax2.set_xlabel("Sv", fontsize = 12)
ax2.tick_params(labelsize = 12)
ax2.annotate("Decreasing " + d18o + "p", xy=(0.09, -22.85), xytext=(0.065, -23), 
             arrowprops = dict(arrowstyle = "->"), fontsize = 12) 
handles, labels = ax2.get_legend_handles_labels()
ax2.legend(handles, labels, loc = 4, prop = {'size': 10})


#fig.savefig('Discharge_model', dpi = 300)

