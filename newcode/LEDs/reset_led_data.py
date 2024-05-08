import json

defaultLedData = {
    "active": False,
    "car_light": {
        "type": "auto lichten",
        "color": [
            255, 255, 255
        ],
        "speed": 0.1
    },
    "knightrider": {
        "type": None,
        "color": [
            255, 0, 0
        ],
        "speed": 0.1
    }
}

def resetLedData():
    with open("LEDs/led_data.json", "w") as fp:
        json.dump(defaultLedData, fp, indent = 4, separators=(',',': '))