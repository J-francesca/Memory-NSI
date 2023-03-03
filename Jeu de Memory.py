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
from random import sample, shuffle

CACHE = True
MONTRE = False

plateau = {(x, y): 0 for x in range(4) for y in range(4)}  # dico
# print(plateau[1, 2])  # col 1 (x=1), y = 2
cache_ou_montre = {(x, y): CACHE for x in range(4) for y in range(4)}


def trouve_places_des_paires():
    toutes_les_cases = [(x, y) for x in range(4) for y in range(4)]
    cases_de_premier_elt_de_paire = sample(toutes_les_cases, 8)
    for case in cases_de_premier_elt_de_paire:
        toutes_les_cases.remove(case)
    cases_restantes = toutes_les_cases
    shuffle(cases_restantes)
    return [(cases_de_premier_elt_de_paire[i], cases_restantes[i]) for i in range(8)]


def init_plateau():  # remplit le plateau avec des paires et les cache

    paires = trouve_places_des_paires()

    i = 1
    for x in paires:
        plateau[x[0]] = i
        plateau[x[1]] = i
        i += 1

    cache_ou_montre = {(x, y): CACHE for x in range(4) for y in range(4)}

    return plateau, cache_ou_montre


def demande_joueur():  # demande au joueur une colonne et une ligne
    taille = [x for x in range(8)]
    proposition_1 = -1
    proposition_2 = -1
    proposition_3 = -1
    proposition_4 = -1
    while proposition_1 not in taille:
        proposition_1 = int(input("Voulez-vous choisir quelle carte? Donnez-moi la position de la colonne:"))
    while proposition_2 not in taille:
        proposition_2 = int(input("Donnez-moi aussi la ligne correspondante:"))
    print("Donnez-moi également la position de la deuxième carte.")
    while proposition_3 not in taille:
        proposition_3 = int(input("La colonne:"))
    while proposition_4 not in taille:
        proposition_4 = int(input("Quelle ligne?"))

    return proposition_1, proposition_2, proposition_3, proposition_4


def jouer():
    reponse_1, reponse_2, reponse_3, reponse_4 = demande_joueur()
    plateau = init_plateau()

    plateau[1][reponse_1, reponse_2] = False
    plateau[1][reponse_3, reponse_4] = False

    choix_1 = plateau[0][reponse_1, reponse_2]
    choix_2 = plateau[0][reponse_3, reponse_4]
    return choix_1, choix_2, plateau


def score():
    score = 0
    choix = jouer()
    if choix[0] == choix[1]:
        score += 2
        print("Vous avez trouvé les mêmes cartes.")
    else:
        score -= 1
        print("Vous n'avez pas trouvé les mêmes cartes. Réessayez!")

    while score < 0:
        score = 0


def affiche_plateau():  # affiche le plateau avec des '*' pour les cartes cachées
    reponse = jouer()
    for x in range(4):
        for y in range(4):
            if reponse[2][1][x, y]:
                reponse[2][0][x, y] = '*'


trouve_places_des_paires()
init_plateau()

score()
affiche_plateau()

print(plateau)
