from poo import *


grille = Grille() # fabrique la grille
# est-ce que l'objet grille possède des methodes pour jouer
# si oui ton code va être
# grille.joue() <----- fait tout.
# sinon

while not grille.fini():
    grille.demande()
    grille.joue()
    print(grille)
    grille.changer_etat()
    print(grille)



