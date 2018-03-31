import time
from os import path
#import arcpy line 11 so user does not wait to enter path and distance.

# INPUT_PATH = raw_input('Map Path (input): ')
INPUT_PATH = "C:\Users\scoblem\Documents\ArcGIS\~NGP\OfflineMaps\~MXD_to_KML"
# OUTPUT_PATH = raw_input('KML Path (output): ')
START_TIMER = time.time()

print("\nLoading arcpy...")

import arcpy

print("Pre-Processing...")

arcpy.env.workspace = (INPUT_PATH)

print("Processing...\n--------------------------------------------------------")

if len(arcpy.ListFiles('*.mxd')) > 0:
    for mxd in arcpy.ListFiles('*.mxd'):
        dataFrame = 'Layers'
        composite = 'NO_COMPOSITE'
        vector = 'VECTOR_TO_VECTOR'
        pixels = 2048
        dpi = 96
        clamped = 'ABSOLUTE'
        for scale in range(10000, 30001, 10000):
            outKML = mxd[:-4]+'.kmz'
            arcpy.MapToKML_conversion(mxd, dataFrame, outKML, scale,
                                        composite, vector, '' ,pixels, dpi, clamped)

else:
    arcpy.AddMessage('There are no map documents (*.mxd) in {}'.format(INPUT_PATH))

# for dist in distance_list:
#     output_fc = '{}_Buffer_{}_meters'.format(input_fc, dist)
#     arcpy.Buffer_analysis(input_fc, output_fc, '{} meters'.format(dist))
#     print('PROCESSED: {}_Buffer_{}_meters'.format(input_fc, dist))

END_TIMER = (time.time() - START_TIMER)
print("--------------------------------------------------------")
print("Process completed in {} seconds.".format(round(END_TIMER, 2)))
