# 1.Le joueur choisit le nombre de carte (le nombre de cartes possibles: 16,24,32,48) et le nombre de joueurs(maximum 4);
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


def trouve_places_des_paires():
    toutes_les_cases = [(x, y) for x in range(4) for y in range(4)]
    cases_de_premier_elt_de_paire = sample(toutes_les_cases, 8)
    for case in cases_de_premier_elt_de_paire:
        toutes_les_cases.remove(case)
    cases_restantes = toutes_les_cases
    shuffle(cases_restantes)
    return [(cases_de_premier_elt_de_paire[i], cases_restantes[i]) for i in range(8)]


def init_plateau():  # remplit le plateau avec des paires et les cache
    plateau = {(x, y): 0 for x in range(4) for y in range(4)}
    paires = trouve_places_des_paires()

    i = 1
    for x in paires:
        plateau[x[0]] = i
        plateau[x[1]] = i
        i += 1

    cache_ou_montre = {(x, y): CACHE for x in range(4) for y in range(4)}

    return plateau, cache_ou_montre


def demande_joueur():  # demande au joueur une colonne et une ligne (position de la carte)
    taille = [x for x in range(8)]
    proposition_1 = -1
    proposition_2 = -1
    while proposition_1 not in taille:
        proposition_1 = int(input("Voulez-vous choisir quelle carte? Donnez-moi la position de la colonne:"))
    while proposition_2 not in taille:
        proposition_2 = int(input("Donnez-moi aussi la ligne correspondante:"))

    return proposition_1, proposition_2


def affiche_plateau(plateau, cache):  # affiche le plateau
    for x in range(4):
        for y in range(4):
            if cache[x, y] is not False:
                print("*", end=" ")
            elif cache[x, y] == None:
                print(" ", end=" ")
            else:
                print(plateau[x, y], end=" ")
        print()


def jouer():
    plateau, cases_cachees = init_plateau()
    while True in cases_cachees.values():
        affiche_plateau(plateau, cases_cachees)
        print()
        reponse_1, reponse_2 = demande_joueur()
        print()
        cases_cachees[reponse_1, reponse_2] = False
        affiche_plateau(plateau, cases_cachees)

        print()
        print("Donnez-moi également la position de la deuxième carte.")
        print()

        reponse_3, reponse_4 = demande_joueur()
        while reponse_1 == reponse_3 and reponse_2 == reponse_4:
            print("Vous avez saisi la même carte.")
            reponse_3, reponse_4 = demande_joueur()
        cases_cachees[reponse_3, reponse_4] = False
        affiche_plateau(plateau, cases_cachees)

        choix_1 = plateau[reponse_1, reponse_2]
        choix_2 = plateau[reponse_3, reponse_4]
        score(choix_1, choix_2)

        print()
        if choix_1 != choix_2:
            print("Vous n'avez pas trouvé les mêmes cartes.")
            print()
            cases_cachees[reponse_1, reponse_2] = True
            cases_cachees[reponse_3, reponse_4] = True
        else:
            print("Vous avez trouvé les mêmes cartes.")
            print()
            cases_cachees[reponse_1, reponse_2] = None
            cases_cachees[reponse_3, reponse_4] = None


def score(choix_1, choix_2):  # compte le nombre de points que le joueur a gagné
    point = 0
    if choix_1 == choix_2:
        point += 2
        print(choix_1, choix_2)
        print("Bravo!")
    else:
        point -= 1
        print("Réessayez!")

    while point < 0:
        point = 0

    return print(f"Le joueur a gagné", point, "points.") if point > 0 else print("Vous n'avez gagné aucun point.")


jouer()
