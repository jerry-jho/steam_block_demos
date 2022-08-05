from arduino import *
from adafruit_ssd1306 import *

SCREEN_WIDTH=const(128)
SCREEN_HEIGHT=const(32)

SCREEN_ADDRESS=const(0x3C)

display = Adafruit_SSD1306(SCREEN_WIDTH, SCREEN_HEIGHT)


if not display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS):
    print("SSD1306 allocation failed")
else:
    display.display()
    delay(2000)
    display.clearDisplay()
    n = 0
    while True:
        display.clearDisplay()
        display.setTextSize(1)
        display.setTextColor(SSD1306_WHITE)
        display.setCursor(0, 0)
        display.println(n)
        n += 1
        delay(100)
        display.display()

