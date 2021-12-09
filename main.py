"""
Multiprocessing based code to estimate the value of PI using monte carlo sampling
Ref: http: // math.fullerton.edu / mathews / n2003 / montecarlopimod.html
Uses workers:
http: // docs.python.org / library / multiprocessing.html  # module-multiprocessing.pool
"""

import random
import multiprocessing as mp
from time import perf_counter

def monte_carlo_pi_part(n):

    count = 0
    for i in range(int(n)):
        x = random.random()
        y = random.random()

        # Point in the unit circle
        if x*x + y*y <= 1:
            count=count+1

    #return
    return count


if __name__=='__main__':
    random.seed()
    np = mp.cpu_count()
    print('You have {0:1d} CPUs'.format(np))

    # Number of points to use for the Pi estimation
    n = 10_000_000

    # iterable with a list of points to generate in each worker
    # each worker process gets n/np number of points to calculate Pi from

    part_count = [n/np] * np

    with mp.Pool(processes=np) as pool:
        count = pool.map(monte_carlo_pi_part, part_count)

    print("Esitmated value of Pi:: ", sum(count)/(n*1.0)*4)