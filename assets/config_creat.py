import os
import json


def creat_config_file(creat_name, creat_last_name):
    fichier = open("./assets/config.json", "a")
    creat_json = json.JSONEncoder().encode({
        "lastname": creat_name, "name": creat_last_name 
        })
    fichier.write(creat_json)
    fichier.close()
    quit()