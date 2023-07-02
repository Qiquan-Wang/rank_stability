#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 14:01:50 2023

@author: qw817
"""


# import packages
import numpy as np
import os
import matplotlib.pyplot as plt
import gudhi
from compute_rank_function_from_barcode import rank_function
import matplotlib.pyplot as plt
import math
import random

# function to generate n pts on the circle of radius r around centre (x,y) normally set to be (0,0)
def sample_circle(r, n, centre = [0,0]):
    theta = np.random.rand(n)*2*np.pi
    x = centre[0] + r * np.cos(theta)
    y = centre[1] + r * np.sin(theta)
    return np.transpose(np.array([x,y])) # output is a nx2 matrix

## Noise 1
# function to sample n pts from the circle of radius r and centre (x,y) with single outlier at (0,0)
def sample_with_single_outlier(r, n, centre=[0,0]):
    pts = sample_circle(r,n, centre)
    return np.vstack([pts[:(n-1),:],[0,0]])

## Noise 2
# function to sample n pts from the circle of radius r and centre (x,y) with gaussian noise with chosen standard deviation
def sample_with_Gaussian(r, n, noise_sd, centre=[0,0]):
    pts = sample_circle(r,n, centre)
    return pts + np.random.normal(0,noise_sd, pts.shape)

## Noise 3
# function to sample n pts from the circle of radius r and centre (x,y) with exponential noise with chosen standard deviation
def sample_with_exponential(r, n, noise_sd, centre=[0,0]):
    pts = sample_circle(r,n, centre)
    return pts + np.random.exponential(noise_sd, pts.shape)

## Noise 4
# function to sample n pts from the circle of radius r and centre (x,y) with power-law noise with chosen standard deviation
def sample_with_powerlaw(r, n, centre=[0,0]):
    # set parameters 
    a = 3
    m = 1/(5*math.sqrt(3))
    pts = sample_circle(r,n, centre)
    return pts + (np.random.pareto(a,pts.shape)+1)*m

## Noise 5
# function to sample n-1 pts from the circle of radius r and centre (x,y) with gaussian noise with chosen standard deviation and a single outlier at (0,0)
def sample_noise5(r, n, noise_sd, centre=[0,0]):
    pts = sample_with_Gaussian(r, n, noise_sd, centre)
    return np.vstack([pts[:(n-1),:],[0,0]])


## Noise 6
# function to sample n pts from the circle of radius r and centre (x,y) with gaussian noise with chosen standard deviation
def sample_extrems(r, n, noise_sd, centre=[0,0]):
    pts = sample_with_Gaussian(r, n, noise_sd, centre)
    out_pts = np.vstack([pts[:(n-11),:],[0,0]])
    # sample 10 extreme points
    theta = np.random.rand(10)*2*np.pi
    rad = np.random.uniform(1.25,3,10)*r
    x = centre[0] + rad * np.cos(theta)
    y = centre[1] + rad * np.sin(theta)
    return np.vstack([out_pts,np.array([x,y]).T])
    
# function to sample from the different types of noise
def sample_noise(type_of_noise, n = 100, r = 2, noise_sd = 0.1, centre = [0,0]):
    # the type of noise should be an integer between 1 and 6 representing the different types of noise
    # the parameters are set as set out in the paper
    if type_of_noise==1:
        return sample_with_single_outlier(r, n, centre)
    
    elif type_of_noise==2:
        return sample_with_Gaussian(r, n, noise_sd, centre)
    
    elif type_of_noise==3:
        return sample_with_exponential(r, n, noise_sd, centre)
    
    elif type_of_noise==4:
        return sample_with_powerlaw(r, n, centre)
    
    elif type_of_noise==5:
        return sample_noise5(r, n, noise_sd, centre)
        
    elif type_of_noise==6:
        return sample_extrems(r, n, noise_sd, centre)

# function for plotting the circle samples with the noise samples together
def plot_scatter(sample0, sample1, sample2, sample3, sample4, sample5, sample6, label0 = "circle", label1 = "noise 1", label2 = "noise 2", label3 = "noise 3", label4 = "noise 4", label5 = "noise 5", label6 = "noise 6"):
    fig, axs = plt.subplots(2,3, figsize = (16,10))
    # noise 1
    axs[0,0].scatter(sample0[:,0], sample0[:,1], label=label0)
    axs[0,0].scatter(sample1[:,0], sample1[:,1], label=label1)
    axs[0,0].axis('equal')
    axs[0,0].legend(loc = "upper right")
    # noise 2
    axs[0,1].scatter(sample0[:,0], sample0[:,1], label=label0)
    axs[0,1].scatter(sample2[:,0], sample2[:,1], label=label2)
    axs[0,1].axis('equal')
    axs[0,1].legend(loc = "upper right")
    # noise 3
    axs[0,2].scatter(sample0[:,0], sample0[:,1], label=label0)
    axs[0,2].scatter(sample3[:,0], sample3[:,1], label=label3)
    axs[0,2].axis('equal')
    axs[0,2].legend(loc = "upper right")
    # noise 4
    axs[1,0].scatter(sample0[:,0], sample0[:,1], label=label0)
    axs[1,0].scatter(sample4[:,0], sample4[:,1], label=label4)
    axs[1,0].axis('equal')
    axs[1,0].legend(loc = "upper right")
    # noise 5
    axs[1,1].scatter(sample0[:,0], sample0[:,1], label=label0)
    axs[1,1].scatter(sample5[:,0], sample5[:,1], label=label5)
    axs[1,1].axis('equal')
    axs[1,1].legend(loc = "upper right")
    # noise 6
    axs[1,2].scatter(sample0[:,0], sample0[:,1], label=label0)
    axs[1,2].scatter(sample6[:,0], sample6[:,1], label=label6)
    axs[1,2].axis('equal')
    axs[1,2].legend(loc = "upper right")    
    
    plt.show()

# define a function that given a distance matrix and indices of 2 groups compute the total variance
def dist_variance(dist_mat, index1, index2):
    var1 = 0
    for i in index1:
        for j in index1:
            var1 += dist_mat[i,j]
    var2 = 0
    for m in index2:
        for l in index2:
            var2 += dist_mat[m,l]
    n1 = len(index1)
    n2 = len(index2)
    tot_var = (var1/(2*n1*(n1-1))) + (var2/(2*n2*(n2-1)))
    return tot_var

# function computes p-val for randomization test from persistence diagrams
def PD_randomization_test(sample1, sample2, N, dist_type="bottleneck", plot=False):
    # default distance type is bottleneck, but can have wasserstein dsitance as well
    n1 = len(sample1)
    n2 = len(sample2)
    labels = [i for i in range(n1+n2)]
    all_samples = sample1+sample2
    # compute a distance matrix between the two sets
    distances = np.zeros([n1+n2,n1+n2])
    for i in range(n1+n2):
        for j in range(i+1,n1+n2):
            if dist_type == "bottleneck":
                dist = gudhi.bottleneck_distance(np.vstack(all_samples[i]), np.vstack(all_samples[j]))
                distances[i,j] = dist
                distances[j,i] = dist
            elif dist_type == "wasserstein":
                dist = gudhi.wasserstein.wasserstein_distance(np.vstack(all_samples[i]), np.vstack(all_samples[j]))
                distances[i,j] = dist
                distances[j,i] = dist
        
    # computes initial variance            
    initial_variance = dist_variance(distances, [i for i in range(n1)], [i for i in range(n1,n1+n2)])
    
    variances = []
    z = 1
    # permute and compute new variances
    for k in range(N-1):
        random.shuffle(labels)
        ind1 = labels[:n1]
        ind2 = labels[n1:]
        
        new_variance = dist_variance(distances, ind1, ind2)
        
        variances.append(new_variance)
        
        if new_variance <= initial_variance:
            z += 1        
     
    # compute p-val as Z/(N+1)
    p_val = z/(N+1)
    
    if plot!=False:
        # plot the distribution of the variances under permutation
        result = plt.hist(variances, bins = 10,  color='c', edgecolor='k', alpha=0.65)
        plt.axvline(initial_variance, color='k', linestyle='dashed', linewidth=1)
        min_ylim, max_ylim = plt.ylim()
        plt.text(initial_variance, max_ylim, 'Observed loss: {:.2f}'.format(initial_variance))
        # plt.savefig(result)
        plt.show()
    
    return p_val #, variances

# computes variance for collection of functions
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

def Randomization_test(sample1, sample2, N, plot=False):
    # takes in two lists of samples and carries out re-randomization testing
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
        ind1 = [int(u) for u, x in enumerate(labels) if x == 1]
        ind2 = [int(u) for u, x in enumerate(labels) if x == 2]
        new_sample1 = [all_samples[w] for w in ind1]
        new_sample2 = [all_samples[w] for w in ind2]
        
        new_variance = total_variance(new_sample1, new_sample2)
        # print(new_variance)
        variances.append(new_variance)
        
        if new_variance <= initial_variance:
            z += 1
    
    # compute p-val 
    p_val = z/(N+1)
    
    if plot:
        # plot the distribution of the variances under permutation
        result = plt.hist(variances, bins = 10,  color='c', edgecolor='k', alpha=0.65)
        plt.axvline(initial_variance, color='k', linestyle='dashed', linewidth=1)
        min_ylim, max_ylim = plt.ylim()
        plt.text(initial_variance, max_ylim, 'Observed loss: {:.2f}'.format(initial_variance))
        plt.show()
    
    return p_val #, variances