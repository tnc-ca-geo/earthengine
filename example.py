import ee

ee.Initialize()

def show(input):
    print input

if __name__ == '__main__':
    collection = ee.ImageCollection('MODIS/MCD43A4_NDVI')
    value = collection.toList(1000)
    for item in value.getInfo():
        print item['id']
