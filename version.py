#!/usr/bin/python3
from urllib import request, parse
import json
import os

url = "https://api.github.com/repos/alexcaussades/Follow-RP/releases"

with open('./assets/version.json') as mon_fichier:
        data = json.load(mon_fichier)

def versions_serach():
        res = request.urlopen(url).read()
        page = res.decode("utf8")
        y = json.loads(page)

        if(y[0]['name'] != data["version"]):
                print("____________________________________")
                print("Une nouvelle version est disponible sur https://github.com/alexcaussades/Follow-RP/releases")
                print("")
                print("Description de la mise à jour")
                print("\n" + y[0]['body'])
                print("____________________________________")