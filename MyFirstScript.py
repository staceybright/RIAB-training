#!  /usr/bin/env python

'''
ABOUT: This is a program that takes this and plots that.
DEPENDS: Python 2.7.3
AUTHOR: S N Bright for STScI, 2013
HISTORY: 2013: Test program
USE: python MyFirstScript.py
'''

import numpy as np
import matplotlib.pyplot as plt


infile = 'Gordon2005_Fig16.txt'
outfile = 'fig16_log_script.pdf'
slope, ran_slope_unc, corr_slope_unc, both_slope_unc, eqn_slope_unc = np.loadtxt(infile, usecols=(0, 1, 2, 3, 4), unpack=True)

figure, ax = plt.subplots()

ax.loglog(slope, ran_slope_unc, ls='--', lw=3, color='b',label='Random Unc.')
ax.loglog(slope, corr_slope_unc, ls=':', lw=3, color='r',label='Correlated Unc.')
ax.loglog(slope, both_slope_unc, ls='-', lw=3, color='g',label='Both')
ax.loglog(slope, eqn_slope_unc, ls='-.', lw=3, color='m',label='Equation')
ax.set_xlabel('Slope [e-/s]')
ax.set_ylabel('Slope Uncertainty [e-/s]')
ax.legend(loc='best')
figure.show()
figure.savefig(outfile)
figure.clf()
