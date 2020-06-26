from random import randint

from cell import Cell
from gui import Gui
from simulation import Simulation

#On déclare une simulation, une cellule et une interface pour avoir acccès au fonction de la classe.
simulation1=Simulation()
simulation1.SetLongueur()
simulation1.SetLargeur()
t=simulation1.GetLongueur()
p=simulation1.GetLargeur()

simulation1.SetNbGen()
nb=simulation1.GetNbGen()

cellule1=Cell(t,p)
interface = Gui(t,p)
interface.getligne()
interface.getcolone()


interface.start()
for x in range(t):
    for y in range(p):
        interface.updateCell(x,y,randint(0,1)) #Affectue un motif aléatoire

#interface.SaveClick(x,y)
for i in range (nb):
    simulation1.CalculNbrVoisin()
    simulation1.CalculregleVoisin()
    for x in range(t):
        for y in range(p):
            interface.updateCell()

