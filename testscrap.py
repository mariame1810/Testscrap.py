import requests
from bs4 import BeautifulSoup
import time
"""
links = []
#compte le nombre de balise div
for i in range(50) :
    url = 'https://www.matchendirect.fr/statistique.html/'
    r = requests.get(url)
    print(r)
    if r.ok:
        print('Page:' + str(i))
        soup = BeautifulSoup(r.text, 'lxml')
        divs = soup.find_all('div')

        for div in divs:
            a = div.find('a')
            if a is not None:  # Vérification si la balise <a> est trouvée
                a=div.find('a')
                link=a['href'] # Utilisation de la méthode get() pour accéder à l'attribut 'href'
                links.append('https://www.matchendirect.fr/'+link)
        #time.sleep(3)
print(len(links))

with open('urls.txt', 'w') as file:
    for link in links:
        file.write(link + '\n')
"""
"""
with open('urls.txt', 'r') as file:
#OU file = open('urls.txt', 'r') identique mais avec with le fichier se ferme lorsqu'on quitte
    for row in file:
        print(row)
"""

url = 'https://www.matchendirect.fr/statistique/fc-barcelone-contre-real-madrid.html'
r = requests.get(url)
if r.ok:
    soup=BeautifulSoup(r.text, 'lxml')
    c=soup.find('span',{'class':'ico_competition'})
    print ('Titre : ' + c.text)
