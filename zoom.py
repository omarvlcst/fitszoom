from astropy.io import fits  # importing i/o subpackage for reading FITS files
from astropy.nddata import Cutout2D
import astropy.units as u # astropy units
from astropy.wcs import WCS

import matplotlib.pyplot as plt
import numpy as np

class FITSZoom(object):

    def __init__(self, filename):
        
        self.filename = filename             
        self.fits = fits.open(filename) # open the fits file --> this returns as a list of Header and Data units
        self.setup() # pull out the data we need so that they are ready to use right after construction
    
    def setup(self, extension=0):
        """
        Extract the necessary attributes from the fits header

        Args:
            extension: the index where the desired data is within the fits
            alternative_names: dictionary mapping the names of appropriate values
        """
        self.header = self.fits[extension].header
        self.data = self.fits[extension].data
        self.wcs = WCS(self.header)
        ### TO DO ##
        sky1 = self.wcs.pixel_to_world(0,0)
        sky2 = self.wcs.pixel_to_world(-1,-1)
        print("---------- Recommendations ------------")
        print(f"ra between {sky1.ra.value:.6f} and {sky2.ra.value:.6f}.")
        print(f"dec between {sky1.dec.value:.6f} and {sky2.dec.value:.6f}.")
        return 
    
    def zoom(self, coordinates, cutout_dimensions, save=False):
        """
        Zoom into the given coordinates and create a cutout with the given dimensions

        Args:
            coordinates (tuple): ra, dec
            cutout_dimensions (tuple): dimensions 
        """

        if cutout_dimensions[0].unit != u.arcsec or cutout_dimensions[1].unit != u.arcsec:
            raise ValueError("please use arcseconds for the dimensions")

        cutout = Cutout2D(self.data, coordinates, cutout_dimensions, wcs=self.wcs)
        
        ax = self.plot(data=cutout.data, save=save)

        return ax, cutout
    
    def plot(self, data=None, save=False, **kwargs):
        """
        Use matplotlib imshow to display the cutout

        Returns:
            axes: the plt axes with the image
        """
        if data is None:
            data = self.data

        # set some defaults
        if not kwargs.get('vmin', False):
            kwargs['vmin'] = np.percentile(self.data, 1)

        if not kwargs.get('vmax', False):
            kwargs['vmax'] = np.percentile(self.data, 99)
    
        fig, ax = plt.subplots(1,1, subplot_kw=dict(projection=self.wcs))

        ax.imshow(data, **kwargs, origin='lower')
        ax.grid(color='white', ls='solid')

        if save == True:
            fig.savefig("zoomed.png")

        return plt.gca()

    def save(self, cutout, output_filename):
        """
        Save a cutout to a new FITS file, without changing the cutout's WCS in the header.
        """

        new_header = cutout.wcs.to_header()

        # Wrap the cropped pixel data and the new header into a primary HDU
        hdu = fits.PrimaryHDU(data=cutout.data, header=new_header)
        # Write it out to disk, overwriting any existing file at that path
        hdu.writeto(output_filename, overwrite=True)

        return output_filename