'''
    File name: BTW_sandpile.py
    Author: Najla Alariefy
    Date created: 08/MAR/2018
    Date last modified: 20/MAY/2018
    Python Version: 3.0
'''
import sys
import argparse

from   random  import randrange
import numpy   as np
from scipy.stats.stats import pearsonr
from plots import printProgressBar, generate_plots, plot3D
from time import sleep
from toppling_rules import check_threshold



# BTW/Abelian Sandpile running function
def BTWsandpile(M = 3, N = 3, show_step = False,
                    time=10000, threshold=4, method='random', plot = False):
    """ Runs the simulation and returns the sandpile

        Args:
            M          (int): Pile width
            N          (int): Pile height
            show_step  (bool): If True, prints sandpile at each time step
            time       (int): How many time steps to run the simulation
            threshold  (int): Critical moment threshold
            method     (string): type of simulation 'center' or 'random'
            plot       (bool): If True, it will print all plots

        Returns:
            avalanche_mass     (list[int]): the mass at all time steps
            avalanche_size     (list[int]): list of avalanche sizes
            avalanche_lifetime (list[int]): list of avalanche lifetimes
            avalanche_area     (list[int]): list of avalanche areas
            avalanche_radius   (list[int]): list of avalanche radius
            sandpile           (M*N np.array): the last sandpile
    """

    avalanche_mass = []  # sand particles on the table at a point in time
    avalanche_size = []  # sand particles moved by the avalanche
    avalanche_lifetime = []  # timesteps it takes for an avalanche to relax the
                             #system to a critical state. '
    avalanche_radius = []
    avalanche_area = []

    # (1) -  initializes an M by N grid
    sandpile = np.zeros((M, N), dtype=int)
    

    # Initial call to print 0% progress
    printProgressBar(0, time-1, prefix = 'Progress:',
                        suffix = 'Complete', length = 50)

    # (2) -  loop through time steps
    for t in range(time-1):
        if method == 'random':
            # Choose random spot
            M_index = randrange(0, M)
            N_index = randrange(0, N)
        elif method == 'center':
            M_index = M//2
            N_index = N//2

        # Add sand grain
        sandpile[M_index, N_index] += 1

        # (3) - toppling
        radius   = np.zeros((M, N), dtype=int)
        radius[M_index, N_index] = 10
        size     = np.zeros((M, N), dtype=int)
        lifetime = np.zeros((M, N), dtype=int)
        area     = np.zeros((M, N), dtype=int)

        size, lifetime, area, radius = check_threshold(sandpile, M_index,
                                        N_index, threshold, s=size, l=lifetime,
                                        a=area, r=radius)

        # plotting each step
        if show_step:
            plot(sandpile)

        # calculating mass at time step
        avalanche_mass.append(sandpile.sum())
        avalanche_size.append(size)
        avalanche_lifetime.append(lifetime)
        avalanche_area.append(area)
        avalanche_radius.append(radius)

        # Update Progress Bar
        sleep(0.1)
        printProgressBar(t + 1, time-1, prefix = 'Progress:',
                         suffix = 'Complete', length = 50)

    print('Sandpile simulation done. ', time, ' time steps elapsed, ', M,
           '*', N, ' pile size.          ')

    # get a plot for the final sandpile, and plot the avalanche's features
    # plot3D(sandpile, max(M,N))
    if plot:
        generate_plots(sandpile, time, avalanche_mass, avalanche_size,
                        avalanche_lifetime, avalanche_area, avalanche_radius,
                        cutoff = 1000)

    return (avalanche_mass, avalanche_size, avalanche_lifetime, avalanche_area,
            avalanche_radius, sandpile)





def main(args):
    assert args.method in ['center', 'random'], \
        "ERROR: sandpile simulation method has to be either 'center or 'random'."
    assert args.threshold > 3, \
        "ERROR: critical moment should be more than 3 sand grains."

    BTWsandpile(args.M, args.N, args.show_step, args.time, args.threshold, args.method, plot= True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-M", "--M", dest="M", default=3,
                        help="pile width", type=int)
    parser.add_argument("-N", "--N", dest="N", default=3,
                        help="pile height", type=int)
    parser.add_argument("-show", "--show_step", dest="show_step", default=False,
                        help=" show plot for each step", type=bool)
    parser.add_argument("-th", "--threshold", dest="threshold", default=4,
                        help="pile theshold", type=int)
    parser.add_argument("-m", "--method", dest="method", default='random',
                        help="pile theshold")
    parser.add_argument("-t", "--time", dest="time", default=10000,
                        help="number of time steps to run the simulation", type=int)

    args = parser.parse_args()
    main(args)
