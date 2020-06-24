from gui import Gui
from Simulation import *
from gui import *
from Cell import *


simulation1=Simulation()
interface = Gui()
interface.start()
Test1=Cell()
simulation1.CalculNbrVoisin()
simulation1.CalculRegleVoisin()
interface.updateCell(Test1.x,Test1.y,Test1.vivant)