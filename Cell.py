from random import randint

class Cell:
    #definition du constructeur d'une cellule.
    def __init__(self, x=15, y=15):
        self.x = x
        self.y = y
        self.vivant = randint(0,1)
        self.nbvoisin = 0

#On verifie le nombre de voisin au coordonnées voisines
    def CheckVoisin(self,y,x,grid):
        self.nbvoisin= 0
        if self.grid[x+1][y] == 1:
                    nbvoisin = nbvoisin+1
        if self.grid[x+1][y-1] == 1:
                    nbvoisin = nbvoisin + 1
        if self.grid[x+1][y+1] == 1:
                    nbvoisin = nbvoisin + 1
        if self.grid[x][y] == 1:
                    nbvoisin = nbvoisin+1
        if self.grid[x][y-1] == 1:
                    nbvoisin = nbvoisin + 1
        if self.grid[x][y+1] == 1:
                    nbvoisin = nbvoisin + 1
        if self.grid[x-1][y] == 1:
                    nbvoisin = nbvoisin+1
        if self.grid[x-1][y-1] == 1:
                    nbvoisin = nbvoisin + 1
        if self.grid[x-1][y+1] == 1:
                    nbvoisin = nbvoisin + 1
        print(self.nbvoisin)


#On affecte les regles en fonction du nombre de voisins.
    def EtatVoisin(self):
        if self.vivant == 0:
            if self.nbvoisin == 3:
                self.vivant = 1
                self.grid[row][column] == 2
        print(self.vivant)
        if self.vivant == 1:
            if self.nbvoisin >3:
                self.vivant=0
            if self.nbvoisin <2:
                self.vivant = 0
                self.grid[row][column] == 1
        print(self.vivant)
