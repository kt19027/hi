let dc = 0
let se = 0
input.onButtonPressed(Button.A, function () {
    dc = randint(0, 10)
    se = randint(0, 10)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    if (se == dc) {
        basic.showString("Hello!")
        basic.showIcon(IconNames.Yes)
        music.playMelody("C G D A F B C5 E ", 120)
        music.playSoundEffect(music.builtinSoundEffect(soundExpression.giggle), SoundExpressionPlayMode.UntilDone)
    } else {
        basic.showIcon(IconNames.No)
    }
})
input.onSound(DetectedSound.Loud, function () {
    basic.showLeds(`
        . . . . .
        . # # # .
        . # . # .
        . # # # .
        . . # . .
        `)
    basic.showLeds(`
        . # . . #
        . # . # .
        . # # . .
        . # . # .
        . # . . #
        `)
})
basic.forever(function () {
	
})
