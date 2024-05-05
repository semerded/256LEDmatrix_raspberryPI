import json

defaultLedData = {
    "active": False,
    "car_light": {
        "type": "car",
        "color": [
            255, 255, 255
        ],
        "speed": 50
    },
    "knightrider": {
        "type": None,
        "color": [
            255, 0, 0
        ],
        "speed": 50
    }
}

def resetLedData():
    with open("LEDs\led_data.json", "w") as fp:
        json.dump(defaultLedData, fp, indent = 4, separators=(',',': '))