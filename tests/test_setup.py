def test_setup():
    """
    Test that the fits image data array shape exceeds 0 for both x and y dimensions
    Test that accessing non-default extensions works
    """

    #from zoom import FITSZoom
    from fitszoom.zoom import FITSZoom

    im_with_ext1 = '../fitszoom/images/tr4_F200W_epoch2_cutout.fits'
    fitszoom_object = FITSZoom(filename=im_with_ext1, extension=1)
    print(fitszoom_object.data.shape)


test_setup()