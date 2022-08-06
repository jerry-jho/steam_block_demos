from arduino import *


class LED7SEG595:

    digital_table = [
        b'\xC0', b'\xF9', b'\xA4', b'\xB0', b'\x99', b'\x92', b'\x82', b'\xF8',
        b'\x80', b'\x90', b'\xFF'
    ]
    digital_select = [b'\xF8', b'\xF4', b'\xF2', b'\xF1']

    def __init__(self, MOSI=D8, MISO=D9, SCK=D7, LT=D4, timer_id=None):
        self.sspi = SoftSPI(MOSI, MISO, SCK)
        self.LT = LT
        self.v = None
        self.delay = 5
        self.timer_id = timer_id

    def begin(self):
        self.sspi.begin()
        self.v = 0
        if self.timer_id is not None:
            from machine import Timer
            self.timer = Timer(self.timer_id)
            self.timer.init(period=20, mode=Timer.PERIODIC, callback=self.loop)

    def setValue(self, v):
        self.v = v

    def loop(self, *a):
        N = 4
        b = [self.digital_table[10] for _ in range(N)]
        if self.v is not None:
            v = int(self.v)
            if v < 0:
                v = 0
            for i in range(N):
                b[i] = self.digital_table[v % 10]
                v //= 10
        for i in range(N):
            digitalWrite(self.LT, LOW)
            self.sspi.transfer(b[i], self.digital_select[i])
            digitalWrite(self.LT, HIGH)
            delay(self.delay)


if __name__ == '__main__':

    led = LED7SEG595(timer_id=0)

    led.begin()
    for n in range(300):
        led.setValue(n)
        delay(1000)
