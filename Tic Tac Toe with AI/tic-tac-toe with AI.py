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
SQUARE_SIZE = WIDTH // COLS

# Size of a circle
CIRC_WIDTH = 15
RADIUS = SQUARE_SIZE // 4

#Size of a cross
CROSS_WIDTH = 15
OFFSET = 50  # a value used to create distance from (0,0) and (600, 600) so that the cross the does not touch the origin

# colors for lines and background using rgb
PURPLE = (93, 63, 211)
BLACK = (0, 0, 0)

# colors for circle and cross
GREEN = (124, 252, 0)
CROSS = BLACK

# Setting up pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("V3l's Tic-Tac-Toe")
screen.fill(PURPLE)


# Class for a Console Board

class Board:

    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))
        self.empty_squares = self.squares  # a list of empty squares in the beginning
        self.marked_squares = 0
        print(self.squares)

    def mark_position(self, row, col, player):
        self.squares[row][col] = player
        self.marked_squares += 1  # this attribute is to see when the board is full

    def is_empty(self, row, col):
        """The purpose of this function is to check if a position on the board is empty"""
        return self.squares[row][col] == 0

    def is_full(self):
        return self.marked_squares == 9

    def empty(self):
        """The purpose of this function is to check if there are any empty squares left on the field"""
        return self.marked_squares == 0

    def get_empty_sqrs(self):
        empty_sqrs = [
                      row for row in range(ROWS)
                      for col in range(COLS)
                      if self.is_empty(row, col)

                      ]
        return empty_sqrs


# Class Screen

class GameScreen:
    def __init__(self):
        self.board = Board()
        self.player = 1  # 1 - X, 2 - O
        self.draw_lines()

    def draw_lines(self):
        # vertical
        pygame.draw.line(screen, BLACK, (210, 0), (210, 650), 10)
        pygame.draw.line(screen, BLACK, (450, 0), (450, 650), 10)

        # horizontal
        pygame.draw.line(screen, BLACK, (0, 220), (650, 220), 10)
        pygame.draw.line(screen, BLACK, (0, 450), (650, 450), 10)

    def draw_fig(self, row, col):

        if self.player == 1:
            # desc line
            START_DESC = (col * SQUARE_SIZE + OFFSET, row * SQUARE_SIZE + OFFSET)
            END_DESC = (col * SQUARE_SIZE + SQUARE_SIZE - OFFSET, row * SQUARE_SIZE + SQUARE_SIZE - OFFSET)
            pygame.draw.line(screen, CROSS, START_DESC, END_DESC, CROSS_WIDTH)

            # asc line
            START_ASC = (col * SQUARE_SIZE + OFFSET, row * SQUARE_SIZE + SQUARE_SIZE - OFFSET)
            END_ASC = (col * SQUARE_SIZE + SQUARE_SIZE - OFFSET, row * SQUARE_SIZE + OFFSET)
            pygame.draw.line(screen, CROSS, START_ASC, END_ASC, CROSS_WIDTH)

        elif self.player == 2:
            center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
            pygame.draw.circle(screen, GREEN, center, RADIUS, CIRC_WIDTH)

    def next_turn(self):
        self.player = self.player % 2 + 1


def main_loop():
    game = GameScreen()
    board = game.board

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # this here converts the pixels to rows and cols for coordinates
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQUARE_SIZE
                col = pos[0] // SQUARE_SIZE

                if board.is_empty(row, col):
                    board.mark_position(row, col, game.player)
                    game.next_turn()
                    game.draw_fig(row, col)
                    print(board.squares)
                else:
                    print('ERROR')

        pygame.display.update()


main_loop()
