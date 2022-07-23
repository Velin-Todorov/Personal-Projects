# ROWS, COLS for the console board class
ROWS = 3
COLS = 3
SIZE_FIELD = ROWS * COLS

# size of the screen
WIDTH = 650
HEIGHT = 650

# Size of a single Square
SQUARE_SIZE = WIDTH // COLS

# Size of a circle
CIRC_WIDTH = 15
RADIUS = SQUARE_SIZE // 4

# Size of a cross
CROSS_WIDTH = 15
OFFSET = 50  # a value used to create distance from (0,0) and (600, 600) so that the cross the does not touch the origin

# colors for lines and background using rgb
PURPLE = (93, 63, 211)
BLACK = (0, 0, 0)
ORANGE = (255, 140, 0)

# colors for circle and cross
GREEN = (124, 252, 0)
CROSS = BLACK