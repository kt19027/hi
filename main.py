dc = 0
se = 0

def on_button_pressed_a():
    global dc, se
    dc = randint(0, 10)
    se = randint(0, 10)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_logo_pressed():
    if se == dc:
        basic.show_string("Hello!")
        basic.show_icon(IconNames.YES)
        music.play_melody("C G D A F B C5 E ", 120)
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.giggle),
            SoundExpressionPlayMode.UNTIL_DONE)
    else:
        basic.show_icon(IconNames.NO)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_sound_loud():
    basic.show_leds("""
        . . . . .
                . # # # .
                . # . # .
                . # # # .
                . . . . .
    """)
    basic.show_leds("""
        . # . . #
                . # . # .
                . # # . .
                . # . # .
                . # . . #
    """)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_forever():
    pass
basic.forever(on_forever)
