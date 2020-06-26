import json


class Simulation:
    #Déclaration du constructeur de la classe simulation
    def __init__(self, NbGeneration = 0, NbCrea = 0, entree1 = 0, entree2= 0 ):
        self.NbGeneration= NbGeneration
        self.NbCrea= NbCrea
        self.grid=[]
        self.entree1 = entree1
        self.entree2 = entree2

    #Fonction permettant de récuperer le nombre de voisin au alentour de toute les cellules.
    def CalculNbrVoisin(self):
        for x in range (len(self.grid)):
            for y in range(len(self.grid[x])):
                self.grid[x][y].CheckVoisin(self.entree1, self.entree2,self.grid)

    #Fonction permettant d'incrémentation le nombre de génération et de définir l'état des cellules/case en fonction de nos regles et de leur voisins.
    def CalculregleVoisin(self):
        self.NbGeneration = self.NbGeneration + 1
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                self.grid[x][y].EtatVoisin()

    #Fonction permettant de fixer la longueur de grille initial pour le lancement du jeu.
    # Une limitation est faite entre 1 et 99 cases. Si l'utilisateur rentre un nombre > ou <
    # Il aura un message et une nouvelle tentative, pareil si l'utilisateur rentre des lettres plutot que des nombres (en temps normal cela aurait planter l'application)
    def SetLongueur(self):
        valid=0
        test=False

        while test == False or valid ==0:
            x = input("Longueur du damier : ")
            test = x.isdigit()
            if test == True:
                x = int(x)
                if x < 100 and  x > 0:
                    valid = 1
                else:
                    print("Erreur de saisie: plage autorisée 1 à 99")
            else:
                print("Erreur de saisie: plage autorisée 1 à 99")


        self.entree1 = x
        print(self.entree1)

    # Fonction permettant de fixer la largeur de grille initial pour le lancement du jeu.
    def SetLargeur(self,y=0):
        valid = 0
        test = False

        while test == False or valid == 0:
            y = input("Largeur du damier : ")
            test = y.isdigit()
            if test == True:
                y = int(y)
                if y < 100 and y > 0:
                    valid = 1
                else:
                    print("Erreur de saisie: plage autorisée 1 à 99")
            else:
                print("Erreur de saisie: plage autorisée 1 à 99")

        self.entree2 = y

        #Fonctions permettant l'affichage des valeurs saisie pour la largeur et la longueur, cette affichage se fait en string

    def GetLargeur(self):
        strentree2=str(self.entree2)
        print("La valeur choisie pour la largeur est : "+ strentree2)
        return self.entree2

    def GetLongueur(self):
        strentree1=str(self.entree1)
        print("La valeur choisie pour la longueur est : " + strentree1)
        return self.entree1


#fonction permettant le choix du nombre de génération a effectuer. (entre 10 et 999)
    def SetNbGen(self):
            valid = 0
            test = False

            while test == False or valid == 0:
                y = input("Nombre de génération souhaitées : ")
                test = y.isdigit()
                if test == True:
                    y = int(y)
                    if y < 1000 and y > 9:
                        valid = 1
                    else:
                        print("Erreur de saisie: plage autorisée 10 à 999")
                else:
                    print("Erreur de saisie: plage autorisée 10 à 999")

            self.NbGeneration = y

    def GetNbGen(self):
        strNb = str(self.NbGeneration)
        print("La valeur choisie pour la génération est : " + strNb)
        return self.NbGeneration

