import logging


FORMAT = '%(asctime)s %(levelname)s [%(name)s::%(funcName)s()] %(message)s'
formater = logging.Formatter(FORMAT)

file_handler = logging.FileHandler('ticTacToe.log')
file_handler.setFormatter(formater)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formater)


logger = logging.getLogger('TicTacToe')
logger.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(console_handler)