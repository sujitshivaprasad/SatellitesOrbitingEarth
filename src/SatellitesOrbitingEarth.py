#!/usr/bin/python
''' The data of all of the satellites orbiting the Earth was 
acquired from the UCS Satellite Database located at:
www.ucsusa.org/satellite_database
The version used here is the most recent'''

import pandas as pd
from orbital import earth, KeplerianElements, plot, plot3d
import numpy as np
import math
import matplotlib.pyplot as plt

# read data from excel file
satellites = pd.read_excel('UCS_Satellite_Database_MostRecent.xlsx')
# set index on satellite names, then create dict
satellites.set_index('Name of Satellite, Alternate Names', inplace=True)
sat_dict = satellites.to_dict(orient='index')

# TODO: define these things first: make sure the units are correct.
# https://pythonhosted.org/OrbitalPy/modules/elements/
# trying with one satellite first, then interate over all
period = sat_dict["ABS-3A "]["Period (minutes)"]
semi_major_axis = math.pow(math.pow(period,2), 3)

eccentricity = sat_dict["ABS-3A "]["Eccentricity"]
inclination = sat_dict["ABS-3A "]["Inclination (degrees)"]
longitude = sat_dict["ABS-3A "]["Longitude of GEO (degrees)"]
perigee = sat_dict["ABS-3A "]["Perigee (km)"]; #TODO: Get this from the spreadsheet 
m0 = 0; #TODO: not sure
body = 'earth'; #earth
ref_epoch = 0; #???

orbit = KeplerianElements.with_period(period, body=earth, e=eccentricity, i=inclination, raan=longitude, arg_pe=perigee)
plot(orbit, title='ABS-3A', animate=True)
plt.show()


