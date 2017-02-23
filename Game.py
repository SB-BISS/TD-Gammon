import numpy as np
import random
import

class Game:

    def __init__(self):
        self.numPoints = 24
        self.players = ['white', 'black']
        self.board = [[] for _ in range(numPoints)]
        self.on_bar = {}
        self.off_board = {}
        self.pieces_left = {}
        for p in self.players:
            self.on_bar[p] = []
            self.off_board[p] = []
            self.pieces_left[p] = 0

    def roll_dice(self):
        return (random.randint(1,6), random.randint(1,6))


    def find_moves(self, roll, player):
        r1, r2 = roll[0], roll[1]
        moves = []

        # Determine how many rolls
        # Did we roll doubles?
        if r1 = r2:
            j = 4
        else
            j = 2

        # Are there pieces on the bar for the given player?
        if len(self.on_bar[player]) >= 1:
            # Does the point where we would put the piece have no pieces or is it controlled by the player?
            if self.board[r1-1] <=1 or self.board[len(self.board[r1-1] - 1 ] == player:
                # TO FINISH:
                # Does the point where we would put the piece have 1 stone that is the opposite player's color?
                If self.board[r1-1] = 1 and self.board[len(self.board[r1-1] - 1 ] != player:
                    piece = self.on_bar[p].pop()

            piece = self.on_bar[p].pop()
            self.board[r1-1].append(piece)

        


    def is_valid_move(self, start, end, piece_color):
        if len(self.board[start]) > 0 and self.board[start][0] == piece_color:
            if end < 0 or end >= len(self.board):
                return False
            if len(self.board[end]) <= 1:
                return True
            if len(self.board[end]) > 1 and self.board[end][-1] == piece_color:
                return True
        return False

    # Check to see if the game is over
    def game_over(self):
        for p in self.players:
            if (self.off_board[p] = 15 and self.pieces_left[p] = 0):
                True
            else
                return False

    # Determine which player has won
    def find_winner(self):
        if (self.off_board[0] = 15 and self.pieces_left[0] = 0):
            self.players[0]

        return self.players[1]
