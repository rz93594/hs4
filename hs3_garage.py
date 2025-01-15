# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 12:27:45 2016

@author: potter
"""

import json
#import urllib
from urllib.request import urlopen
import sys
import getopt


o  = sys.argv[1]

# Read command line args
myopts, args = getopt.getopt(sys.argv[1:],"i:o:")
 
###############################
# o == option
# a == argument passed to the o
###############################

if o == 'UP':
        data = json.load(urlopen('http://<URL>/JSON?request=controldevicebyvalue&ref=304&value=75'))
elif o == 'DOWN':
        data = json.load(urlopen('http://<URL>/JSON?request=controldevicebyvalue&ref=304&value=0'))
else:
        print("failed")
 
# Display input and output file name passed as the args
