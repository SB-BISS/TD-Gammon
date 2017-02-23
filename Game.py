import numpy as np
import random

class Game:

    def __init__(self):
        self.players = ['white', 'black']
        self.board = [[] for _ in range(24)]
        self.on_bar = {}
        self.off_board = {}
        self.pieces_left = {}
        for p in self.players:
            self.on_bar[p] = []
            self.off_board[p] = []
            self.pieces_left[p] = 15

        # Initialize the board with a hard coded set-up for each point (0 indexed!)
        for i in range(2):
            self.board[0].append('white')
        for i in range(5):
            self.board[5].append('black')
        for i in range(3):
            self.board[7].append('black')
        for i in range(5):
            self.board[11].append('white')
        for i in range(5):
            self.board[12].append('black')
        for i in range(3):
            self.board[16].append('white')
        for i in range(5):
            self.board[18].append('white')
        for i in range(2):
            self.board[23].append('black')

    def roll_dice(self):
        return (random.randint(1,6), random.randint(1,6))


    def find_moves(self, roll, player):
        r1, r2 = roll[0], roll[1]

        # Determine how many rolls
        # Did we roll doubles?
        if r1 == r2:
            print("Player {} rolled double {}'s!".format(player, r1))
            j = 2
        else:
            j = 2

        # Are there pieces on the bar for the given player?
        if len(self.on_bar[player]) >= 1:
            # Does the point where we would put the piece have no pieces or is it controlled by the player?
            if self.board[r1-1] <=1 or self.board[len(self.board[r1-1])- 1 ] == player:
                # Does the point where we would put the piece have 1 stone that is the opposite player's color?
                if self.board[r1-1] == 1 and self.board[len(self.board[r1-1])- 1] != player:
                    piece = self.on_bar[player].pop()
                    if self.board[r1-1] == get_opponent(player):
                        hit = self.board[r1-1].pop()
                        self.on_bar[get_opponent(player)].append(hit)
                        self.board[r1-1].append(piece);

            piece = self.on_bar[p].pop()
            self.board[r1-1].append(piece)

        print("Player {} has no pieces on the bar".format(player))
        # Can the player hit the other player?
        for i in range(len(self.board)):
            # print(self.board[i][len(self.board[i])])
            if self.board[i] == player:
                print('yup')
                # Check to see if the point a roll away has 1 opponent piece
                if len(self.board[i + r1]) == 1 and self.board[i + r1] == get_opponent(player):
                    print("Player {} can hit! point {}".format(player, self.board[i + r1]))




    def is_valid_move(self, start, end, piece_color):
        if len(self.board[start]) > 0 and self.board[start] == piece_color:
            if end < 0 or end >= len(self.board):
                return False
            if len(self.board[end]) <= 1:
                return True
            if len(self.board[end]) > 1 and self.board[end] == piece_color:
                return True
        return False

    # Check to see if the game is over
    def game_over(self):
        for p in self.players:
            if (self.off_board[p] == 15 and self.pieces_left[p] == 0):
                True
            else:
                return False

    # Get the opposite color of the given player (useful for hitting)
    def get_opponent(self, player):
        for p in self.players:
            if p != self.players[p]:
                return self.players[p]

    # Determine which player has won
    def find_winner(self):
        if (self.off_board[0] == 15 and self.pieces_left[0] == 0):
            self.players[0]

        return self.players[1]

    # Print the contents of a desired point on the board
    def print_point(self, point):
        print("Point #{} has {} pieces: {}".format(point, len(self.board[point]), self.board[point]))
