#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 23:15:46 2022

@author: qw817
"""

import random
import numpy as np
import matplotlib.pyplot as plt

def total_variance(sample1, sample2):
    # takes in two lists of samples and computes their total variance
    n1 = len(sample1)
    n2 = len(sample2)
    
    # compute variance of the two samples
    # compute mean of each sample
    mean1 = sum(sample1)/n1
    mean2 = sum(sample2)/n2
    
    # compute variance
    var1 = np.sum([np.square(i-mean1) for i in sample1])/(n1-1)
    var2 = np.sum([np.square(i-mean2) for i in sample2])/(n2-1)
    
    return var1 + var2
    
    
    
def Permutation_test(sample1, sample2, N, plot=False):
    # takes in two lists of samples and carries out permutation testing
    # function returns p-value 
    
    n1 = len(sample1)
    n2 = len(sample2)
    labels = [1 for i in range(n1)] + [2 for i in range(n2)]
    initial_variance = total_variance(sample1, sample2)
    
    all_samples = sample1 + sample2
    
    z = 1
    variances = []
    
    # permute over N interation
    for i in range(N-1):
        random.shuffle(labels)
        ind1 = [u for u, x in enumerate(labels) if x == 1]
        ind2 = [u for u, x in enumerate(labels) if x == 2]
        new_sample1 = all_samples[int(ind1)]
        new_sample2 = all_samples[int(ind2)]
        
        new_variance = total_variance(new_sample1, new_sample2)
        
        variances.append(new_variance)
        
        if new_variance <= initial_variance:
            z += 1
    
    # compute Z/N
    p_val = z/(N+1)
    
    if plot:
        # plot the distribution of the variances under permutation
        result = plt.hist(variances, bins = 10,  color='c', edgecolor='k', alpha=0.65)
        plt.axvline(initial_variance, color='k', linestyle='dashed', linewidth=1)
        min_ylim, max_ylim = plt.ylim()
        plt.text(initial_variance*1.1, max_ylim*0.9, 'Observed loss: {:.2f}'.format(initial_variance))
        plt.show()
    
    return p_val



    
    
    
    
    
    
    