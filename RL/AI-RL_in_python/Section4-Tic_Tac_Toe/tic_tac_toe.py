# https://deeplearningcourses.com/c/artificial-intelligence-reinforcement-learning-in-python
# https://www.udemy.com/artificial-intelligence-reinforcement-learning-in-python
# Simple reinforcement learning algorithm for learning tic-tac-toe
# Use the update rule: V(s) = V(s) + alpha*(V(s') - V(s))
# Use the epsilon-greedy policy:
#   action|s = argmax[over all actions possible from state s]{ V(s) }  if rand > epsilon
#   action|s = select random action from possible actions from state s if rand < epsilon
#
#
# INTERESTING THINGS TO TRY:
#
# Currently, both agents use the same learning strategy while they play against each other.
# What if they have different learning rates?
# What if they have different epsilons? (probability of exploring)
#   Who will converge faster?
# What if one agent doesn't learn at all?
#   Poses an interesting philosophical question: If there's no one around to challenge you,
#   can you reach your maximum potential?
from __future__ import print_function, division
from builtins import range, input
# Note: you may need to update your version of future
# sudo pip install -U future


import numpy as np
import matplotlib.pyplot as plt

LENGTH = 3


class Environment:
    def __init__(self, LENGTH, player_one, player_two, verbose=True):
        self.size = LENGTH
        self.board = build_board(self.size)
        self.player_one = player_one
        self.player_two = player_two
        self.verbose = verbose

    def check_legality(self, r, c):
        if 0 <= r < LENGTH and 0 <= c < LENGTH and self.board[r, c] == 0:
            return True
        else:
            return False

    def update_board(self, player, r, c):
        self.board[r, c] = player.player_num

    def switch_players(self, player):
        if player == self.player_one:
            return self.player_two
        else:
            return self.player_one

    def game_over(self):
        #check for winner
        rows = [np.sum(self.board[x,:]) for x in range(LENGTH)]
        columns = [np.sum(self.board[:,x]) for x in range(LENGTH)]
        diagonals = [self.board.trace(), np.fliplr(self.board).trace()]

        if any(LENGTH in sublist for sublist in [rows or columns or diagonals]):
            return (self.player_one.name, True)
        elif any(-LENGTH in sublist for sublist in [rows or columns or diagonals]):
            return (self.player_two.name, True)
        elif not 0 in self.board:
            return("draw", True)
        else:
            return("game is on", False)

    def play_game(self):
        if self.verbose:
            print_board(self.board)

        while True:
            for p in [self.player_one, self.player_two]:
                print("player {}, where do you want to place your symbol?".format(p.player_num))
                r,c = list(map(int, input().strip().split()))
                while not self.check_legality(r,c):
                    print("illigeal move!")
                    print("player {}, where do you want to place your symbol?".format(p.player_num))
                    r, c = list(map(int, input().strip().split()))
                self.update_board(p,r,c)
                print_board(self.board)
                GO = self.game_over()
                if GO[1]:
                    print(GO[0])
                    return None
                else:
                    self.switch_players(p)


class Human:
    def __init__(self, player_num, name="Human"):
        self.player_num = player_num
        self.symbol = set_symbol(player_num)
        self.name = name

class Agent:
    def __init__(self, player_num, name="Agent"+str(np.random.randint(100))):
        self.player_num = player_num
        self.symbol = set_symbol(player_num)
        self.name = name

def build_board(size):
    # r -> Row, c -> Column
    r = c = size
    board_state = np.zeros((r,c))
    return board_state


def print_board(board_state):
    print_mapping = {-1:"O", 0:" ", 1:"X"}
    for r in range(LENGTH):
        row = ""
        for c in range(LENGTH):
            row+=print_mapping[board_state[r, c]] + "|"
        print(row)
        print("-" * LENGTH * 2)

def set_symbol(player_number):
    if player_number == 1:
        return "X"
    elif player_number == -1:
        return "O"
    else:
        raise Exception("player number is out of scope")





if __name__ == "__main__":

    human1 = Human(1)
    human2 = Human(-1)
    env= Environment(LENGTH,human1, human2)

    env.play_game()
    # print(env.board)
    #
    # env.update_board(agent,0,1)
    # print(env.board)
    #
    # env.update_board(human, 0, 2)
    # print(env.board)