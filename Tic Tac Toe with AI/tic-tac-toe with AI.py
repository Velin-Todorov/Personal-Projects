import numpy as np
import pygame
import sys

# ROWS, COLS for the console board class
ROWS = 3
COLS = 3

# size of the screen
WIDTH = 650
HEIGHT = 650

# Size of a single Square
SQUARE = WIDTH // COLS

# Size of a circle
CIRC_WIDTH = 15
RADIUS = SQUARE // 4

# colors for lines and background using rgb
PURPLE = (93, 63, 211)
BLACK = (0, 0, 0)

# colors for circle and cross
GREEN = (124, 252, 0)
CROSS = (0, 0, 0)

# Setting up pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("V3l's Tic-Tac-Toe")
screen.fill(PURPLE)


# Class for a Console Board

class Board:

    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))
        self.mark_position(1, 1, player=0)
        print(self.squares)

    def mark_position(self, row, col, player):
        self.squares[row][col] = player

    def is_empty(self, row, col):
        return self.squares[row][col] == 0


# Class Screen

class GameScreen:
    def __init__(self):
        self.board = Board()
        self.player = 1 # 1 - X, 2 - O
        self.draw_lines()

    def draw_lines(self):
        # vertical
        pygame.draw.line(screen, BLACK, (210, 0), (210, 650), 10)
        pygame.draw.line(screen, BLACK, (450, 0), (450, 650), 10)

        # horizontal
        pygame.draw.line(screen, BLACK, (0, 220), (650, 220), 10)
        pygame.draw.line(screen, BLACK, (0, 450), (650, 450), 10)

    def next_turn(self):
        self.player = self.player % 2 + 1

    def draw_fig(self, row, col):

        if self.player == 1:
            pass

        elif self.player == 2:
            center = (col * SQUARE + SQUARE // 2, row * SQUARE + SQUARE // 2)
            pygame.draw.circle(screen, GREEN, center, RADIUS)



def main_loop():
    game = GameScreen()
    board = game.board

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # this here converts the pixels to rows and cols for coordinates
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQUARE
                col = pos[0] // SQUARE

                if board.is_empty(row, col):
                    board.mark_position(row, col, game.player)
                    game.next_turn()
                    game.draw_fig(row, col)
                    print(board.squares)
                else:
                    print('ERROR')

        pygame.display.update()


main_loop()
