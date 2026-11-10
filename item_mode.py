from pico2d import *

import game_framework
import game_world


selected_ball_size = 21
item_select_image = None


def init():
    global item_select_image

    if item_select_image is None:
        item_select_image = load_image('item_select.png')


def finish():
    pass


def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    item_select_image.draw(get_canvas_width() // 2, get_canvas_height() // 2)
    update_canvas()


def handle_events():
    global selected_ball_size

    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key in (SDLK_ESCAPE, SDLK_i):
            game_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
            selected_ball_size = 21
            game_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            selected_ball_size = 41
            game_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_0:
            selected_ball_size = None
            game_framework.pop_mode()


def pause():
    pass


def resume():
    pass
