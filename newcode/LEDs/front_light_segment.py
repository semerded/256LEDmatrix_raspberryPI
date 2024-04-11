def main():
    from LEDs._segment import _Segment
    from time import sleep
    import board

    ledCount: int = 80 # 80
    frontLight = _Segment(board.D10, ledCount, 0.1)

    while True:
        data = frontLight.loadData("front_light")
        frontLight.pixels.fill(data["color"])
        
        sleep(0.1)