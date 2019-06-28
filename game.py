import curses
from drawing import draw_background, draw_tracks, draw_time
from config import GAME_SIZE, FPS
from misc import limit_fps


SCENE = [draw_time, draw_tracks, draw_background]
state = {'time': 0}


@limit_fps(fps=FPS)
def draw_scene(screen):
    for draw_element in reversed(SCENE):
        draw_element(screen, state)
    screen.refresh()


def main(screen):
    screen.resize(*GAME_SIZE)
    while True:
        draw_scene(screen)
        state['time'] += 1
    screen.clear()
    screen.getkey()


curses.wrapper(main)
