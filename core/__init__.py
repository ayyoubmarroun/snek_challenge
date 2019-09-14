

class Board(object):

    def __init__(self, width: int, heigth: int):
        self.width = width
        self.heigth = heigth
        self.board = [[True for column in range(heigth)] for row in range(width)]

    def draw_block(self, x, y):
        if x < 0 or y <0:
            raise IndexError(f"Combination of x,y:{x},{y} out of range.")
        self.board[x][y] = False
    
    def get_cell(self, x, y):
        if x < 0 or y <0:
            raise IndexError(f"Combination of x,y:{x},{y} out of range.")
        return self.board[x][y]

    def is_cell_available(self, x, y):
            return self.get_cell(x, y)
        
    def copy(self):
        return Board(self.width, self.heigth)


class Snek(object):
    movements = {"R": [1, 0], "D": [0, 1], "L": [-1, 0], "U": [0, -1]}

    def __init__(self, snek: list):
        self.snek = snek

    def sonar(self, board: Board):
        new_board = self.available_cells(board)
        movements = self.possible_movements()
        sonar = []
        for m in movements:
            try:
                if new_board.is_cell_available(*movements[m]):
                    sonar.append(m)
            except IndexError:
                pass
        return sonar

    def possible_movements(self):
        head = self.snek[0]
        movements = Snek.movements.copy()
        for m in movements.keys():
            movements[m] = list(map(sum, zip(head,movements[m])))
        return movements


    def available_cells(self, board: Board):
        new_board = board.copy()
        for i in range(len(self.snek)-1):
            body = self.snek[i]
            new_board.draw_block(*body)
        return new_board
    
    def move_snek(self, direction: str, board: Board):
        if direction not in Snek.movements.keys():
            raise Exception(f"Movement \"{direction}\" unknown.")
        if direction not in self.sonar(board):
            raise Exception(f"Can't move \"{direction}\", there is something bloking you!!!")
        head = self.snek[0]
        head = list(map(sum,zip(head, Snek.movements[direction])))
        self.snek = [head] + self.snek[:-1]

    


class Game(object):

    def __init__(self, board: list, snek: list):
        self.board = Board(*board)
        self.snek = Snek(snek)

    def move_snek(self, direction):
        self.snek.move_snek(direction, self.board)

    def movements(self):
        return self.snek.sonar(self.board)

    def copy(self):
        return Game([self.board.width, self.board.heigth], self.snek.snek)
    


def numberOfAvailableDifferentPaths(board, snake, depth):
    game = Game(board, snake)
    return available_paths(game, depth)
    

def available_paths(game: Game, depth):
    total_paths = 0
    if depth == 0:
        return 0
    if depth == 1:
        return len(game.movements())
    
    for move in game.movements():
        game_copy = game.copy()
        game_copy.move_snek(move)
        total_paths += available_paths(game_copy, depth - 1)
    return total_paths