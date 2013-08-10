
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
        self.modified_intensities = None
        self.raw_correlations = None
        self.modified_correlations = None
        self.raw_correlations
    
    def correlate(self, gaps_method, norm_method, sub_method):
    
    def inter_correlate(self, gaps_method, norm_method, sub_method):
    
    def add_noise(self, mean):
    
    def add_power_fluctuations(self, sigma):
    
    def add_gaps(self, mask):
    
    def add_pixel_gain(self, gain):
    
    def add_nonlinear_gain(self, gain):
    
    def add_background(self, bg):
    
    @property
    def ensemble_statistics(self)
        stats = {}
        stats['raw intensity'] = (np.mean(self.raw_intensities), np.stdev(self.raw_intensities))
        if self.modified_intensities:
            stats['modified intensity'] = (np.mean(self.modified_intensities), np.stdev(self.modified_intensities))
        if self.raw_correlations:
            stats['raw correlation'] = (np.mean(self.raw_correlations), np.stdev(raw_correlations))
        if self.modified_correlations:
            stats['modified correlation'] = (np.mean(self.modified_correlations), np.stdev(self.modified_correlations))
        return stats
    
    def plot(self):
    
    def save():
    
    @classmethod
    def load(cls, filename):
        f = h5py.File(filename)
        data = np.array(f['data'])
        f.close()
        
        return cls(data)
    
