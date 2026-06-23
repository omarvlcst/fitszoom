from astropy.io import fits  # importing i/o subpackage for reading FITS files

import astropy.units as u # astropy units

import matplotlib.pyplot as plt
import numpy as np

class FITSZoom(object):

    def __init__(self, filename):
        
        self.filename = filename             
        self.fits = fits.open(filename) # open the fits file --> this returns as a list of Header and Data units
        self.setup() # pull out the data we need so that they are ready to use right after construction
    
    def setup(self):
        """
        Extract the necessary attributes from the fits header
        """
        self.header = self.fits[0].header
        self.data = self.fits[0].data
        ### TO DO ###
        return 
    
    def zoom(self, coordinates, cutout_dimensions):
        """
        Zoom into the given coordinates and create a cutout with the given dimensions

        Args:
            coordinates (tuple): ra, dec
            cutout_dimensions (tuple): dimensions 
        """

        ### TO DO ###
        return 
    
    def plot(self, **kwargs):
        """
        Use matplotlib imshow to display the cutout

        Returns:
            axes: the plt axes with the image
        """

        # set some defaults
        if not kwargs.get('vmin', False):
            kwargs['vmin'] = np.percentile(self.data, 1)

        if not kwargs.get('vmax', False):
            kwargs['vmax'] = np.percentile(self.data, 99)
    

        plt.imshow(self.data, **kwargs)

        return plt.gca()
