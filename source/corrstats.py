
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
    

class Corr( N_, ar1, ar2, ar3,  norm_, sub_,  nozero_):

    def __init__ (  self , N_, ar1, ar2, ar3,  norm_, sub_,  nozero_ ):   
        self.N =  N_

        self.norm = norm_
        self.sub = sub_
        self.nozero = nozero_
          
        self.ar1_mean  =  mean_no_zero(ar1)
        self.ar2_mean  =  mean_no_zero(ar2)
          
        self.ar1_stdev  = stdev_no_zero(ar1, ar1_mean)
        self.ar2_stdev  = stdev_no_zero(ar2, ar2_mean)

        if norm==0:
          norm_factor = ar1_mean * ar2_mean
        elif norm==1:
            norm_factor = ar1_stdev * ar2_stdev
        else:
            norm_factor = 1.
          
        return correlate ( ar1,ar2,ar3)



    def correlate( ar1, ar2, arC): 
    
        if self.sub == 0 and self.nozero == 0:
            for phi in xrange( self.N ):
                counts=0 # keep track of the number of good pairs
                for i in xrange( self.N ) : 
                    j = i + phi
                if j >= N: 
                    j  = j - N
              
                if ar1[i] > 0 and ar2[j] > 0: 
                    arC[phi] += ( ar1[i] - ar1_mean) *( ar2[j]-ar2_mean) 
                    counts += 1
                arC[phi] = arC[phi] / (norm_factor *  counts)
      
      
      
      
      else if ( sub==1 && nozero == 0 )
          for ( int phi=0; phi < N; phi++ ) 
            float counts(0); // keep track of the number of good pairs
            for ( int i=0; i < N; i++) 
              int j = i + phi;
              
              if (j >= N) 
                j -= N;
              
              if (ar1[i] > 0 && ar2[j] > 0) 
                arC[phi] += ar1[i]* ar2[j] ;
            counts += 1;
        arC[phi] = arC[phi] / (norm_factor *  counts);

  else if (sub == 0 && nozero == 1)
      for ( int phi=0; phi < N; phi++ ) 
        for ( int i=0; i < N; i++) 
          int j = i + phi;
          
          if (j >= N) 
            j -= N;
          
          arC[phi] += ( ar1[i] - ar1_mean) *( ar2[j]-ar2_mean) ;
        arC[phi] = arC[phi] / (norm_factor *  float(N) );
  else
      for ( int phi=0; phi < N; phi++ ) 
        for ( int i=0; i < N; i++) 
          int j = i + phi;
          
          if (j >= N) 
            j -= N;
          
          arC[phi] += ar1[i]* ar2[j] ;

        arC[phi] = arC[phi] / (norm_factor *  float( N ) );



    def mean_no_zero(ar): 
        if self.nozero == 0:
            ar_mean=0
            counts=0
            for i in xrange( self.N ) :
                if(ar[i] > 0)
                    ar_mean += ar[i];
                    counts ++;
            if counts > 0:
                return ar_mean / counts;
            else:
                return 0;
        else:
            ar_mean=0
            for i in xrange( self.N ) :
                ar_mean += ar[i]
            return ar_mean / float( self.N)

    def stdev_no_zero(self, float * ar, float ar_mean):
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
