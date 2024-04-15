def main():
    from LEDs._segment import _Segment
    from time import sleep
    import board
    
    from LEDs.LEDeffects import rider, static, rainbowfull, rainbowRider

    ledCount: int = 112 # 80, 32 rear
    carlight = _Segment(board.D10, ledCount, 0.1)

    while True:
        data = carlight.loadData("car_light")
        rider(carlight, data["color"], ledCount)
        
        sleep(0.1)