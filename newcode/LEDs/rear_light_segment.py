def main():
    from LEDs._segment import _Segment
    from time import sleep
    import board

    ledCount: int = 32
    frontLight = _Segment(board.D12, ledCount, 0.4)

    while True:
        data = frontLight.loadData("front_light")
        frontLight.pixels.fill(data["color"])
        
        sleep(0.1)
        