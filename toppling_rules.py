'''
    File name: toppling_rules.py
    Author: Najla Alariefy
    Date created: 08/MAR/2018
    Date last modified: 19/MAY/2018
    Python Version: 3.0
'''

import numpy as np


def check_threshold(sandpile,i ,j, threshold, s, l, a, r):
    """ Checks for avalanche events, returns avalanche attributes.

        Args:
            sandpile:   array holding sand grainsself
            i :         row index of the avalanche site
            j :         column index of the avalanche site
            threshold : toppling threshold
            s, l, a, r: tracking size, lifetime, area, radius of the avalanche

        Returns:
            size
            lifetime
            area
            radius

    """

    ## Beginning Avalanche
    # Checking for avalanche:
        # IF  (the location is inside the table)
        # AND (the number of sand grains is above the threshold)

    if not (i > sandpile.shape[0] or  j > sandpile.shape[1] or i <0 or j <0)and sandpile[i,j] >= threshold:
        l[i,j] += 1             # increase lifetime
        s[i,j] += threshold     # increase size
        a[i,j] = 1              # count area
        # execute the toppling rules
        r = toppling(sandpile, i, j, threshold, s, l, a, r)

    ## Ending Avalanche


    # Lifetime is how many topplings the avalanche triggered
    lifetime = np.sum(l)

    # Area is sum of all unique cells that have been toppled
    area = np.sum(a)

    # Radius is how long's the furtherist toppling site from the initial site
    m,n = np.where(r==10) # initial site index
    R,C = np.where(r==1)  # all sites that have been affected
    radius = np.max([abs(R-m)+abs(C-n)]) if R.size !=0 else 0

    # Size is how many grains of sand have been displaced
    size = np.sum(s)

    return size, lifetime, area, radius



# Executes toppling rules
def toppling(sandpile, i, j, threshold, size, lifetime, area, radius):
    """ Toppling rules based on Bak-Tang-Wiesenfeld sandpile rules. """


    # (1) toppling rule: z(i, j, t) = z(i, j, t) -  4
    sandpile[i,j] = sandpile[i,j]  -  threshold


    # (2) toppling rule: z(i ± 1, j, t) = z(i ± 1, j, t) + 1
    if i + 1 <= sandpile.shape[0]-1:
        sandpile[i + 1,j]  += 1
        radius[i + 1,j] = 1 if radius[i + 1,j] != 10 else 10
        check_threshold(sandpile, i + 1 ,j,threshold,size,lifetime,area,radius)
    if i - 1 >= 0:
        sandpile[i - 1,j] += 1
        radius[i - 1,j] = 1 if radius[i - 1,j] != 10 else 10
        check_threshold(sandpile, i - 1 ,j,threshold,size,lifetime,area,radius)


    # (3) toppling rule: z(i, j ± 1, t) = z(i, j ± 1, t) + 1
    if j + 1 <= sandpile.shape[1]-1:
        sandpile[i ,j + 1] += 1
        radius[i ,j + 1] = 1 if radius[i ,j + 1] != 10 else 10
        check_threshold(sandpile,i, j + 1 ,threshold,size,lifetime,area,radius)
    if j - 1 >= 0:
        sandpile[i ,j - 1] += 1
        radius[i ,j - 1] = 1 if radius[i ,j - 1] != 10 else 10
        check_threshold(sandpile,i, j - 1 ,threshold,size,lifetime,area,radius)

    return radius
