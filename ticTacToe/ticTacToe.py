import logging
import logger.logger
import random
from itertools import cycle
from game.player import Player


logger = logging.getLogger('TicTacToe')

class TicTacToe():
    def __init__(self, player1, player2):
        logger.debug('Created TicTacToe instance')
        self.players = [player1, player2]
        self.moves = []

    def fill_board(self):
        self.moves.append('')
        for i in range(1, 10):
            self.moves.append(i)

    def reset_board(self):
        self.moves.clear()

    def is_board_full(self):
        moves_left = len([i for i in self.moves if str(i).isnumeric()])
        logger.debug(f'{moves_left} moves left')
        return moves_left == 0

    def have_winner(self):
        if self.moves[1] == self.moves[2] == self.moves[3] or\
           self.moves[4] == self.moves[5] == self.moves[6] or\
           self.moves[7] == self.moves[8] == self.moves[9] or\
           self.moves[1] == self.moves[4] == self.moves[7] or\
           self.moves[2] == self.moves[5] == self.moves[8] or\
           self.moves[3] == self.moves[6] == self.moves[9] or\
           self.moves[1] == self.moves[5] == self.moves[9] or\
           self.moves[3] == self.moves[5] == self.moves[7]:
            return True
        return False

    def draw_board(self):
        logger.debug('Drawig the board')
        for i in range(1, len(self.moves), 3):
            print('-------------')
            print(f'| {self.moves[i]} | {self.moves[i + 1]} | {self.moves[i + 2]} |')

        print('-------------')


    def is_valid_index(self, index):
        try:
            isValid = True

            if not 0 < index < 10:
                print('Wrong index!')
                isValid = False
            else:
                if not str(self.moves[index]).isnumeric():
                    logger.error('Already set')
                    print('Already set!')
                    isValid = False

            return isValid
        except Exception as e:
            logger.error(e)

    def set_move(self, index, character):
        try:
            self.moves[index] = character
            logger.debug(f'Successfuly moved to {index} with character {character}')

        except Exception as e:
            logger.exception(e)

    def produce_move(self, player_id):
        player = self.players[player_id]
        index = player.input_index()

        while not self.is_valid_index(index):
            self.draw_board()
            index = player.input_index()

        char = player.get_character()
        self.set_move(index, char)

    def start(self):
        logger.debug('Game started!')
        self.reset_board()
        self.fill_board()
        player_ids = cycle([0, 1])

        for _ in range(random.randint(0,1)):
            next(player_ids)

        while not self.is_board_full() and not self.have_winner():
            self.draw_board()
            player_id = next(player_ids)
            self.produce_move(player_id)

        self.draw_board()

        if self.have_winner():
            winner = self.players[player_id]
            loser = self.players[next(player_ids)]
            print (f"Player {winner.get_name()} win! {loser.get_name()} don't worry, lucky next time:)")
        else:
            print(f'Draw, lucky next time!')
