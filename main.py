#!/usr/bin/python3
import os
import json
import help
import sr
import time
import sqlite3
from assets import config_creat
from datetime import date
import version
today = date.today()

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

try:
    with open('assets/config.json') as mon_fichier:
        data = json.load(mon_fichier)
except (FileNotFoundError):
    print("Absence de fichier de configration sur le logiciel")
    print("Creation du fichier utilisateur !")
    creat_name = input("Votre nom RP ? : ")
    creat_last_name = input("Votre prénom RP ? : ")
    print("Votre fichier est configurer relancer le logiciel")
    config_creat.creat_config_file(creat_name, creat_last_name)
    
print("Bienvenue sur Follow RP")
print("Besoin d'aide taper: help")

version.versions_serach()




i = 'rr'

try:
    while i :

        a = input("Que voulez-vous faire {0} ? : ".format(data['name']))

        a = a.split()

        if (a[0] == "creat"):
            try:
                req = a[1]
                prenom = input("Qu'elle est son prenom ? ")
                age = input("Qu'elle est son age ? ")
                ville = input("Qu'elle sa ville ? (Si pas disponible (n)) ")
                function = input("Qu'elle est sa fonction ? (doc, citoyen, cherif, autre) ")
                sr.creatplayer(req, age, prenom, ville, function)
            except:
                print("Manque information player")
        

        if (a[0] == "sr"):
            try:
                req = a[1]
                sr.player(req)
            except:
                print("Manque information player")
            
        if (a[0] == "edit"):
            try:
                req = a[1]
                information = input("votre nouvelle information ? ")
                sr.editplayer(req, information)
            except: 
                print("Manque information player")

        if (a[0] == 'help'):
            help.help_funtion()

        if (a[0] == 'version'):
            version.numero_version()
            
        if (a[0] == "exit"):
            quit()
    
except (KeyboardInterrupt): 
    print(" Fermeture du logiciel")