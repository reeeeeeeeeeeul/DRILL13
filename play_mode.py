from pico2d import *
import game_framework
import game_world
from boy import Boy
from grass import Grass
import pause_mode


def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            import title_mode
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_mode(pause_mode)
        else:
            boy.handle_event(event)



def init():
    global boy
    global running

    running = True
    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)


def update():
    game_world.update()


def pause():
    boy.pause()


def resume():
    pass


def render():
    clear_canvas()
    game_world.render()
    update_canvas()

def finish():
    global boy
    game_world.clear()
    boy = None
