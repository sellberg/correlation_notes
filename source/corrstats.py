
# AUTHORS:
# TJ Lane <tjlane@stanford.edu>
# Jonas Sellberg <sellberg@slac.stanford.edu>
# Derek Mendez <dermen@stanford.edu>
#
# Aug 9, 2013

"""
An interface to CorrStats - a statistical approach to correlations from an ensemble.
"""

import numpy as np

class CorrStats(object):
    """
    """
    def __init__(self, intensities, mask=None):
        """
        """
        
        self.raw_intensities = intensities.copy()
        if not mask:
            self.mask = np.ones(intensities.shape[1:])
        else:
            self.mask = mask
        
    def correlate(self, gaps_method, norm_method, sub_method):
    
    def correlate_inter(self, gaps_method, norm_method, sub_method):
    
    def add_noise(self, mean):
    
    def add_power_fluctuations(self, sigma):
    
    def add_gaps(self, mask):
    
    def add_pixel_gain(self, gain):
    
    def add_nonlinear_gain(self, gain):
    
    def add_background(self, bg):
    
    def ensemble_statistics(self)
    
    def plot(self):
    
    def save()
    
    def load()
    
