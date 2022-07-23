from classes import *

# Setting up pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("V3l's Tic-Tac-Toe")
screen.fill(PURPLE)


def main_loop():
    game = GameScreen()
    board = game.board
    ai = game.ai

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

                if board.is_empty(row, col) and game.running:
                    game.make_move(row, col)

                    if game.is_over():
                        game.running = False
                else:
                    print('ERROR')

            if event.type == pygame.KEYDOWN:

                # g - press this on your keyboard to change the game mode
                if event.key == pygame.K_g:
                    game.change_gamemode()

                # 0 - when you press this on your keyboard it changes to a random AI or MiniMax AI
                if event.key == pygame.K_0:
                    ai.change_level()

                # r - press this on your keyboard to reset the board
                if event.key == pygame.K_r:
                    game.reset()
                    board = game.board
                    ai = game.ai

        if game.game_mode == 'AI' and game.player == ai.player and game.running:
            pygame.display.update()

            # AI methods
            row, col = ai.eval(board)
            game.make_move(row, col)

            if game.is_over():
                game.running = False

        pygame.display.update()


main_loop()
