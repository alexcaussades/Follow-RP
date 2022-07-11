#!/usr/bin/python3
from urllib import request, parse
import json
import os
import webbrowser

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

url = "https://api.github.com/repos/alexcaussades/Follow-RP/releases"

with open('./assets/version.json') as mon_fichier:
        data = json.load(mon_fichier)
        res = request.urlopen(url).read()
        page = res.decode("utf8")
        y = json.loads(page)

def versions_serach():
        
        if(y[0]['name'] != data["version"]):
                print("____________________________________")
                print(bcolors.FAIL + "Une nouvelle version est disponible 🔽:"+ bcolors.RESET )
                print("⏩ Taper la commande : version")

def numero_version():
        print("Vous êtes sur la version : {0}".format(data["version"]))
        if(y[0]['name'] != data["version"]):
                a = input("mettre à jour ? (y/n)")

                if(a == "y"):
                        repro = request.urlopen(y[0]["url"]).read()
                        info = repro.decode("utf8")
                        res = json.loads(info)
                        webbrowser.open(y[0]["html_url"])

