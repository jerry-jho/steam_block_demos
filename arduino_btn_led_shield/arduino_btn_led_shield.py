from arduino import *
from led7seg import LED7SEG595
from machine import Timer

class shield:
    __LEDPIN__ = [D13, D12, D11, D10]
    __KEYPIN__ = [A1, A2, A3]
    def __init__(self, timer_id=0):
        self.__led7seg = LED7SEG595()
        self.__led7seg.begin()            
        self.__timer = Timer(timer_id)
        self.__timer.init(period=20, mode=Timer.PERIODIC, callback=self.__loop__)
        self.__last_key = [1, 1, 1]
        self.begin()

    def begin(self):
        pass

    def __loop__(self, *s):
        for i, k in enumerate(self.__KEYPIN__):
            kv = digitalRead(k)
            if kv != self.__last_key[i]:
                self.onKeyInput(i, kv)
                self.__last_key[i] = kv
        self.__led7seg.loop()

    def onKeyInput(self, keyId, keyValue):
        pass

    def onAnalogInput(self, value):
        pass

    def set7SegValue(self, v):
        self.__led7seg.setValue(v)

    def setLEDValue(self, ledId, value):
        if ledId >= 0 and ledId < 4:
            digitalWrite(self.__LEDPIN__[ledId], value)


class MyApp(shield):
    def begin(self):
        self.v = 0
        self.led_id = 0

    def onKeyInput(self, keyId, keyValue):
        if keyValue == 0:
            if keyId == 0:
                self.v += 1
            elif keyId == 1:
                self.v -= 1
            else:
                for i in range(4):
                    self.setLEDValue(i, LOW)
                self.setLEDValue(self.led_id, HIGH)
                self.led_id += 1
                if self.led_id == 4:
                    self.led_id = 0
            if self.v < 0:
                self.v = 0
            self.set7SegValue(self.v)

digitalWrite(D13, LOW)
digitalWrite(D12, LOW)
digitalWrite(D11, LOW)
digitalWrite(D10, LOW)

app = MyApp()

while True:
    delay(1000)