# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 13:43:57 2020

@author: jreynolds
"""
# created this script to incorporate recent modifications to bike network, this will no longer be necessary going forward

import arcpy

full_network = r"E:\Scratch\\BikePedAuto_NewFields.shp"

# Add BikePlus, Bike_L, Bike_R Field to Bike Network Feature Class -JR
arcpy.AddField_management(full_network, field_name="BikePlus", field_type='Text')

# use search cursor to process bike attribute
bike_facilities = ['1','1A','1B','1C','2','2A','2B', '3A', '3B']


fields = ['BikeNetwor', 'RoadClass', 'BIKE_L', 'BIKE_R', 'BikePlus']
with arcpy.da.UpdateCursor(full_network, fields) as cursor:
    for row in cursor:
        
        
        # Modified to use "or" instead of "and"
        if row[2]in bike_facilities or row[3] in bike_facilities:
            row[4] = 'Y'
        else:
            row[4] = 'N'
            
        
        # Local, rural, neighborhood roads
        if row[1] == '11 Other Local, Neighborhood, Rural Roads':
            row[0] = 'Y'
        
        # Use entire road network except Highways, interstates, ramps to determine basic bike network
        if row[1] not in [ '1 Interstates', '2 US Highways, Separated', '4 Major State Highways, Separated', '7 Ramps, Collectors']:
            row[0] = 'Y'
        
        
        cursor.updateRow(row)