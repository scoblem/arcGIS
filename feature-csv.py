from os import path
from arcpy import SearchCursor

# base_dir ="C:\Users\scoblem\Documents\ArcGIS\~NGP\GeoDatabase\NGP_Master_Rev_01.gdb"
base_dir ="C:\Users\scoblem\Documents\ArcGIS\~NGP\Layers\NGP_Pipeline_RevD.gdb"
feature_class = "Placemarks\Points"
fc = path.join(base_dir, feature_class)

cursor = SearchCursor(fc)

def make_list():
    field_values = list()
    for row in cursor:
        field_values.append(row.getValue('Name'))
    return field_values

def get_duplicates(field_values):
    duplicate_values = list()
    for value in field_values:
        if field_values.count(value) > 1: duplicate_values.append(value)
    duplicate_values.sort()
    return duplicate_values

def get_unique(field_values):
    unique_values = list()
    for value in field_values:
        if field_values.count(value) == 1: unique_values.append(value)
    unique_values.sort()
    return unique_values

def print_attr():


field_val = make_list()
x = get_duplicates(field_val)
y = get_unique(field_val)

print(fc)
print(y)
print("List contains {0} items.".format(len(get_unique(field_val))))
