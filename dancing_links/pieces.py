import logging
from links import make_objects, search

PIECES = ('CDDC', 'DHCC', 'DHHD', 'DSDH', 'DSHS', 'HCCD', 'HCHS', 'SHCS', 'SSCH')

BUMP_OUT = {
    'C': (0, 0),
    'D': (0, 1),
    'H': (1, 0),
    'S': (1, 1)
}

BUMP_IN = {
    'C': (1, 1),
    'D': (1, 0),
    'H': (0, 1),
    'S': (0, 0)
}

SIDES = ((12, 0, 1, 12), (12, 2, 3, 0), (12, 12, 4, 2), (1, 5, 6, 12),
         (3, 7, 8, 5), (4, 12, 9, 7), (6, 10, 12, 12), (8, 11, 12, 10),
         (9, 12, 12, 11))


def row(pos, piece):
    result = 44 * [0]
    result[pos] = 1
    result[piece + 9] = 1

    # Populate the piece related info
    for idx in range(2):
        bump = BUMP_OUT[PIECES[piece][idx]]
        result[SIDES[pos][idx] * 2 + 18] = bump[0]
        result[SIDES[pos][idx] * 2 + 19] = bump[1]

    for idx in range(2):
        bump = BUMP_IN[PIECES[piece][idx+2]]
        result[SIDES[pos][idx + 2] * 2 + 18] = bump[0]
        result[SIDES[pos][idx + 2] * 2 + 19] = bump[1]

    return result[:-2]


def rows():
    result = []
    for i in range(9):
        result += [row(i, j) for j in range(9)]
    return result


def position_loc(vector):
    return vector.index(1)


def piece_loc(vector):
    half_vector = vector[9:]
    return half_vector.index(1)


def out_bump_loc(vector):
    bump_vector = vector[18:22]
    return bump_vector


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    board = rows()
    board = [r[:9] for r in board]
    head = make_objects(board, range(81))
    search(head)