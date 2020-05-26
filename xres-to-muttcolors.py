#!/usr/bin/env python3


import sys


color_map = {
    'background':   'BACKGROUND',
    'color0':       'BLACK',
    'color8':       'BRBLACK',
    'color1':       'RED',
    'color9':       'BRRED',
    'color2':       'GREEN',
    'color10':      'BRGREEN',
    'color3':       'YELLOW',
    'color11':      'BRYELLOW',
    'color4':       'BLUE',
    'color12':      'BRBLUE',
    'color5':       'MAGENTA',
    'color13':      'BRMAGENTA',
    'color6':       'CYAN',
    'color14':      'BRCYAN',
    'color7':       'WHITE',
    'color15':      'BRWHITE'
}


def v2ci(v):
    if v < 48:
        return 0
    elif v < 115:
        return 1
    else:
        return (v - 35) // 40


def dist_square(a1, b1, c1, a2, b2, c2):
    return (a1 - a2) ** 2 + (b1 - b2) ** 2 + (c1 - c2) ** 2


# For more information on this algorithm, see
# https://stackoverflow.com/a/41978310
def c24to8(color):
    r, g, b = (color & 0xff0000) >> 16, (color & 0xff00) >> 8, color & 0xff

    ir = v2ci(r)
    ig = v2ci(g)
    ib = v2ci(b)
    color_index = 36 * ir + 6 * ig + ib

    avg = (r + g + b) // 3
    grey_index = 23 if avg > 238 else (avg - 3) // 10

    i2cv = [0, 0x5f, 0x87, 0xaf, 0xd7, 0xff]
    cr = i2cv[ir]
    cg = i2cv[ig]
    cb = i2cv[ib]
    gv = 8 + 10 * grey_index

    color_err = dist_square(cr, cg, cb, r, g, b)
    grey_err = dist_square(gv, gv, gv, r, g, b)

    return 16 + color_index if color_err <= grey_err else 232 + grey_index


def main():
    if len(sys.argv) > 1:
        f = open(sys.argv[1])
    else:
        f = sys.stdin

    for line in f:
        if line.startswith('!'):
            continue
        elem = [e.strip(' *.#\t\n') for e in line.split(':')]
        if len(elem) != 2:
            continue

        if elem[0] in color_map:
            color8 = c24to8(int(elem[1], base=16))
            print('{} = color{}'.format(color_map[elem[0]], color8))

    f.close()


if __name__ == '__main__':
    main()
