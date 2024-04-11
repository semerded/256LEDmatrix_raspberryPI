import json

def LEDswitch(state: bool):
    fp = open("LEDs/led_data.json")
    data = json.load(fp)
    data["active"] = state
    fp.close()
    fp = open("LEDs/led_data.json", "w")
    json.dump(data, fp, indent = 4, separators=(',',': '))
    fp.close()