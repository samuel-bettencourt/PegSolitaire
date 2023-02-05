import random
import sys


class BoardHole:
    def __init__(self, i_d):
        self.id = i_d
        self.status = 'X'
        self.ur = None
        self.ul = None
        self.left = None
        self.dl = None
        self.dr = None
        self.right = None


class Solutions:
    def __init__(self):
        self.sols = 0
        self.tots = 0
        self.winning_games = []

class Board:
    def __init__(self, moves, previous_moves, starting_pos):
        self.positions = []
        self.moves = moves
        self.previous_moves = previous_moves
        self.starting_pos = starting_pos
        for i in range(0, 15):
            self.positions.append(BoardHole(i))
        self.connect_holes()
        self.positions[starting_pos].status = 'O'

    def connect_holes(self):
        self.positions[0].dr = self.positions[2]
        self.positions[0].dl = self.positions[1]

        self.positions[1].dr = self.positions[4]
        self.positions[1].right = self.positions[2]
        self.positions[1].ur = self.positions[0]
        self.positions[1].dl = self.positions[3]

        self.positions[2].dr = self.positions[5]
        self.positions[2].ul = self.positions[0]
        self.positions[2].left = self.positions[1]
        self.positions[2].dl = self.positions[4]

        self.positions[3].dr = self.positions[7]
        self.positions[3].right = self.positions[4]
        self.positions[3].ur = self.positions[1]
        self.positions[3].dl = self.positions[6]

        self.positions[4].dr = self.positions[8]
        self.positions[4].right = self.positions[5]
        self.positions[4].ur = self.positions[2]
        self.positions[4].ul = self.positions[1]
        self.positions[4].left = self.positions[3]
        self.positions[4].dl = self.positions[7]

        self.positions[5].dr = self.positions[9]
        self.positions[5].ul = self.positions[2]
        self.positions[5].left = self.positions[4]
        self.positions[5].dl = self.positions[8]

        self.positions[6].dr = self.positions[11]
        self.positions[6].right = self.positions[7]
        self.positions[6].ur = self.positions[3]
        self.positions[6].dl = self.positions[10]

        self.positions[7].dr = self.positions[12]
        self.positions[7].right = self.positions[8]
        self.positions[7].ur = self.positions[4]
        self.positions[7].ul = self.positions[3]
        self.positions[7].left = self.positions[6]
        self.positions[7].dl = self.positions[11]

        self.positions[8].dr = self.positions[13]
        self.positions[8].right = self.positions[9]
        self.positions[8].ur = self.positions[5]
        self.positions[8].ul = self.positions[4]
        self.positions[8].left = self.positions[7]
        self.positions[8].dl = self.positions[11]

        self.positions[9].dr = self.positions[14]
        self.positions[9].ul = self.positions[5]
        self.positions[9].left = self.positions[8]
        self.positions[9].dl = self.positions[13]

        self.positions[10].right = self.positions[11]
        self.positions[10].ur = self.positions[6]

        self.positions[11].right = self.positions[12]
        self.positions[11].ur = self.positions[7]
        self.positions[11].ul = self.positions[6]
        self.positions[11].left = self.positions[10]

        self.positions[12].right = self.positions[13]
        self.positions[12].ur = self.positions[8]
        self.positions[12].ul = self.positions[7]
        self.positions[12].left = self.positions[11]

        self.positions[13].right = self.positions[14]
        self.positions[13].ur = self.positions[9]
        self.positions[13].ul = self.positions[8]
        self.positions[13].left = self.positions[12]

        self.positions[14].ul = self.positions[9]
        self.positions[14].left = self.positions[13]

    def display_board(self):
        print("     ", self.positions[0].status)
        print("    ", self.positions[1].status, self.positions[2].status)
        print("   ", self.positions[3].status, self.positions[4].status, self.positions[5].status)
        print("  ", self.positions[6].status, self.positions[7].status, self.positions[8].status, self.positions[9].status)
        print(" ", self.positions[10].status, self.positions[11].status, self.positions[12].status, self.positions[13].status, self.positions[14].status)

    def number_of_pins(self):
        pins = 0
        for i in range(0, len(self.positions)):
            if self.positions[i].status == 'X':
                pins += 1
        return pins

    def execute_move(self, move_index):
        starting_hole = self.moves[move_index][0]
        jumped_hole = self.moves[move_index][1]
        end_hole = self.moves[move_index][2]
        # print(starting_hole, "->", jumped_hole, "->", end_hole)
        self.positions[starting_hole].status = 'O'
        self.positions[jumped_hole].status = 'O'
        self.positions[end_hole].status = 'X'

    def options(self):
        self.moves.clear()
        for i in range(0, 15):
            if self.positions[i].status == 'O':
                if self.positions[i].dr != None and self.positions[i].dr.dr != None:
                    if self.positions[i].dr.status == 'X' and self.positions[i].dr.dr.status == 'X':
                        current_move = [self.positions[i].dr.dr.id, self.positions[i].dr.id, self.positions[i].id]
                        self.moves.append(current_move)
                if self.positions[i].right != None and self.positions[i].right.right != None:
                    if self.positions[i].right.status == 'X' and self.positions[i].right.right.status == 'X':
                        current_move = [self.positions[i].right.right.id, self.positions[i].right.id, self.positions[i].id]
                        self.moves.append(current_move)
                if self.positions[i].ur != None and self.positions[i].ur.ur != None:
                    if self.positions[i].ur.status == 'X' and self.positions[i].ur.ur.status == 'X':
                        current_move = [self.positions[i].ur.ur.id, self.positions[i].ur.id, self.positions[i].id]
                        self.moves.append(current_move)
                if self.positions[i].ul != None and self.positions[i].ul.ul != None:
                    if self.positions[i].ul.status == 'X' and self.positions[i].ul.ul.status == 'X':
                        current_move = [self.positions[i].ul.ul.id, self.positions[i].ul.id, self.positions[i].id]
                        self.moves.append(current_move)
                if self.positions[i].left != None and self.positions[i].left.left != None:
                    if self.positions[i].left.status == 'X' and self.positions[i].left.left.status == 'X':
                        current_move = [self.positions[i].left.left.id, self.positions[i].left.id, self.positions[i].id]
                        self.moves.append(current_move)
                if self.positions[i].dl != None and self.positions[i].dl.dl != None:
                    if self.positions[i].dl.status == 'X' and self.positions[i].dl.dl.status == 'X':
                        current_move = [self.positions[i].dl.dl.id, self.positions[i].dl.id, self.positions[i].id]
                        self.moves.append(current_move)

    def display_options(self):
        print(self.moves)

    def choose_option(self, choice_index):
        self.execute_move(choice_index)
        self.previous_moves.append(self.moves[choice_index])

    def copy_board(self):
        moves = self.moves.copy()
        previous_moves = self.previous_moves.copy()
        board_copy = Board(moves, previous_moves, self.starting_pos)
        for i in range(0, 15):
            board_copy.positions[i].status = self.positions[i].status
        return board_copy

    def take_turn(self):
        self.options()
        if self.number_of_pins() == 1:
            # print("SOLUTION FOUND")
            number_of_solutions.sols += 1
            number_of_solutions.tots += 1
            number_of_solutions.winning_games.append(self.previous_moves)
        elif len(self.moves) == 0:
            # print("GAME OVER")
            number_of_solutions.tots += 1
        else:
            for i in range(0, len(self.moves)):
                next_board = self.copy_board()
                next_board.choose_option(i)
                next_board.take_turn()

    def reset_game(self):
        for i in range(0, 15):
            self.positions[i].status = 'X'

    def get_hint(self):
        pass

    def game_play(self):
        while True:
            self.display_board()
            self.options()
            if self.number_of_pins() == 1:
                print("Congrats you solved the puzzle")
                input("Enter any Key to Exit: ")
                break
            elif len(self.moves) == 0:
                print("Game Over: You are out of moves")
                input("Enter any Key to Exit: ")
                break
            else:
                self.display_options()
                actual_ind = int(input("Enter choice index: "))
                self.choose_option(actual_ind-1)


random.seed(None)
number_of_solutions = Solutions()
game1 = Board([], [], 0)
game1.take_turn()
print("Number of Solutions\t", number_of_solutions.sols)
print("Total Number of Games:\t", number_of_solutions.tots)
print(sys.getsizeof(number_of_solutions.sols))
for i in range(0, 15):
    print(number_of_solutions.winning_games[i])
game1.game_play()
