import numpy as np
import matplotlib as pyplot
import os
from astropy.io import fits

fitsfile = 'M100.mom0.fits'
import glob
data = fits.getdata(fitsfile)
col1 = data[20, :]
col2 = data[33, :]
col3 = data[50, :]
pyplot.show()
#pyplot.figure()
pyplot.plot(np.arange(67), col1)
mean = np.mean(col1)
pyplot.axhline(mean)
pyplot.legend(['Column 20', 'Mean'])
pyplot.title('Plot of Column 20 Values and Mean')
pyplot.xlabel('Pixels')
pyplot.ylabel('Intensity')
pyplot.show()
#pyplot.figure()
pyplot.plot(np.arange(67), col2)
mean = np.mean(col2)
pyplot.axhline(mean)
pyplot.legend(['Column 200', 'Mean'])
pyplot.title('Plot of Column 200 Values and Mean')
pyplot.xlabel('Pixels')
pyplot.ylabel('Intensity')
pyplot.show()
#pyplot.figure()
pyplot.plot(np.arange(67), col3)
mean = np.mean(col3)
pyplot.axhline(mean)
pyplot.legend(['Column 800', 'Mean'])
pyplot.title('Plot of Column 800 Values and Mean')
pyplot.xlabel('Pixels')
pyplot.ylabel('Intensity')
pyplot.show()
