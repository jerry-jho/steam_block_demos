# STEAM 组件示例集合

本demo集合融合了常用的STEAM电子组件，包括传感器、动作器、显示单元等，同时提供Arduino示例和MicroPython示例

示例所使用的开发板为标准尺寸的Arduino Uno、Arduino Leonard、ESPDuino、WeMos D1 R32（后两者可以用MicroPython）

大部分示例需要配合PH2.0扩展板

# 安装 Arduino 相关库

打开Arduino IDE，安装库，选择libraries/steam_blocks

每个demo所需要安装的库，在.ino文件头部已做说明

# 安装 MicroPython 相关库

首先在开发板上安装好MicroPython，然后使用ampy（安装Python，然后pip install adafruit-ampy）将

libraries/py/arduino.py
libraries/py/<开发板>/espboard.py

复制到开发板上