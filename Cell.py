from gui import Gui
from Simulation import *
from gui import *
from Cell import *

class Cell:
    def __init__(self):
        self.x = 2
        self.y = 3
        self.vivant = 1
        self.nbvoisin = 2


    def CheckVoisin(self,y,x,grid):
        nbvoisin = 0
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


    def EtatVoisin(self):
        if self.vivant == 0:
            if self.nbvoisin == 3:
                self.vivant = 1
                self.grid[row][column] == 2
        if self.vivant == 1:
            if self.nbvoisin >3:
                self.vivant=0
            if self.nbvoisin <2:
                self.vivant = 0
                self.grid[row][column] == 1

