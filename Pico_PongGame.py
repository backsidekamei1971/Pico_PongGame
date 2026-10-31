import machine
import ssd1306
import time
i2c = machine.I2C(0, scl=machine.Pin(9), sda=machine.Pin(8))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
x = 10
y = 10
width = 8
height = 8
dx = 2
dy = 2
while True:
    oled.fill(0)
    x += dx
    y += dy  
    if x <= 0 or x + width >= 128:
        dx = -dx
    if y <= 0 or y+ height >= 64:
        dy = -dy
        
    oled.fill_rect(x, y, width, height, 1)   
    oled.show()   
    time.sleep_ms(16)
