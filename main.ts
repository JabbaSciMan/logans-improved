/**
 * A made a comment so  I could make a committ
 */
function plotScore () {
    scoreMod25 = score % 25
    if (scoreMod25 <= 5) {
        led.toggle((scoreMod25 - 1) % 5, 0)
    } else if (scoreMod25 <= 10) {
        led.toggle((scoreMod25 - 1) % 5, 1)
    } else if (scoreMod25 <= 25) {
        led.toggle((scoreMod25 - 1) % 5, 2)
    } else if (scoreMod25 <= 30) {
        led.toggle((scoreMod25 - 1) % 5, 3)
    } else {
        led.toggle((scoreMod25 - 1) % 5, 4)
    }
}
input.onPinPressed(TouchPin.P2, function () {
    timePaused += -1
})
input.onButtonPressed(Button.B, function () {
    timePaused += -1
})
input.onPinPressed(TouchPin.P1, function () {
    if (loco >= bottomPosOfRange && loco <= bottomPosOfRange + lengthOfRange) {
        score += 1
        lengthOfRange += -1
        timePaused += -1
        music.playTone(988, music.beat(BeatFraction.Sixteenth))
    } else {
        score += -1
        music.playTone(220, music.beat(BeatFraction.Sixteenth))
    }
    plotScore()
})
let range: neopixel.Strip = null
let loco = 0
let scoreMod25 = 0
let lengthOfRange = 0
let bottomPosOfRange = 0
let score = 0
score = 0
let timePaused = 25
let LengthOfStrip = 53
let direction = 1
bottomPosOfRange = 16
lengthOfRange = 20
let strip = neopixel.create(DigitalPin.P0, LengthOfStrip, NeoPixelMode.RGB)
basic.forever(function () {
    // When the length of the blue range is shrunk to zero then you win and flash rainbow 10 times.
    // 
    if (lengthOfRange <= 0) {
        music.startMelody(music.builtInMelody(Melodies.Entertainer), MelodyOptions.Once)
        for (let index = 0; index < 10; index++) {
            strip.showRainbow(1, 360)
            basic.pause(500)
            strip.clear()
            strip.show()
            basic.pause(500)
        }
        lengthOfRange = 20
    } else {
        range = strip.range(bottomPosOfRange, lengthOfRange)
        range.showColor(neopixel.colors(NeoPixelColors.Blue))
        loco += direction
        if (loco > 52) {
            loco = 51
            direction = -1
        }
        if (loco < 0) {
            loco = 1
            direction = 1
        }
        strip.setPixelColor(loco, neopixel.colors(NeoPixelColors.Red))
        strip.show()
        basic.pause(timePaused)
        strip.clear()
    }
})
