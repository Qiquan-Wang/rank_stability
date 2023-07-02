#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 19:27:08 2022

@author: qw817
"""

import numpy as np

def rank_function(Barcode, dim, bins, interval=False):
    # take as input the diagram outputs with all the dimensions and select 
    # the preferred to convert into rank functions
    # dim - represents the dimension wanted
    # bins = number of x and y evaluation points
    
    bars = Barcode[dim]
    
    if bars.shape[0] == 0:
        return print("No element of this dimension")
    
# =============================================================================
#     # find if there exists any essential cycles (values at infinity) and remove
#     # that column
#     keep_element = [np.isfinite(barcode[i,:]) for i in range(barcode.shape[0])]
#     bars = barcode[keep_element,:]
# =============================================================================
    
    # if interval is true then compute the rank function over that region
    # otherwise use the max and min values of the barcodes
    if interval==False:
        min_val = np.min(bars)
        max_val = np.max(bars)
    else:
        min_val = interval[0]
        max_val = interval[1]
        
    val_range = np.linspace(min_val, max_val, bins)
    y_val_range = np.flip(val_range)
    
    
    n = bars.shape[0]
    
    rank_fn = np.zeros([bins, bins])
    for i in range(n):
        begin = bars[i,0]
        end = bars[i,1]
        
        x_indices = [o for o, x in enumerate(val_range>=begin) if x]
        y_indices = [l for l, y in enumerate(y_val_range<=end) if y]
        

        for k in x_indices:
            rank_fn[y_indices, k] +=1
        
    # make the lower triangle values zero
    for i in range(1,bins):
        for j in range(i):
            rank_fn[i,bins-j-1] = 0
    
    return rank_fn
    
    
    
    
    
    
    