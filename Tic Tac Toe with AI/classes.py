from constants import *
import numpy as np
import pygame
import sys
import random
import copy
from constants import *

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

    def final_state(self, show=False):
        """
        returns 0 if no win YET
        returns 1 if player 1 wins
        returns 2 if player 2 wins
        """
        for col in range(COLS):

            # checking for vertical win
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                if show:
                    iPos = (col * SQUARE_SIZE + SQUARE_SIZE // 2, 20)
                    ePos = (col * SQUARE_SIZE + SQUARE_SIZE // 2, HEIGHT - 20)
                    pygame.draw.line(screen, ORANGE, iPos, ePos, CROSS_WIDTH)
                return self.squares[0][col]

        for row in range(ROWS):

            # checking for horizontal win
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                if show:
                    iPos = (20, row * SQUARE_SIZE + SQUARE_SIZE // 2)
                    ePos = (WIDTH - 20, row * SQUARE_SIZE + SQUARE_SIZE // 2)
                    pygame.draw.line(screen, ORANGE, iPos, ePos, CROSS_WIDTH)
                return self.squares[row][0]

        # primary diagonal win
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            if show:
                iPos = (20, 20)
                ePos = (WIDTH - 20, HEIGHT - 20)
                pygame.draw.line(screen, ORANGE, iPos, ePos, 10)

            return self.squares[0][0]

        # secondary diagonal win
        if self.squares[0][ROWS - 0 - 1] == self.squares[1][ROWS - 1 - 1] == self.squares[2][ROWS - 2 - 1] != 0:
            if show:
                iPos = (20, HEIGHT - 20)
                ePos = (WIDTH - 20, 20)
                pygame.draw.line(screen, ORANGE, iPos, ePos, 10)
            return self.squares[0][ROWS - 0 - 1]

        # NO WIN YET
        return 0

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
            (row, col) for row in range(ROWS)
            for col in range(COLS)
            if self.is_empty(row, col)
        ]

        return empty_sqrs


class AI:

    def __init__(self, level=1, player=2):
        self.level = level
        self.player = player

    def rnd(self, board):

        empty_squares = board.get_empty_sqrs()
        idx = random.randrange(0, len(empty_squares))

        return empty_squares[idx]

    def minimax(self, board, maximizing: bool):

        # base case
        case = board.final_state()

        # base case 1 -> player 1 wins
        if case == 1:
            return 1, None  # eval, move

        # base case 2 -> player 2 wins
        if case == 2:
            return -1, None

        # base case 3 -> no more turns
        elif board.is_full():
            return 0, None

        if maximizing:
            max_eval = -100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for row, col in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_position(row, col, 1)
                eval = self.minimax(temp_board, False)[0]

                if eval > max_eval:
                    max_eval = eval
                    best_move = (row, col)

            return max_eval, best_move

        min_eval = 100
        best_move = None
        empty_sqrs = board.get_empty_sqrs()

        for row, col in empty_sqrs:
            temp_board = copy.deepcopy(board)
            temp_board.mark_position(row, col, self.player)
            eval = self.minimax(temp_board, maximizing=True)[0]

            if eval < min_eval:
                min_eval = eval
                best_move = (row, col)

        return min_eval, best_move

    def eval(self, main_field):
        if self.level == 0:
            #  random choice
            eval = 'random'
            move = self.rnd(main_field)
        else:
            # MiniMax algorithm
            eval, move = self.minimax(main_field, False)

        print(f'AI has chosen to mark the square in pos {move} with an eval of {eval}')
        return move

    def change_level(self):
        if self.level == 1:
            print('Level changed to 0')
            self.level = 0
        else:
            print('Level changed to 1')
            self.level = 1


# Class Screen

class GameScreen:
    def __init__(self):
        self.board = Board()
        self.player = 2  # 1 - 0, 2 - X
        self.ai = AI()
        self.game_mode = 'AI'  # 2 modes - pvp or AI
        self.running = True  # set to False if win/Game over/draw
        self.draw_lines()

    def make_move(self, row, col):
        self.board.mark_position(row, col, self.player)
        self.draw_fig(row, col)
        self.next_turn()

    def draw_lines(self):

        screen.fill(PURPLE)
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

    def change_gamemode(self):
        if self.game_mode == 'pvp':
            print(f'Game mode changed to AI')
            self.game_mode = 'AI'
        else:
            print(f'Game mode changed to PVP')
            self.game_mode = 'pvp'

    def reset(self):
        self.__init__()

    def is_over(self):
        return self.board.is_full() != 0 or self.board.final_state(show=True)