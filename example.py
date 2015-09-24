import ee

ee.Initialize()

test_geometry = {
  'type': 'Feature',
  'properties': {},
  'geometry': {
    'type': 'Polygon',
    'coordinates': [
      [
        [
          -122.23663330078124,
          37.84883250647402
        ],
        [
          -122.14874267578125,
          37.90736658145496
        ],
        [
          -122.0416259765625,
          37.85316995894978
        ],
        [
          -122.10205078125,
          37.79893346559687
        ],
        [
          -122.23663330078124,
          37.84883250647402
        ]
      ]
    ]
  }
}

def list_images():
    collection = ee.ImageCollection('MODIS/MCD43A4_NDVI')
    value = collection.toList(1000)
    for item in value.getInfo():
        print item['id']

def mean_example():
    feature = ee.Feature(test_geometry)
    raster = ee.Image('MODIS/MCD43A4_NDVI/MCD43A4_005_2015_08_21')
    stats = raster.reduceRegion('mean', feature.geometry())
    print stats.getInfo()
    stats = raster.reduceRegion('min', feature.geometry())
    print stats.getInfo()
    stats = raster.reduceRegion('max', feature.geometry())
    print stats.getInfo()



if __name__ == '__main__':
    list_images()
    mean_example()

