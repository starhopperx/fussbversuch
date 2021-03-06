import pprint
import build_map

# adressen = ['\nRichard-Wagner-Str. 31, 75031 Eppingen\n', '\nFasanenstr. 25, 75180 Pforzheim\n','\nZum Stadion 1, 74821 Mosbach\n', '\nLorscher Str. 84, 68519 Viernheim\n','\nPleikartsförster Str. 130, 69124 Heidelberg\n', '\nErbprinzenstr. 52, 75175 Pforzheim\n','\nPostfach 2112, 69240 Mühlhausen\n', '\nPostfach 1429, 76293 Stutensee\n', '\nHertzstr. 23, 76187 Karlsruhe\n','\nSchwetzinger Str. 92, 69190 Walldorf\n', '\nJahnstr. 1, 69207 Sandhausen\n','\nPostfach 310446, 68264 Mannheim\n', '\nSchwetzinger Str. 92, 69190 Walldorf\n','\nJahnstr. 1, 69207 Sandhausen\n', '\nPleikartsförster Str. 130, 69124 Heidelberg\n','\nZum Stadion 1, 74821 Mosbach\n', '\nLorscher Str. 84, 68519 Viernheim\n', '\nPostfach 310446, 68264 Mannheim\n','\nPostfach 2112, 69240 Mühlhausen\n', '\nErbprinzenstr. 52, 75175 Pforzheim\n','\nRichard-Wagner-Str. 31, 75031 Eppingen\n', '\nPostfach 1429, 76293 Stutensee\n','\nHertzstr. 23, 76187 Karlsruhe\n', '\nFasanenstr. 25, 75180 Pforzheim\n']
# bm = build_map.BuildMap(adressen, '73770, Denkendorf')
# bm.main()
test = {'CFC Hertha (B-Junioren)': 'Nordhauser Str. 23, 10589 Berlin',
    'SV Empor Berlin (B-Junioren)': 'Cantianstr. 24, 10437 Berlin',
    '1.FC Wilmersdorf (B-Junioren)': 'Blissestr. 20 B, 10713 Berlin',
    'FC Internationale (B-Junioren)': 'Priesterweg 2, 10829 Berlin',
    'TSV Rudow (B-Junioren)': 'Neuköllner Str. 277, 12357 Berlin'}

for key,val in test.items():
    print(key, 'is the key for ', val)

'''
-------------------------------------------
s = 'Postfach 2112, 69240 Mühlhausen'

if 'Postfach' in s:
    s=s.split(',')
    s= s[1].strip(' ')
    print(s)

----------------------------------------------


data = {'Gebiet': {'1': {'1': {'_0123456789ABCDEF0123456700004010': 'Deutschland'},
                  '2': {'_0123456789ABCDEF0123456700004010': 'Deutschland'},
                  '4': {'_0123456789ABCDEF0123456700004010': 'Deutschland'},
                  '43': {'_0123456789ABCDEF0123456700004010': 'Deutschland'},
                  '6': {'_0123456789ABCDEF0123456700004010': 'Deutschland'}},
            '10': {'4': {'_0123456789ABCDEF0123456700004010': 'Deutschland'}},
            '3': {'1': {'_0123456789ABCDEF0123456700004010': 'Deutschland'},
                  '4': {'_0123456789ABCDEF0123456700004010': 'Deutschland'},
                  '6': {'_0123456789ABCDEF0123456700004010': 'Deutschland'}},
            '4': {'1': {'_0123456789ABCDEF0123456700004010': 'Deutschland'},
                  '2': {'_0123456789ABCDEF0123456700004010': 'Deutschland'},
                  '4': {'_0123456789ABCDEF0123456700004010': 'Deutschland'},
                  '6': {'_0123456789ABCDEF0123456700004010': 'Deutschland'}},
            '6': {'1': {'_0123456789ABCDEF0123456700004010': 'Deutschland'},
                  '4': {'_0123456789ABCDEF0123456700004010': 'Deutschland'},
                  '6': {'_0123456789ABCDEF0123456700004010': 'Deutschland'}},
            '7': {'1': {'_0123456789ABCDEF0123456700004010': 'Deutschland'},
                  '4': {'_0123456789ABCDEF0123456700004010': 'Deutschland'},
                  '6': {'_0123456789ABCDEF0123456700004010': 'Deutschland'}},
            '8': {'4': {'_0123456789ABCDEF0123456700004010': 'Deutschland'},
                  '6': {'_0123456789ABCDEF0123456700004010': 'Deutschland'}}},
 'Mannschaftsart': {'_1': 'Herren',
                    '_10': 'D-Junioren',
                    '_3': 'A-Junioren',
                    '_4': 'Frauen',
                    '_6': 'B-Junioren',
                    '_7': 'B-Juniorinnen',
                    '_8': 'C-Junioren'},
 'Spielklasse': {'1': {'_1': 'Bundesliga',
                       '_2': '2.Bundesliga',
                       '_4': 'Regionalliga',
                       '_43': '3.Liga',
                       '_6': 'Oberliga'},
                 '10': {'_4': 'Regionalliga'},
                 '3': {'_1': 'Bundesliga',
                       '_4': 'Regionalliga',
                       '_6': 'Oberliga'},
                 '4': {'_1': 'Bundesliga',
                       '_2': '2.Bundesliga',
                       '_4': 'Regionalliga',
                       '_6': 'Oberliga'},
                 '6': {'_1': 'Bundesliga',
                       '_4': 'Regionalliga',
                       '_6': 'Oberliga'},
                 '7': {'_1': 'Bundesliga',
                       '_4': 'Regionalliga',
                       '_6': 'Oberliga'},
                 '8': {'_4': 'Regionalliga', '_6': 'Oberliga'}}}

wam_url = {'145': {'0123456789ABCDEF0123456700004180': {'_http://www.fussball.de/spieltagsuebersicht/bfv-b-junioren-verbandsliga-baden-b-junioren-verbandsliga-b-junioren-saison1718-baden/-/staffel/020DR2R3U0000002VS54898DVTQF3A0H-G': 'bfv-B-Junioren ''Verbandsliga'}},
            '146': {'0123456789ABCDEF0123456700004180': {'_http://www.fussball.de/spieltagsuebersicht/bfv-b-junioren-landesliga-mittelbaden-baden-b-junioren-landesliga-b-junioren-saison1718-baden/-/staffel/020EQ1DN3O00000DVS54898DVTQF3A0H-G': 'bfv-B-Junioren '
                                                                                                                                                                                              'Landesliga '
                                                                                                                                                                                              'Mittelbaden'},
                                                        {'_http://www.fussball.de/spieltagsuebersicht/bfv-b-junioren-landesliga-odenwald-baden-b-junioren-landesliga-b-junioren-saison1718-baden/-/staffel/020EQ1DMFC00000CVS54898DVTQF3A0H-G': 'bfv-B-Junioren '
                                                                                                                                                                                           'Landesliga '
                                                                                                                                                                                           'Odenwald'},
                                                        {'_http://www.fussball.de/spieltagsuebersicht/bfv-b-junioren-landesliga-rhein-neckar-baden-b-junioren-landesliga-b-junioren-saison1718-baden/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G': 'bfv-B-Junioren ''Landesliga '}}}

    w_key = wam_url["146"]["0123456789ABCDEF0123456700004180"]

w_new = {v: k for k, v in w_key.items()}
print(w_new)


             #Verband Kürzel definieren
bundeslaender = {"Deutschland": "_89", "Baden": "_32", "Bayern": "_31", "Berlin": "_66", "Brandenburg": "_61", "Bremen": "_02", "Wuerttemberg": "_35"}

#Saison definieren
saison = {"Aktuell": "_1718"}

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
wam_arten = data
print(wam_arten["Mannschaftsart"])

in_mannschaftsart = input("Mannschaftsart ? ")
for k, m in wam_arten["Mannschaftsart"].items():
    if m == in_mannschaftsart:
        in_mak = k
#wam_wettbewerbsurls = get_wettbewerbsurl(bundeslaender[in_verband], saison[in_saison], in_mak)
#pprint.pprint(wam_wettbewerbsurls)

# 5. Spielklasse

print(wam_arten["Spielklasse"][in_mak.strip("_")])
in_spielklasse = input("Spielkasse ? ")
spielklasse_id = wam_arten["Spielklasse"][in_mak.strip("_")]
for a, b in wam_arten["Spielklasse"][in_mak.strip("_")].items():
    if b == in_spielklasse:
        spielklasse_id = a

print(spielklasse_id.strip("_"))

# 6. Gebiet  --- Mannschaftsart [in_mak] u. Spielkasse [spielklasse_id] ID's werden benötigt
print(wam_arten["Gebiet"][in_mak.strip("_")][spielklasse_id.strip("_")])
in_gebiet = input("Gebiet ? ")
gebiet_id = wam_arten["Gebiet"][in_mak.strip("_".items)][spielklasse_id][in_gebiet]
print(gebiet_id)


#get_wettbewerbsurl(get_mannschaftsart(saison["Aktuell"],bundeslaender["Wuerttemberg"],"B-Junioren"))

'''
