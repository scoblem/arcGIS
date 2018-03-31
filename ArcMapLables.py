#1km KP markers (1:100,000 - <none>)
def FindLabel ( [KP] ):
  return ("KP "+ [KP])

#10km KP markers (1:500,000 - 1:115,000)
def FindLabel ( [KP] ):
    if int(([KP])) % 10 == 0: return ("KP " + [KP])

#50km KP markers (1:2,000,000 - 1:600,000)
def FindLabel ( [KP] ):
    if int(([KP])) % 50 == 0: return ("KP " + [KP])

#100km KP markers inc sol / eol (<none> - 1:2,500,000)
def FindLabel ( [KP] ):
    if int(([KP])) % 100 == 0 or int(([KP])) in [0, 622]: return ("KP " + [KP])

# Access track lables for rail crossing map.
def FindLabel ( [OBJECTID]  , [UNIQUE_ID] , [MAJOR_ASSET_TYPE_DESC] , [MINOR_ASSET_TYPE_DESC]  ):
    if int([OBJECTID]) == 11:
        MyLable = "Proposed Equipment Access"
    elif int([OBJECTID]) == 10:
        MyLable ="Proposed Light Vehicle Access to Warego Rd"
    else:
        MyLable = [UNIQUE_ID]
    return MyLable


# FC: Access Tracks -LABLES
# Lable track with availabe fields only.
def FindLabel ( [UNIQUE_ID] ,  [NAME] , [PROJECT_USAGE], [LENGTH_m]   ):
    Len = round(float( [LENGTH_m] ),2)
    MyLable = "{0} Access".format( [PROJECT_USAGE] )
    if [UNIQUE_ID] : MyLable = "{0} Access - {1} ({2}) {3}".format( [PROJECT_USAGE] , [UNIQUE_ID] , [NAME], Len   )
    return MyLable
