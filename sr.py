import os


def player(req):
    try:
        fichier = open("./player/"+ req +".txt", "r")
        print("------------------------------------")
        print (fichier.read())
        print("------------------------------------")
        fichier.close()   
    except (FileNotFoundError):
        print("Aucune personne, n'a était trouver ! vous pouvez la crée avec la fonction creat ;)")
    
        


def editplayer(req, information):
    fichier = open("./player/"+ req +".txt", "a")
    fichier.write("\n"+ information)
    print("Le fichier à bien était mis à jours, pour le joueur "+ req +" !")
    fichier.close()

def creatplayer(req, age, prenom, ville, function):
    fichier = open("./player/"+ req +".txt", "a")
    fichier.write("Name: " + req + "\n" "LastName: " + prenom + "\n" "Age: " + age + "\n" "ville: " + ville + "\n" "fonction: " + function + "\n")
    fichier.close()
