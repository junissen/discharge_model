#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 18:20:37 2017

@author: julianissen
"""

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize = (8,8))

ax1 = fig.add_subplot(1,1,1)

sv_array = [0.02, 0.014, 0.042, 0.032, 0.011, 0.009, 0.049, 0.045]

m_array= [0.9, 0.6, 1.8, 1.4, 0.5, 0.4, 2.1, 2.0]

#ax1.scatter(sv_array, m_array, marker = 's', color = 'k')

def trendline(xd, yd, ax, order, c, linestyle, alpha=1, left = True):
    """Make a line of best fit"""

    #Calculate trendline
    coeffs = np.polyfit(xd, yd, order)

    intercept = coeffs[-1]
    slope = coeffs[-2]
    power = coeffs[0] if order == 2 else 0

    minxd = np.min(xd)
    maxxd = np.max(xd)

    xl = np.array([minxd, maxxd])
    yl = power * xl ** 2 + slope * xl + intercept

    #Plot trendline
    #ax.plot(xl, yl, c, alpha=alpha, lw = 2)

    #Calculate R Squared
    p = np.poly1d(coeffs)

    ybar = np.sum(yd) / len(yd)
    ssreg = np.sum((p(xd) - ybar) ** 2)
    sstot = np.sum((yd - ybar) ** 2)
    Rsqr = ssreg / sstot
    """
    if left:
        #Plot R^2 value
        #ax.text(0.25 * maxxd + 0.9 * minxd, 0.9 * np.max(yd) + 0.25 * np.min(yd),
        #         '$R^2 = %0.2f$' % Rsqr, fontsize = 8)
        ax.text(0.7 * maxxd + 0.9 * minxd, 0.1 * np.max(yd) + 0.35 * np.min(yd),
                'y = ' + str("{0:.2f}".format(slope)) + 'x +' + str("{0:.2f}".format(intercept)), fontsize = 12)

    else:
        #Return the R^2 value:
        #ax.text(0.75 * maxxd + 0.2 * minxd, 0.75 * np.max(yd) + 0.2 * np.min(yd),
        #         '$R^2 = %0.2f$' % Rsqr, fontsize = 8)
        ax.text(0.25 * maxxd + 0.9 * minxd, 0.9 * np.max(yd) + 0.35 * np.min(yd),
                'y = ' + str("{0:.2f}".format(slope)) + 'x +' + str("{0:.2f}".format(intercept)), fontsize = 8)
    """
    print slope
    print intercept

trendline(sv_array, m_array, ax = ax1, order = 1, c = '0.3', linestyle = '--', alpha = 1, left = True)

d18o = r'$\delta^{18}\!O$'

ax1.set_xlabel('Discharge Increase (Sv) from Melting LIS through Southern Outlet', fontsize = 12)
ax1.set_ylabel('Equivalent Sea Level Rise (m) over 500 years', fontsize = 12)
ax1.set_title('Sea Level Rise for varying ' + d18o  + ' of meltwater components', fontsize = 14)

ax1.tick_params(labelsize = 14)

discharge_7p_25i = [0.0199, 0.0406]
discharge_7p_12i = [0.0416, 0.0811]

discharge_6p_25i = [0.0247, 0.0367]
discharge_6p_12i = [0.0517, 0.0696]

meltwater_7p_25i = []
meltwater_7p_12i = []
meltwater_6p_25i = []
meltwater_6p_12i = []

for item in discharge_7p_25i:
    y = (43.01*item) + 0.02
    meltwater_7p_25i.append(y)
  
for item in discharge_7p_12i:
    y = (43.01*item) + 0.02
    meltwater_7p_12i.append(y)
    
for item in discharge_6p_25i:
    y = (43.01*item) + 0.02
    meltwater_6p_25i.append(y)
    
for item in discharge_6p_12i:
    y = (43.01*item) + 0.02
    meltwater_6p_12i.append(y)
    
minxd = 0.04
maxxd = 0.125
x = np.array([minxd, maxxd])

y = (43.01 * x) + 0.02
    
ax1.plot(x, y, color = 'gray', zorder = 1)

discharge_7p_25i_combined = discharge_7p_25i[0] + discharge_7p_25i[1]
print "7p 25i"
print discharge_7p_25i
print discharge_7p_25i_combined

discharge_7p_12i_combined = discharge_7p_12i[0] + discharge_7p_12i[1]
print "7p 12i"
print discharge_7p_12i
print discharge_7p_12i_combined

discharge_6p_25i_combined = discharge_6p_25i[0] + discharge_6p_25i[1]
print "6p 25i"
print discharge_7p_25i
print discharge_7p_25i_combined

discharge_6p_12i_combined = discharge_6p_12i[0] + discharge_6p_12i[1]
print "6p 12i"
print discharge_6p_12i
print discharge_6p_12i_combined
    
meltwater_7p_25i_combined = meltwater_7p_25i[0] + meltwater_7p_25i[1]
meltwater_7p_12i_combined = meltwater_7p_12i[0] + meltwater_7p_12i[1]
print "Max meltwater partitioned: Benthic- " + str(meltwater_7p_12i[0]) +  " Planktonic- " + str(meltwater_7p_12i[1])
print "Max meltwater: " + str(meltwater_7p_12i_combined)
print "Min meltwater: " + str(meltwater_7p_25i_combined)

meltwater_6p_25i_combined = meltwater_6p_25i[0] + meltwater_6p_25i[1]
meltwater_6p_12i_combined = meltwater_6p_12i[0] + meltwater_6p_12i[1]


#ax1.scatter(discharge_7p_25i, meltwater_7p_25i, marker = 'x', color = 'r', s = 100, linewidth = 3, zorder = 2)
#ax1.scatter(discharge_7p_12i, meltwater_7p_12i, marker = 'o', color = 'm', s = 100, linewidth = 3, zorder = 2)

#ax1.scatter(discharge_6p_25i, meltwater_6p_25i, marker = 'x', color = 'b', s = 100, linewidth = 3, zorder = 2)
#ax1.scatter(discharge_6p_12i, meltwater_6p_12i, marker = 'o', color = 'g', s = 100, linewidth = 3, zorder = 2)



ax1.scatter(0.014+0.032, 0.6+1.4, marker = '*', color = 'k', s = 100, linewidth = 3, zorder = 2, label = d18o + 'p: -7.7 | ' + d18o + 'i: -35 (Carlson2009)')
ax1.scatter(0.02+0.042, 0.9+1.8, marker = '+', color = 'k', s = 100, linewidth = 3, zorder = 2, label = d18o + 'p: -7.7 | ' + d18o + 'i: -25 (Carlson2009)')

ax1.scatter(discharge_7p_25i_combined, meltwater_7p_25i_combined, marker = 'x', color = 'r', s = 100, linewidth = 3, zorder = 3, label = d18o + 'p: -7.7 | ' + d18o + 'i: -25.5')
ax1.scatter(discharge_6p_25i_combined, meltwater_6p_25i_combined, marker = 'x', color = 'b', s = 100, linewidth = 3, zorder = 3, label = d18o + 'p: -6.3 | ' + d18o + 'i: -25.5')

ax1.scatter(discharge_7p_12i_combined, meltwater_7p_12i_combined, marker = 'o', color = 'm', s = 100, linewidth = 3, zorder = 3, label = d18o + 'p: -7.7 | ' + d18o + 'i: -12.5')
ax1.scatter(discharge_6p_12i_combined, meltwater_6p_12i_combined, marker = 'o', color = 'g', s = 100, linewidth = 3, zorder = 3, label = d18o + 'p: -6.3 | ' + d18o + 'i: -12.5')

handles, labels = ax1.get_legend_handles_labels()
ax1.legend(handles, labels, loc = 4, prop = {'size': 10})

#fig.savefig('Meltwater_estimates', dpi = 300)