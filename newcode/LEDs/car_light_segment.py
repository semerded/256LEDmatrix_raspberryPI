def main():
    from LEDs._segment import _Segment
    from time import sleep
    import board
    from LEDs.LEDeffects import ledEffectsProperties
    
    ledCount: int = 136 # 80, 56 rear (112)
    carlight = _Segment(board.D10, ledCount, 0.1)
    
    from LEDs.LEDeffects import LEDeffects
    
    ledEffects = LEDeffects(carlight, ledCount)

    while True:
        data = carlight.loadData("car_light")
        ledEffects.getEffectByName(data["type"], data["color"])
        if ledEffectsProperties[data["type"]]["speed"]:
            sleep(data["speed"])