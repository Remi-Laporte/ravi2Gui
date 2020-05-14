import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class Gui(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        self.setGeometry(1000, 1000, 600, 600) #MODIFICATION TAILLE FENETRE
        self.setWindowTitle('Titre de folie') #MODIFICATION DU TITRE
        self.show()


