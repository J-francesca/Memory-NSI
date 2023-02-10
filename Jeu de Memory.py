# 1.Le joueur choisit le nombre de carte (le nombre de cartes possible: 16,24,32,48) et le nombre de joueurs(maximum 4);
# 2.Toutes les cartes sont cachées, il y a toujours des paires de cartes qui ont le chiffre identique ou la forme identique;
# 3.Le joueur va choisir deux cartes pour voir si deux cartes sont identiques ou pas ;
# 4.
#  Premier cas:
#      Si les deux cartes sont identiques, l'utilisateur les récupère et il gagne  point;
#  Deuxième cas:
#      Si les deux cartes ne sont pas identiques, les cartes seront recachées et le joueur ne gagne pas de point;
# 5.Ensuite, on recommence à l'étape 3 jusqu'il y a plus de cartes cachées;
# 6.Enfin, on affiche le score du joueur (ou les scores des joueurs). Le jeu est terminé.


# 1. Commence par ignoner cette option et faire 4x4 = 16 (tu verras après coment changer)
# RESTE OK

# demarrer en mode texte

# variable plateau

"""
plateau = [[0 for x in range(4)] for y in range(4)] # liste de listes
print(plateau[2][1]) # ligne 2 col 1 ... Pfffff
"""
from random import randint

CACHE = True
MONTRE = False

plateau = {(x, y): 0 for x in range(4) for y in range(4)}  # dico
#print(plateau[1, 2])  # col 1 (x=1), y = 2

cache_ou_montre = {(x, y): CACHE for x in range(4) for y in range(4)}

def init_plateau():# remplit le plateau avec des paires et les cache
    for x in range(4):
        for y in range(4):
            plateau[(x,y)] = randint(1,8)

    return plateau


def affiche_plateau():  # affiche le plateau avec des '*' pour les cartes cachées
    for x in range(4):
        for y in range(4):
            if cache_ou_montre:
                plateau[(x,y)] ='*'
    return plateau

def demande_joueur(): # demande au joueur une colonne et une ligne
    proposition_1 = int(input("Voulez-vous voir quelle carte? Donnez-moi la colonne:"))
    proposition_2 = int(input("Donnez-moi aussi la ligne correspondante:"))
    return s
plateau_1 =affiche_plateau()
print(plateau_1)
print(demande_joueur())