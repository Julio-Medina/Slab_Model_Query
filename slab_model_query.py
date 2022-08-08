#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 08:08:04 2021

@author: julio
"""
import numpy as np
from numpy import genfromtxt
import sys
slab_model_data=genfromtxt('./cam_slab2_dep_02.24.18.xyz', delimiter=',')
slab_model_data=np.transpose(slab_model_data)
longitude_list=slab_model_data[0]-360
latitude_list=slab_model_data[1]
depth_list=slab_model_data[2]
latitude=float(sys.argv[1])
longitude=float(sys.argv[2])
#B=np.isclose()
longitude_value_positions,=np.where(np.isclose(longitude_list,longitude,atol=0.025))
depth_positions_rp,=np.where(np.isclose(latitude_list[longitude_value_positions],latitude,atol=0.025))
depths=depth_list[longitude_value_positions][depth_positions_rp]
#test_slab_data=np.transpose(slab_model_data)
print(longitude_list[longitude_value_positions][depth_positions_rp])
print(latitude_list[longitude_value_positions][depth_positions_rp])
print(depths)
print('Slab model depth: ',np.average(depths))