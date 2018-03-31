import time
START_TIMER = time.clock()
PATH = raw_input('Feature Path: ')
DISTANCE = raw_input('Buffer Distances (m): ')

print("\nSlowy importing arcpy module...")

import arcpy
from os import path

print("Pre-Processing...")

arcpy.env.workspace = path.dirname(PATH)
input_fc = path.basename(PATH)
distance_list = DISTANCE.split(', ')

print("Processing...\n--------------------------------------------------------")

for dist in distance_list:
    output_fc = '{}_Buffer_{}_meters'.format(input_fc, dist)
    arcpy.Buffer_analysis(input_fc, output_fc, '{} meters'.format(dist))
    print('PROCESSED: {}_Buffer_{}_meters'.format(input_fc, dist))

END_TIMER = round((time.clock() - START_TIMER), 2)
print("--------------------------------------------------------")
print("Process completed in {} seconds.".format(END_TIMER))
