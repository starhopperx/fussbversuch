import gmplot
import googlemaps


#Adressen Liste

adressen = ["STADIONSTR. 5, 89073 ULM", "TALSTR. 17, 71691 FREIBERG AM NECKAR","TÜBINGER STR. 71, 72336 BALINGEN", "MERCEDESSTR. 109, 70372 STUTTGART","JAHNSTR. 1, 69207 SANDHAUSEN"]

"""Längen und Breitengrade abrufen"""
def get_latlon(adress):

    gmaps = googlemaps.Client(key='AIzaSyB3OicPc2Q0Vv9q6jGnEYkP44vVw8d_fjY')


    geocode_result = gmaps.geocode(adress)

    lat = geocode_result[0]["geometry"]["location"]["lat"]
    lon = geocode_result[0]["geometry"]["location"]["lng"]
    #test - print results
    return lat, lon


lat, lon = get_latlon("Wiesensteig")


#print (lat,lon)

gmap = gmplot.GoogleMapPlotter.from_geocode("73770 Denkendorf")

gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"


gmap.marker(lat, lon, 'tomato', title="Test")

for a in adressen:
    lat, lon = get_latlon(a)
    gmap.marker(lat, lon, 'cornflowerblue')


gmap.draw("map.html")