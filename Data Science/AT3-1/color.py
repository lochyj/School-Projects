import curses

color_theme = {
    "463f3a", # Background colour
    "ffffff"  # Foreground colour
}

# TODO: FIX THE COLOURS!!!
def convert_hex_to_curses_color(hex):
    out = list(int(hex[i : i + 2], 16) for i in [0, 2, 4])

    for count, i in enumerate(out):
        out[count] = int(i)

    return out

def init_colors(screen):
    colors = list(map(convert_hex_to_curses_color, color_theme))

    for count, i in enumerate(colors):
        curses.init_color(count, i[0], i[1], curses.COLOR_BLACK)
