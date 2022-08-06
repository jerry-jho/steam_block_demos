from espboard import *
from machine import Pin,SoftI2C
import machine
import time


OUTPUT = Pin.OUT
INPUT = Pin.IN
HIGH = 1
LOW = 0

def pinMode(pin, mode):
    pass
    
def digitalWrite(pin, val):
    p = Pin(pin, Pin.OUT)
    p.value(val)

def digitalRead(pin):
    p = Pin(pin, Pin.IN)
    return p.value()

def delay(ms):
    time.sleep_ms(ms)

class SoftSPI:
    def __init__(self, MOSI, MISO, SCK):
        self.MOSI = MOSI
        self.MISO = MISO
        self.SCK = SCK

    def begin(self):
        self.spi = machine.SoftSPI(
            sck=Pin(self.SCK, mode=Pin.OUT),
            mosi=Pin(self.MOSI, mode=Pin.OUT),
            miso=Pin(self.MISO, mode=Pin.IN))
    
    def transfer(self, *bs):
        for b in bs:
            self.spi.write(b)     






