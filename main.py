import board
import neopixel

pixels = neopixel.NeoPixel(board.D10, 1) # Raspberry Pi wiring!
 
increment = True
value = 0
while True:    
    value = value+1 if increment else value-1    
    if value == 0:
        increment = True
    elif value == 255:
        increment = False
    pixels.fill((value, value, value))
