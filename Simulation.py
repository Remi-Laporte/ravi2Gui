from gui import Gui
from Simulation import *
from gui import *
from Cell import *

class Simulation:
    def __init__(self):
        self.MaxX = 20
        self.MaxY = 40
        self.NbGeneration= 0
        self.NbCrea= 0
        self.grid=[]

    def CalculRegleVoisin(self):
        self.NbGeneration= self.NbGeneration + 1
        for x in range(self.MaxX):
            for y in range(self.MaxY):
                self.grid[x][y].EtatVoisin()


    def CalculNbrVoisin(self):
        for x in range(self.MaxX):
            for y in range(self.MaxY):
                self.grid[x][y].CheckVoisin()

