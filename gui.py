import json
import threading
from simulation import Simulation
import pygame

# Define some colors
from simulation import Simulation

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Gui(threading.Thread):
    def __init__(self,ligne,colone):
        threading.Thread.__init__(self)
        self.width = 20
        self.height = 20
        self.margin = 5
        self.grid = []
        self.ligne = ligne
        self.colone= colone

        for row in range(self.ligne):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(self.colone):
                self.grid[row].append(0)  # Append a cell

    def getcolone(self):
        print(self.colone)
        return self.colone

    def getligne(self):
        print(self.ligne)
        return self.ligne

    def setcolone(self, x):
        self.colone = x

    def setligne(self, y):
        self.ligne = y

    def updateCell(self,x=0,y=0,valeur=0):
        self.grid[x][y]=valeur

    def run(self):

        # Initialize pygame
        pygame.init()

        # Set the HEIGHT and WIDTH of the screen
        WINDOW_SIZE = [1920, 1080]
        screen = pygame.display.set_mode(WINDOW_SIZE)

        # Set title of screen
        pygame.display.set_caption("Le jeu de la vie-Rémi-Gaetan")

        # Loop until the user clicks the close button.
        done = False

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        # -------- Main Program Loop -----------
        while not done:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (self.width + self.margin)
                    row = pos[1] // (self.height + self.margin)
                    # Set that location to one
                    self.grid[row][column] = 1
                    print("Click ", pos, "Grid coordinates: ", row, column)

            # Set the screen background
            screen.fill(BLACK)

            # Draw the grid
            for row in range(self.ligne):
                for column in range(self.colone):
                    color = WHITE
                    if self.grid[row][column] == 1:
                        color = GREEN
                    if self.grid[row][column] == 2:
                        color = RED
                    if self.grid[row][column] == 3:
                        color = BLACK
                    pygame.draw.rect(screen,
                                     color,
                                     [(self.margin + self.width) * column + self.margin,
                                      (self.margin + self.height) * row + self.margin,
                                      self.width,
                                      self.height])
            # Limit to 60 frames per second
            clock.tick(60)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

        # Be IDLE friendly. If you forget this line, the program will 'hang'
        # on exit.
        pygame.quit()

    def SaveClick(self,ligne,colone):
        print("Save")
        dictionnaire = {}
        for x in range(ligne): # Tentatif de sauvegarde
            for y in range(colone):
                dictionnaire['xy']=self.grid[ligne][colone].text()
        print (dictionnaire)
        with open('data.json', 'w') as file:
            json.dump(dictionnaire, file)
