def main():
    from LEDs._segment import _Segment
    from time import sleep
    import board
    
    ledCount: int = 16 # 80, 32 rear (112)
    carlight = _Segment(board.D10, ledCount, 0.1)
    
    from LEDs.LEDeffects import LEDeffects
    
    ledEffects = LEDeffects(carlight, ledCount)

    while True:
        data = carlight.loadData("car_light")
        ledEffects.getEffectByName(data["type"], data["color"])
        sleep(0.1)