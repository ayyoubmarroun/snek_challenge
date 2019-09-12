

class Board(object):

    def __init__(self, width: int, heigth: int):
        self.width = width
        self.heigth = heigth
        self.board = [[True for column in heigth] for row in width]

    def draw_block(self, x, y):
        # TODO: Add exception out of  bounds
        self.board[x][y] = False
    
    def get_cell(self, x, y):
        # TODO: Add exception out of  bounds
        return self.board[x][y]

    def is_cell_available(self, x, y):
        try:
            return self.board[x][y]
        except Exception:
            return False
        
    def copy(self):
        return Board(self.width, self.heigth)


class Snek(object):
    movements = {"R": [0, 1], "D": [0, 1], "L": [0, -1], "U": [0, -1]}

    def __init__(self, snek: list):
        self.snek = snek

    def sonar(self, board: Board):
        new_board = self.draw_snek(board)
        head = self.snek[0]
        res = map(sum,[zip(head,m) for m in [[0,1], [0,-1], [1,0], [-1,0]]])
        sonar = map(new_board.is_cell_available, *res)
        return sonar


    def draw_snek(self, board: Board):
        new_board = board.copy()
        for body in self.snek:
            new_board.draw_block(*body)
        return new_board
    
    def move_snek(self, direction: str, board: Board):
        if direction in Snek.movements.keys():
            raise Exception(f"Movement \"{direction}\" unknown.")
        if direction not in self.sonar(board):
            raise Exception(f"Can't move \"{direction}\", going out of bounds!")
        head = self.snek[0]
        head = list(map(sum,zip(head, Snek.movements[direction])))
        self.snek = head + self.snek[:-1]

    


class Game(object):

    def __init__(self, board: list, snek: list):
        self.board = Board(*board)
        self.snek = Snek(snek)
    
    