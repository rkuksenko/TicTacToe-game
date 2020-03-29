import logging
import logger
from game.player import Player
from game.ticTacToe import TicTacToe

print ('Welcome to the Tic Tac Toe game!!')

print ('Player 1')
player1 = Player()
player1.init()

print ('Player 2')
player2 = Player()
player2.init()

instance = TicTacToe(player1, player2)

print ("Let's go!")

finish_game = False
while not finish_game:
    instance.start()

    choice = ''
    while choice != 'y' and choice != 'n':
        choice = str(input ('Play again? (y/n): '))

    if choice == 'n':
        break

print ('Good Luck:)')