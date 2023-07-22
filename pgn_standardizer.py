import sys
from chess.pgn import read_game
from textwrap import wrap

for filename in sys.argv[1:]:
    with open(filename, 'r') as pgn:
        game = read_game(pgn)
        game_str = str(game)

        out = ''
        for s in game_str.split('\n'):
            if s == '':
                out += '\n'

            for w in wrap(s, width=80, break_long_words=False, break_on_hyphens=False):
                out += f'{w}\n'

    print(out, file=open(f'{filename}.tmp', 'w'), end='\n')
