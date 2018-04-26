from bs4 import BeautifulSoup
import requests


ver_urls = []

# ----------------------Vereins URL--------------------------------------------------------------------------------
# Input Webbbewerbs URL mit der Tabelle . Funktion extrahiert Vereins URLs

def get_verurls(url):
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    for link in soup.find_all('a', {'class': "club-wrapper"}):
        if link.get('href') != None:
            ver_urls.append(link.get('href'))

    return ver_urls

# -----------------------Vereinsseite Scrapen------------------------------------------------------------------------
# Input Vereins URL Output Vereinsadresse und Nmen

def get_veradressen(url):
    # Vereinsname in Titel
    r = requests.get(url)
    html = r.text
    asoup = BeautifulSoup(html, 'lxml')
    title = asoup.find("title").get_text()
    title = title.replace('\n', '')
    # Adresse
    aso = asoup.find(id="teamProfile")
    a = aso.find_all('div', {'class': "column-left"})

    b = a[1].find('div', {'class': "value"})
    b = b.text
    b = b.replace('\t', '')
    # Postfach String entfernen
    if 'Postfach' in b:
        b = b.split(',')
        b = b[1].strip(' ')
    #print(title, ':', b)
    return title, b
