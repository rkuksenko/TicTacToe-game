import logger.logger
import logging

logger = logging.getLogger('TicTacToe')


class Player:
    def __init__(self):
        logger.debug(f'Created player instance')

    def init(self):
        self.name = input('Input your name: ')
        self.character = input('Input character: ')
        logger.debug(f'Created player {self.name} with character {self.character}')

    def input_index(self):
        try:
            is_valid = False
            index = ''

            while not is_valid:
                index = str(input(f"{self.name}, it's your turn, choose index (1-9): "))
                logger.debug(f'Received {index} index')

                if len(index) == 1 and index.isdigit():
                    is_valid = True
                else:
                    print('Wrong index, try again')

        except Exception as e:
            logger.error(e)
        finally:
            return int(index)

    def get_character(self):
        return self.character

    def get_name(self):
        return self.name
