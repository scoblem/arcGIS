PATH = raw_input('Feature Path: ')
DISTANCE = raw_input('Buffer Distances (m): ')

import arcpy
from os import path

arcpy.env.workspace = path.dirname(PATH)
input_fc = path.basename(PATH)
distance_list = DISTANCE.split(', ')

for dist in distance_list:
    output_fc = '{}_Buffer_{}_meters'.format(input_fc, dist)
    arcpy.Buffer_analysis(input_fc, output_fc, '{} meters'.format(dist))
    print('PROCESSED: {}_Buffer_{}_meters'.format(input_fc, dist))
