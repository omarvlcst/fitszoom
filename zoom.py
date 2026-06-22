from astropy.io import fits

class FITSZoom(object):

    def __init__(self, filename):
        
        self.filename = filename
        self.fits = fits.open(filename)

    def setup(self):
        """
        Extract the necessary attributes from the fits header
        """

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