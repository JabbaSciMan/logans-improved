input.onPinPressed(TouchPin.P1, function () {
    if (strip.length() - 20 >= loco && strip.length() - 37 <= loco) {
        basic.showString("GG")
    }
})
let loco = 0
let strip: neopixel.Strip = null
let bottomPosOfRange = 16
let lengthOfRange = 20
strip = neopixel.create(DigitalPin.P0, 53, NeoPixelMode.RGB)
let range = strip.range(bottomPosOfRange, lengthOfRange)
basic.forever(function () {
    strip.setBrightness(25)
    range.showColor(neopixel.colors(NeoPixelColors.Blue))
    for (let index = 0; index < 1; index++) {
        strip.setPixelColor(36, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(35, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(34, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(33, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(32, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(31, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(30, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(29, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(28, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(27, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(26, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(25, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(24, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(23, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(22, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(21, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(20, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(19, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(18, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(17, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(16, neopixel.colors(NeoPixelColors.Blue))
        strip.show()
        loco += 1
        strip.setPixelColor(loco, neopixel.colors(NeoPixelColors.Red))
        basic.pause(25)
        strip.show()
        strip.clear()
    }
    strip.setBrightness(25)
    for (let index = 0; index < 53; index++) {
        strip.setPixelColor(36, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(35, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(34, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(33, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(32, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(31, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(30, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(29, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(28, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(27, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(26, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(25, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(24, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(23, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(22, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(21, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(20, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(19, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(18, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(17, neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(16, neopixel.colors(NeoPixelColors.Blue))
        strip.show()
        loco += -1
        strip.setPixelColor(loco, neopixel.colors(NeoPixelColors.Red))
        strip.show()
        basic.pause(25)
        strip.clear()
    }
})
