import requests
import json
import os


with open('./assets/version.json') as mon_fichier:
        data = json.load(mon_fichier)

def versions_serach():
    x = requests.get("https://api.github.com/repos/alexcaussades/Follow-RP/releases")
    
    y = json.loads(x.text)
  
    if(y[0]['name'] != data["version"]):    
       print("____________________________________")
       print("Une nouvelle version est disponible sur https://github.com/alexcaussades/Follow-RP/releases")
       print("")
       print("Description de la mise à jour")
       print("\n" + y[0]['body'])
       print("____________________________________")
       