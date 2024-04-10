import json

with open("LEDs/led_data.json", "r+") as fp:
    data = json.load(fp)
    data["active"] = False
    fp.seek(0)
    json.dump(data, fp, indent = 4, separators=(',',': '))