from Constants_Jeu_de_Memory import *
from random import sample, shuffle


class Grille:

    def __init__(self):

        # contenu vide
        self.contenu = {(x, y): 0 for x in range(NB_DE_COLONNE) for y in range(NB_DE_LIGNE)}

        # on remplit contenu avec des paires
        toutes_les_cases = [(x, y) for x in range(NB_DE_COLONNE) for y in range(NB_DE_LIGNE)]
        cases_de_premier_elt_de_paire = sample(toutes_les_cases, NB_PAIRES)
        for case in cases_de_premier_elt_de_paire:
            toutes_les_cases.remove(case)
        cases_restantes = toutes_les_cases
        shuffle(cases_restantes)
        for i in range(NB_PAIRES):
            self.contenu[cases_de_premier_elt_de_paire[i]] = i
            self.contenu[cases_restantes[i]] = i
        self.proposition_x1 = -1
        self.proposition_y1 = -1
        self.proposition_x2 = -1
        self.proposition_y2 = -1
        # au départ toutes les cartes sont cachées
        self.etat = {(x, y): CACHE for x in range(NB_DE_COLONNE) for y in range(NB_DE_LIGNE)}

    def __str__(self):  # affichage
        affiche = ""
        for x in range(NB_DE_LIGNE):
            for y in range(NB_DE_COLONNE):
                if self.etat[x, y] == CACHE:
                    affiche = affiche + "* "
                elif self.etat[x, y] == MONTRE:
                    affiche = affiche + str(self.contenu[x, y]) + " "
                else:
                    affiche = affiche + " " + " "
            affiche += "\n"
        return affiche

    def demande(self):
        taille = [x for x in range(NB_DE_LIGNE)]
        while self.proposition_x1 not in taille:
            self.proposition_x1 = int(input("Voulez-vous choisir quelle carte? Donnez-moi la position de la colonne:"))
        while self.proposition_y1 not in taille:
            self.proposition_y1 = int(input("Donnez-moi aussi la ligne correspondante:"))
        while self.proposition_x2 not in taille:
            self.proposition_x2 = int(input("Voulez-vous choisir quelle carte? Donnez-moi la position de la colonne:"))
        while self.proposition_y2 not in taille:
            self.proposition_y2 = int(input("Donnez-moi aussi la ligne correspondante:"))
        while self.proposition_x1 == self.proposition_x2 and self.proposition_y1 == self.proposition_y2:
            print()
            self.proposition_x2 = int(input("Voulez-vous choisir quelle carte? Donnez-moi la position de la colonne:"))

            self.proposition_y2 = int(input("Donnez-moi aussi la ligne correspondante:"))
        return self.proposition_x1, self.proposition_y1, self.proposition_x2, self.proposition_y2

    def joue(self):  # fait jouer toute la partie

        if self.etat[self.proposition_x1, self.proposition_y1] == CACHE:
            self.etat[self.proposition_x1, self.proposition_y1] = MONTRE

        print("Donnez-moi également la position de la deuxième carte.")

        if self.etat[self.proposition_x2, self.proposition_y2] == CACHE:
            self.etat[self.proposition_x2, self.proposition_y2] = MONTRE


    def changer_etat(self):
        if self.contenu[self.proposition_x1, self.proposition_y1] == self.contenu[
            self.proposition_x2, self.proposition_y2]:
            self.etat[self.proposition_x1, self.proposition_y1] = TROUVE
            self.etat[self.proposition_x2, self.proposition_y2] = TROUVE
        else:
            self.etat[self.proposition_x1, self.proposition_y1] = CACHE
            self.etat[self.proposition_x2, self.proposition_y2] = CACHE

        self.proposition_x1 = -1
        self.proposition_y1 = -1
        self.proposition_x2 = -1
        self.proposition_y2 = -1



    def fini(self):
        if all(self.etat) != CACHE:
            return True
        else:
            return False
