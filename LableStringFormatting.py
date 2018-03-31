def FindLabel ( [MAPSYMBOL], [Excavation]  ):
    MyLable = "{0} ({1})".format( [MAPSYMBOL] , [Excavation] )
    return MyLable

def FindLabel ( [Name], [TYPE], [Capacity]):
    MyLable = "{0} - {1} ({2} M3)".format( [Name], [TYPE], [Capacity] )
    return MyLable

def FindLabel ( [UNIQUE_ID] , [MAIN_RD_KP], [PROJECT_USAGE]  ):
    MyLable = "{0} ({1}) \n {2}".format( [UNIQUE_ID] , [MAIN_RD_KP], [PROJECT_USAGE]  )
    return MyLable

def FindLabel ( [UNIQUE_ID] ,  [NAME] , [PROJECT_USAGE], [LENGTH_m]   ):
    import locale
    locale.setlocale(locale.LC_ALL, '')
    length =  locale.format("%.2f", float([LENGTH_m]), grouping = True)

    MyLable = "{0} Access \n {1}m".format( [PROJECT_USAGE], length)
    if [UNIQUE_ID] : MyLable = "{0} Access - {1} ({2}) \n {3}m".format( [PROJECT_USAGE] , [UNIQUE_ID] , [NAME], length)
    return MyLable

def FindLabel ( [UNIQUE_ID] ,  [NAME] , [PROJECT_USAGE], [LENGTH_m]   ):
    import locale
    locale.setlocale(locale.LC_ALL, '')
    length =  locale.format("%.2f", float([LENGTH_m]), grouping = True)

    MyLable = "{0} Access \n {1}m".format( [PROJECT_USAGE], length)
    if [UNIQUE_ID] : MyLable = "{0} \n {1}m".format( [UNIQUE_ID] , length)
    return MyLable

def FindLabel ( [NAME] ):
  return [NAME].title()

  UNIQUE_ID IN ('AT175','AT170')

def FindLabel ( [UNIQUE_ID] ,  [NAME] , [PROJECT_USAGE], [LENGTH_m]   ):
    import locale
    locale.setlocale(locale.LC_ALL, '')
    length =  locale.format("%.2f", float([LENGTH_m]), grouping = True)

    MyLable = "{0} Access \n {1}m".format( [PROJECT_USAGE], length)
    if [UNIQUE_ID] : MyLable = "{0} \n {1}m".format( [UNIQUE_ID] , length)
    return MyLable

#Display Expression for Data Driven Pages
from os import path
from arcpy import SearchCursor
base_dir ="C:\Users\scoblem\Documents\ArcGIS\~NGP\GeoDatabase\NGP_MCD_Features.gdb"
feature_class = "Pipeline_Intersections"
fc = path.join(base_dir, feature_class)
cursor = SearchCursor(fc)

def FindLabel ():
  StartPage = list()
  RowCount = int()
  for row in cursor:
    StartPage.append(row.getValue('Page'))
    RowCount += 1
  StartPage.sort()
  PageCount = (RowCount-1) + (StartPage[0])

  return PageCount

# Data Driven Page of Pages
 <dyn type="page" property="name"/> of <dyn type="page" property="expression"/>


value = 0

def autoincrement():
    global value

    if value == 0:
        value = 1
    else:
        value += 1

    return value

autoincrement()
