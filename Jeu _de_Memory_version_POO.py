from Constants_Jeu_de_Memory import *
from random import sample, shuffle
class Grille:

    def __init__(self):
        self.contenu = {(x,y): 0 for x in range(NB_DE_COLONNE) for y in range(NB_DE_LIGNE) }
        
