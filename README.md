# Streamer led display
Ce microprogramme a pour but de contrôler les leds du streamer

## Config
L'installation des drivers est expliquée sur [cette page](https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel?tab=readme-ov-file).
Voir notamment la config spécifique pour les raspi [ici](https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel?tab=readme-ov-file).

Les leds doivent être branchées sur les GPIO suivants :

|I/O led|GPIO                 |
|-------|---------------------|
|5v     |pin 4 (5.0 VDC)      |
|DIN    |pin 19 (GPIO 12 MSIO)|
|GND    |pin 20 (Ground)      |