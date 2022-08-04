from espboard import *
from machine import Pin,SoftI2C
import time
import framebuf


OUTPUT = Pin.OUT
INPUT = Pin.IN
HIGH = 1
LOW = 0

def pinMode(pin, mode):
    pass
    
def digitalWrite(pin, val):
    p = Pin(pin, Pin.OUT)
    p.value(val)

def delay(ms):
    time.sleep_ms(ms)
    

SSD1306_SWITCHCAPVCC = False
SSD1306_WHITE = 1

class Adafruit_SSD1306:
    # register definitions
    SET_CONTRAST        = const(0x81)
    SET_ENTIRE_ON       = const(0xa4)
    SET_NORM_INV        = const(0xa6)
    SET_DISP            = const(0xae)
    SET_MEM_ADDR        = const(0x20)
    SET_COL_ADDR        = const(0x21)
    SET_PAGE_ADDR       = const(0x22)
    SET_DISP_START_LINE = const(0x40)
    SET_SEG_REMAP       = const(0xa0)
    SET_MUX_RATIO       = const(0xa8)
    SET_COM_OUT_DIR     = const(0xc0)
    SET_DISP_OFFSET     = const(0xd3)
    SET_COM_PIN_CFG     = const(0xda)
    SET_DISP_CLK_DIV    = const(0xd5)
    SET_PRECHARGE       = const(0xd9)
    SET_VCOM_DESEL      = const(0xdb)
    SET_CHARGE_PUMP     = const(0x8d)
    
    def __init__(self, width, height, i2c=None):
        if i2c is None:
            i2c = SoftI2C(scl = Pin(SCL),sda = Pin(SDA),freq = 10000)
        self.i2c = i2c
        self.temp = bytearray(2)
        self.buffer = bytearray(((height // 8) * width) + 1)
        self.buffer[0] = 0x40  # Set first byte of data buffer to Co=0, D/C=1
        self.framebuf = framebuf.FrameBuffer1(memoryview(self.buffer)[1:], width, height)
        self.width = width
        self.height = height       
        self.pages = self.height // 8
        self.x = 0
        self.y = 0
        self.color = 1

    def begin(self, external_vcc=False, addr=0x3c):
        self.addr = addr
        self.external_vcc = external_vcc
        self.poweron()
        self.init_display()
        return True

    def init_display(self):
        for cmd in (
            self.SET_DISP | 0x00, # off
            # address setting
            self.SET_MEM_ADDR, 0x00, # horizontal
            # resolution and layout
            self.SET_DISP_START_LINE | 0x00,
            self.SET_SEG_REMAP | 0x01, # column addr 127 mapped to SEG0
            self.SET_MUX_RATIO, self.height - 1,
            self.SET_COM_OUT_DIR | 0x08, # scan from COM[N] to COM0
            self.SET_DISP_OFFSET, 0x00,
            self.SET_COM_PIN_CFG, 0x02 if self.height == 32 else 0x12,
            # timing and driving scheme
            self.SET_DISP_CLK_DIV, 0x80,
            self.SET_PRECHARGE, 0x22 if self.external_vcc else 0xf1,
            self.SET_VCOM_DESEL, 0x30, # 0.83*Vcc
            # display
            self.SET_CONTRAST, 0xff, # maximum
            self.SET_ENTIRE_ON, # output follows RAM contents
            self.SET_NORM_INV, # not inverted
            # charge pump
            self.SET_CHARGE_PUMP, 0x10 if self.external_vcc else 0x14,
            self.SET_DISP | 0x01): # on
            self.write_cmd(cmd)
        self.fill(0)
        self.display()

    def poweroff(self):
        self.write_cmd(self.SET_DISP | 0x00)

    def contrast(self, contrast):
        self.write_cmd(self.SET_CONTRAST)
        self.write_cmd(contrast)

    def invert(self, invert):
        self.write_cmd(self.SET_NORM_INV | (invert & 1))

    def display(self):
        x0 = 0
        x1 = self.width - 1
        if self.width == 64:
            # displays with width of 64 pixels are shifted by 32
            x0 += 32
            x1 += 32
        self.write_cmd(self.SET_COL_ADDR)
        self.write_cmd(x0)
        self.write_cmd(x1)
        self.write_cmd(self.SET_PAGE_ADDR)
        self.write_cmd(0)
        self.write_cmd(self.pages - 1)
        self.write_framebuf()
        
    def clearDisplay(self):
        self.fill(0)
        
    def setTextSize(self, s):
        pass
        
    def setTextColor(self, c):
        self.color = c
    
    def setCursor(self, x, y):
        self.x = x
        self.y = y
    
    def println(self, val):
        self.framebuf.text(str(val), self.x, self.y, self.color)
        
        
    def fill(self, col):
        self.framebuf.fill(col)

    def pixel(self, x, y, col):
        self.framebuf.pixel(x, y, col)

    def scroll(self, dx, dy):
        self.framebuf.scroll(dx, dy)

    def text(self, string, x, y, col=1):
        self.framebuf.text(string, x, y, col)

    def write_cmd(self, cmd):
        self.temp[0] = 0x80 # Co=1, D/C#=0
        self.temp[1] = cmd
        self.i2c.writeto(self.addr, self.temp)

    def write_framebuf(self):
        # Blast out the frame buffer using a single I2C transaction to support
        # hardware I2C interfaces.
        self.i2c.writeto(self.addr, self.buffer)

    def poweron(self):
        pass



