import ee

# Trigger the authentication flow
#ee.Authenticate()

# Initialize the library
#ee.Initialize()

# vegetation data
veg = ee.ImageCollection("LANDSAT/LE07/C01/T1_8DAY_NDVI")

startDate = '2017-01-01'
stopDate = '2022-01-01'

# filter veg data by start and stop date
veg = veg.select('NDVI').filterDate(startDate, stopDate)

# coordinates for Ormond Beach, FL
lon = -81.075
lat = 29.286389

# center around Ormond Beach
poi = ee.Geometry.Point(lon, lat)

roi = poi.buffer(1e4)

# Reduce the veg collection to average value to make image of
veg_img = veg.mean()

# create url for map
# create green to red color palatte. green --> more vegetated; red --> less vegetated
url = veg_img.getThumbUrl({
    'min': 0.0, 'max': 1.0, 'dimensions': 1024, 'region': roi,
    'palette': ['FFFFFF', 'CE7E45', 'DF923D', 'F1B555', 'FCD163', '99B718', '74A901',
    '66A000', '529400', '3E8601', '207401', '056201', '004C00', '023B01',
    '012E01', '011D01', '011301']})

print(url)
