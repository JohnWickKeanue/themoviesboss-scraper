import time
from bs4 import BeautifulSoup
import requests

url = "https://themoviesboss.mx/movies/avatar-the-way-of-water-2/"

def flix(url):
    client = requests.session()
    r = client.get(url).text
    soup = BeautifulSoup (r, "html.parser")
    links = soup.select('a[href^="https://themoviesboss.mx/links/"]')
    gd_txt = f"Total Links Found : {len(links)}\n\n"
    for a in links:
       link = a["href"]
       r = client.get(link)
       soup = BeautifulSoup(r.text, "html.parser")
       links1 = soup.select('a[href^="https://links.inbbotlist.com/links/"]')
       for a in links1:
           link = a["href"]
           r = client.get(link)
           soup = BeautifulSoup(r.text, "html.parser")
           links = soup.select('a[href^="https://filepress.lol/file/"]')
           for a in links:
                 link = a["href"]
                 print(link)
    
print(flix(url))
