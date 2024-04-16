import subprocess, threading, json

def main():
    subprocess.call("sudo python3 main.py", shell=True)
    
def knightRider():
    subprocess.call("sudo python3 LED_knightRider.py", shell=True)
    
def carLight():
    subprocess.call("sudo python3 LED_car.py", shell=True)
        
threading.Thread(target=main).start()

from time import sleep
while True:
    with open("LEDs/led_data.json") as fp:
        if json.load(fp)["active"]:
            break
    sleep(0.1)
    
threading.Thread(target=knightRider).start()
threading.Thread(target=carLight).start()

print("calling done")