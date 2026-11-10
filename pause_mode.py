import game_framework
import game_world
from pico2d import *


def init():
    pass


def finish():
    pass


def update():
    pass


def render():
    clear_canvas()
    game_world.render()
    draw_rectangle(350, 250, 375, 350)
    draw_rectangle(425, 250, 450, 350)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_mode()
            import title_mode
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()
