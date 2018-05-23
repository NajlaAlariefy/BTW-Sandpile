'''
    File name: plots.py
    Author: Najla Alariefy
    Date created: 08/MAR/2018
    Date last modified: 01/MAY/2018
    Python Version: 3.0
'''

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import cm
from pylab import *
from scipy import stats
import powerlaw
plt.style.use('seaborn')


# plots all plots when running from command line
def generate_plots(sandpile, time, avalanche_mass, avalanche_size,
                   avalanche_lifetime, avalanche_area, avalanche_radius,
                   cutoff = 100):
    time = time - cutoff
    plot_sandpile(sandpile,time)
    plot_mass(avalanche_mass)
    plot_pdf(avalanche_mass[cutoff:], 'Mass')
    plot_pdf(avalanche_lifetime, 'Lifetime')
    plot_pdf(avalanche_size, 'Size')
    plot_pdf(avalanche_radius, 'Radius')
    plot_pdf(avalanche_area, 'Area')



# plots the sandpile as a heatmap
def plot_sandpile(sandpile, time):
    fig = plt.figure(figsize=(10,10))
    plt.title('The sandpile after '+ str(time) +' grains dropped.')
    plt.imshow(sandpile, cmap='hot', interpolation='nearest')
    plt.savefig("figs/sandpile.svg")
    plt.show()
    plt.clf()



# plots Mass Accumelation through Time
def plot_mass(mass):
    plt.clf()
    fig = plt.figure(figsize=(14,7))
    plt.plot(range(0,len(mass)),mass)
    plt.ylabel(' Mass')
    plt.xlabel(' Time')
    plt.title('Avalanche Mass Accumelation through Time', fontsize=12)
    plt.fill_between(0, mass)
    plt.savefig("figs/mass.svg")
    plt.show()
    plt.clf()



# Plotting log-log plots with Power Law Fit
def plot_loglog(avalanche, label):
    powerlaw.plot_pdf(avalanche)
    plt.ylabel(str(feature))
    plt.title('Avalanche ' + label + ' — Power Law Fit')
    plt.savefig("figs/" + label + "_powerlaw.svg")
    plt.show()
    plt.clf()



# Plotting PDF plots with Power Law Fit
def plot_pdf(avalanche, label):
    fig = plt.figure(figsize=(7,7))
    plt.hist(avalanche, bins = range(min(avalanche), max(avalanche) + 200, 200))
    # Computing theoretical distribution, code excerpt from
    # https://elf11.github.io/2017/10/29/python-fitting-data.html
    xt = plt.xticks()[0]
    xmin, xmax = min(xt), max(xt)
    lnspc = np.linspace(xmin, xmax, len(avalanche))
    ab,bb,cb,db = stats.beta.fit(avalanche)
    pdf_beta = stats.beta.pdf(lnspc, ab, bb,cb, db)
    plt.plot(lnspc, pdf_beta, label="Beta")
    plt.grid(True)
    plt.title('Avalanche'+ label + ' PDF', fontsize=18)
    plt.savefig("figs/distribution.svg")
    plt.show()
    plt.clf()



# no longer in use
def plot3D(sandpile,size):
    x = linspace(-1, 1, size)
    y = x
    X,Y = meshgrid(x, y)
    Z = sandpile
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap= 'copper_r')
    plt.title('Sandpile at the Last Time Iteration')
    plt.show()
    plt.clf()



# Print iterations progress, code excerpt from https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total:
        print()
