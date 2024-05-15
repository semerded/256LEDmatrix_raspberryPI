def main():
    from LEDs._segment import _Segment
    from time import sleep
    import board, json
    from LEDs.LEDeffects import ledEffectsProperties
    
    ledCount: int = 136 # 80, 56 rear (112)
    carlight = _Segment(board.D10, ledCount, 0.1)
    
    from LEDs.LEDeffects import LEDeffects
    
    ledEffects = LEDeffects(carlight, ledCount)

    while True:
        data = carlight.loadData("car_light")
        
        if data["reset"]:
            ledEffects.reset()
            with open("LEDs/led_data.json") as fp:
                ledData = json.load(fp)
            ledData["car_light"]["reset"] = False
            with open("LEDs/led_data.json", "w") as fp:
                json.dump(ledData, fp, indent = 4, separators=(',',': '))
                
        ledEffects.getEffectByName(data["type"], data["color"])
        if ledEffectsProperties[data["type"]]["speed"]:
            sleep(data["speed"])