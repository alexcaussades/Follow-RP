#!/usr/bin/python3
import os
import json
import help
import sr
import time
from assets import config_creat
from datetime import date
import version
today = date.today()

try:
    with open('./assets/config.json') as mon_fichier:
        data = json.load(mon_fichier)
except (FileNotFoundError):
    print("Absence de fichier de configration sur le logiciel")
    print("Creation du fichier utilisateur !")
    creat_name = input("Votre nom RP ? : ")
    creat_last_name = input("Votre prénom RP ? : ")
    config_creat.creat_config_file(creat_name, creat_last_name)
    print("Votre fichier est configuer relancer le logiciel")

print("Bienvenue sur Follow RP")
print("Besoin d'aide taper: help")

version.versions_serach()

i = 'rr'

try:
    while i :
        a = input("Que voulez-vous faire {0} ? : ".format(data['name']))


        if (a == "creat"):
            req = input("Qu'elle est son nom ? ")
            prenom = input("Qu'elle est son prenom ? ")
            age = input("Qu'elle est son age ? ")
            ville = input("Qu'elle sa ville ? (Si pas disponible (n)) ")
            function = input("Qu'elle est sa fonction ? (doc, citoyen, cherif, autre) ")
            sr.creatplayer(req, age, prenom, ville, function)
        

        if (a == "sr"):
            req = input("Qu'elle personne ? ")
            sr.player(req)
            
        if (a == "edit"):
            req = input("Qu'elle personne ? ")
            information = input("votre nouvelle information ? ")
            sr.editplayer(req, information)

        if (a == 'help'):
            help.help_funtion()
            
        if (a == "exit"):
            quit()
    
except (KeyboardInterrupt):
    print(" Fermeture du logiciel")