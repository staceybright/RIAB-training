'''
ABOUT: How Python can be used to execute IRAF/PyRAF tasks
DEPENDS: Python 2.7.3
AUTHOR: S N Bright for STScI, 2013
HISTORY: 2013: Test program
USE: python pyraf_example.py
'''

#Load the packages we need
import pyraf, os, glob
from pyraf import iraf
from iraf import noao, digiphot, daophot

#Generate a list of all the fits files
file_list = glob.glob('*_ima.fits')
print file_list

#Loops though all the .fits files
for file in file_list:
    #Test for old files, and remove them if they exist
    file_query = os.access(file + '1.coo.1', os.R_OK)
    if file_query == True:
        os.remove(file + '1.coo.1')
    #Run daofind on one image
    iraf.daofind(
        image = file + '[1]',
        interactive = 'no',
        verify = 'no')

