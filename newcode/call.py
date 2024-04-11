import subprocess, threading, json

fp = open("LEDs/led_data.json")
data = json.load(fp)
data["active"] = True
fp.close()
fp = open("LEDs/led_data.json", "w")
json.dump(data, fp, indent = 4, separators=(',',': '))
fp.close()


def main():
    subprocess.call("sudo python3 main.py", shell=True)
    
def knightRider():
    subprocess.call("sudo python3 LED_knightRider.py", shell=True)
    
def frontLight():
    subprocess.call("sudo python3 LED_front.py", shell=True)
    
def rearLight():
    subprocess.call("sudo python3 LED_rear.py", shell=True)
        
threading.Thread(target=main).start()
threading.Thread(target=knightRider).start()
threading.Thread(target=frontLight).start()
threading.Thread(target=rearLight).start()
print("calling done")