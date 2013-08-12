
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
    
    def intra_correlate(self, gaps_method, norm_method, sub_method):
   
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
    

class Corr( object):

    def __init__ (  self , N, A, B, norm, sub,  nozero ):   
        self.N =  N

        self.norm = norm
        self.sub = sub
        self.nozero = nozero
          
        self.A = A
        self.B = B

        self.A_mean  =  mean_no_zero(A)
        self.B_mean  =  mean_no_zero(B)
          
        self.A_stdev  = stdev_no_zero(A, A_mean)
        self.B_stdev  = stdev_no_zero(B, B_mean)

        if norm==0:
            self.norm_factor = self.A_mean * self.B_mean
        elif norm==1:
            self.norm_factor = self.A_stdev * self.B_stdev
        else:
            self.norm_factor = 1.
        
        self.C = np.zeros( self.N ) 

        return correlate ()


    def correlate(self): 
    
        if self.sub == 0 and self.nozero == 0:
            for phi in xrange( self.N ):
                counts=0 # keep track of the number of good pairs
                for i in xrange( self.N ) : 
                    j = i + phi
                if j >= self.N: 
                    j  = j - self.N
              
                if self.A[i] > 0 and self.B[j] > 0: 
                    self.C[phi] += ( self.A[i] - self.A_mean) *( self.B[j]-self.B_mean) 
                    counts += 1
                self.C[phi] = self.C[phi] / (norm_factor *  counts)
      
      
        elif  self.sub==1 and self.nozero == 0 :
            for phi in xrange( self.N ) : 
                counts=0 # keep track of the number of good pairs
                for i in xrange( self.N ) :
                    j = i + phi
              
                    if j >= self.N: 
                        j = j -  self.N
              
                    if self.A[i] > 0 and self.B[j] > 0: 
                        self.C[phi] += self.A[i]* self.B[j] 
                        counts += 1
                
                self.C[phi] = self.C[phi] / (norm_factor *  counts);

        elif self.sub == 0 and self.nozero == 1:
            for phi in xrange( self.N ) :
                for i in xrange( self.N ) :
                    j = i + phi
          
                    if j >= self.N: 
                        j = j- self.N
          
                    self.C[phi] += ( self.A[i] - self.A_mean) *( self.B[j]-self.B_mean) ;
                self.C[phi] = self.C[phi] / (norm_factor *  float(self.N) );
        else:
            for phi in xrange( self.N ) :
                for i in xrange( self.N ) :
                    j = i + phi
          
                    if j >= self.N: 
                        j = j - self.N
          
                    self.C[phi] += self.A[i]* self.B[j]

                self.C[phi] = self.C[phi] / (norm_factor *  float( self.N ) )


    def mean_no_zero(self, ar): 
        if self.nozero == 0:
            ar_mean=0
            counts=0
            for i in xrange( self.N ) :
                if(ar[i] > 0)
                    ar_mean += ar[i]
                    counts +=1
            if counts > 0:
                return ar_mean / counts
            else:
                return 0
        else:
            ar_mean=0
            for i in xrange( self.N ) :
                ar_mean += ar[i]
            return ar_mean / float( self.N)

    def stdev_no_zero(self,ar, ar_mean):
        """the array ar is already mean subtracted"""

        if (nozero == 0 ):
            ar_stdev=0
            counts=0
            for i in xrange( self.N ):
                if ar[i] > 0:
                    ar_stdev += ( ar[i]- ar_mean )* ( ar[i] - ar_mean ) 
                    counts +=1
            if counts > 0:
                return sqrt( ar_stdev / counts )
            else:
                return 0
      
        else:
            ar_stdev = 0
            for i in xrange( self.N ): 
                ar_stdev += ( ar[i]- ar_mean )* ( ar[i] - ar_mean ) 
        return np.sqrt( ar_stdev / float(self.N) )
