from random import sample, shuffle

CACHE = 1
MONTRE = 0
TROUVE = 2


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
            if cache[x, y] == CACHE:
                print("*", end=" ")
            elif cache[x, y] == TROUVE:
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
        if score(choix_1, choix_2) == True:
            cases_cachees[reponse_1, reponse_2] = TROUVE
            cases_cachees[reponse_3, reponse_4] = TROUVE
            # il faut dire que les cases choix_1 et choix_2 sont TROUVE

        print()
        if choix_1 != choix_2:
            print("Vous n'avez pas trouvé les mêmes cartes.")
            print()
            cases_cachees[reponse_1, reponse_2] = True
            cases_cachees[reponse_3, reponse_4] = True



def score(choix_1, choix_2) -> bool:
    il_a_trouve = False
    point = 0
    if choix_1 == choix_2:
        il_a_trouve = True
        point += 2
        print("Bravo!")
    else:
        point -= 1
        print("Réessayez!")

    while point < 0:
        point = 0

    print(f"Le joueur a gagné", point, "points.") if point > 0 else print("Vous n'avez gagné aucun point.")
    return il_a_trouve




jouer()
