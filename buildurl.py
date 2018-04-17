import requests
import json
import pprint
import scrapingfussbde
import  build_map


#Verband Kürzel definieren
bundeslaender = {"Deutschland": "_89", "Baden": "_32", "Bayern": "_31", "Berlin": "_66", "Brandenburg": "_61", "Bremen": "_02", "Wuerttemberg": "_35"}

#Saison definieren
saison = {"Aktuell": "_1718"}



def walk_dict(d):
    for k,v in d.items():
        if isinstance(v, dict):
            walk_dict(v)
        else:
            print(k,"---", v)

#Die erste AjaxUrl Input Saison und Bundesland-> Antwort Mannschaftsart,Spielklasse,Gebiet
# Return URL mit Mannschaftsart
def get_mannschaftsart(saison, bundesland):


    s = saison
    b = bundesland

    #letzte 1 in der url ist Punkt 3. "Typ" Wir brauchen nur Meisterschaft
    ajaxurl = "http://www.fussball.de/wam_arten" + b + s + "_1.json"

    response = requests.get(ajaxurl)
    #response = requests.get("http://www.fussball.de/wam_wettbewerbsurls_89_1718_1_1.json")
    #response = requests.get("http://www.fussball.de/ajax.actual.table/-/staffel/020AG56UI8000000VS54898DVUVCCN5J-G")
    data = response.json()

    return data


#Die Wettbewerbsurl was wird abgerufen ?
def get_wettbewerbsurl(bundesland, saison, mannschaftsart):
    b = bundesland
    s = saison
    m = mannschaftsart
    #print("http://www.fussball.de/wam_wettbewerbsurls"+ b + s + "_1"+ m + ".json")

    response = requests.get("http://www.fussball.de/wam_wettbewerbsurls"+ b + s + "_1"+ m + ".json")
    data = response.json()

    #print("----------------------------------")
    #print("http://www.fussball.de/wam_wettbewerbsurls"+ b + s + "_1"+ m + ".json)
    #pprint(data)
    #print("---------------------------------")

    return data

#-------------------------------------Auswahl wie in Fussball.de---------------------------------------
# 1. Verband
# 2. Saison
# 3. Typ .... zB Meisterschaft, Pokal etc Da können wir Meisterschaft als Default nehmen
# 4. Mannschaftsart C-Jugend, B-Jugend etc.
# 5. Spielklasse
# 6. Gebiet
# 7. Wettbewerb

# 1.
print(bundeslaender.keys())
in_verband = input("Welcher Verband ? ")
print(bundeslaender[in_verband])
# 2.
print(saison.keys())
in_saison = input("Welche Saison ? ")
print(saison[in_saison])

# 4. Mannschaftsart  --- Antwort beinhaltet 4., 5., 6. Gebiet -----3. Skipped
wam_arten = get_mannschaftsart(saison[in_saison], bundeslaender[in_verband])
print(wam_arten["Mannschaftsart"])

in_mannschaftsart = input("Mannschaftsart ? ")
for k, m in wam_arten["Mannschaftsart"].items():
    if m == in_mannschaftsart:
        in_mak = k
wam_wettbewerbsurls = get_wettbewerbsurl(bundeslaender[in_verband], saison[in_saison], in_mak)
#pprint.pprint(wam_wettbewerbsurls)

# 5. Spielklasse

print(wam_arten["Spielklasse"][in_mak.strip("_")])
in_spielklasse = input("Spielkasse ? ")
spielklasse_id = wam_arten["Spielklasse"][in_mak.strip("_")]
for a, b in wam_arten["Spielklasse"][in_mak.strip("_")].items():
    if b == in_spielklasse:
        spielklasse_id = a

print(spielklasse_id)

# 6. Gebiet  --- Mannschaftsart [in_mak] u. Spielkasse [spielklasse_id] ID's werden benötigt
swap_gebiet = {v: k for k, v in wam_arten["Gebiet"][in_mak.strip("_")][spielklasse_id.strip("_")].items()}
print(swap_gebiet)
in_gebiet = input("Gebiet ? ")
gebiet_id = swap_gebiet[in_gebiet]


# 7. Wettbewerb
swap_wettbewerb = {}
for k, v in wam_wettbewerbsurls[spielklasse_id.strip("_")][gebiet_id.strip("_")].items():
    swap_wettbewerb[v]=k

print(swap_wettbewerb.keys())

in_wettbewerb = input("Wettbewerb ? ")
wettb_url = swap_wettbewerb[in_wettbewerb].strip("_")
print(wettb_url)


# URL aufrufen und Vereine extrahieren
verurls = scrapingfussbde.get_verurls(wettb_url)




# Vereinsseite aufrufen und Adresse extrahieren
adressen=[]
for a in verurls:
    adressen.append(scrapingfussbde.get_veradressen(a))

bm = build_map.BuildMap(adressen, 'Wiesensteig')
bm.main()


