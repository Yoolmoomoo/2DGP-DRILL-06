from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1000, 800
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False;
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                running = False
    pass

def place_hand_randomly():
    global hand, hand_x ,hand_y
    hand.draw(hand_x, hand_y)
    if x == hand_x and y == hand_y:
        hand_x = random.randint(100, 900)
        hand_y = random.randint(100, 700)
    pass

def find_hand():
    global frame, x, y, hand_x, hand_y, t,i
    i += 4
    t = i / 100
    x = (1-t)*x + t*hand_x
    y = (1-t)*y + t*hand_y
    if hand_x <= x:
        character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', x, y, 100, 100)
    elif hand_x > x:
        character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, ' ', x, y, 100, 100)
    if i == 100:
        i = 0
    pass

i = 0
t = 0
running = True
hand_x, hand_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    place_hand_randomly()
    find_hand()
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.07)

    handle_events()

close_canvas()




