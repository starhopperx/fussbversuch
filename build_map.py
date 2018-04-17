import gmplot
import googlemaps


class BuildMap:

    api_key = 'AIzaSyB3OicPc2Q0Vv9q6jGnEYkP44vVw8d_fjY'

    def __init__(self, adressen,home):
        # Adressen Liste
        self.adressen = adressen
        self.home = home

    def main(self):
        gmap = gmplot.GoogleMapPlotter.from_geocode(self.home,zoom=5)
        lat, lon = self.get_latlon(self.home)
        gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"
        gmap.marker(lat, lon, 'tomato', title="Zuhause")

        for a in self.adressen:
            for k, v in a.items():
                lat, lon = self.get_latlon(v)
                gmap.marker(lat, lon, 'cornflowerblue',title=k)

        gmap.draw("map.html")


    """Längen und Breitengrade abrufen"""
    def get_latlon(self,adress):

        gmaps = googlemaps.Client(self.api_key)
        geocode_result = gmaps.geocode(adress)
        print(geocode_result)
        lat = geocode_result[0]["geometry"]["location"]["lat"]
        lon = geocode_result[0]["geometry"]["location"]["lng"]

        return lat, lon


#lat, lon = get_latlon("Wiesensteig")

if __name__ == '__main__':
    adressen = ['\nRichard-Wagner-Str. 31, 75031 Eppingen\n', '\nFasanenstr. 25, 75180 Pforzheim\n','\nZum Stadion 1, 74821 Mosbach\n', '\nLorscher Str. 84, 68519 Viernheim\n','\nPleikartsförster Str. 130, 69124 Heidelberg\n', '\nErbprinzenstr. 52, 75175 Pforzheim\n','\nPostfach 2112, 69240 Mühlhausen\n', '\nPostfach 1429, 76293 Stutensee\n', '\nHertzstr. 23, 76187 Karlsruhe\n','\nSchwetzinger Str. 92, 69190 Walldorf\n', '\nJahnstr. 1, 69207 Sandhausen\n','\nPostfach 310446, 68264 Mannheim\n', '\nSchwetzinger Str. 92, 69190 Walldorf\n','\nJahnstr. 1, 69207 Sandhausen\n', '\nPleikartsförster Str. 130, 69124 Heidelberg\n','\nZum Stadion 1, 74821 Mosbach\n', '\nLorscher Str. 84, 68519 Viernheim\n', '\nPostfach 310446, 68264 Mannheim\n','\nPostfach 2112, 69240 Mühlhausen\n', '\nErbprinzenstr. 52, 75175 Pforzheim\n','\nRichard-Wagner-Str. 31, 75031 Eppingen\n', '\nPostfach 1429, 76293 Stutensee\n','\nHertzstr. 23, 76187 Karlsruhe\n', '\nFasanenstr. 25, 75180 Pforzheim\n']
    bm = BuildMap(adressen, '73770 Denkendorf')
    print(bm.main())

