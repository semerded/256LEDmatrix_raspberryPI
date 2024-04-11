import subprocess, threading, json

def main():
    subprocess.call("sudo python3 main.py", shell=True)
    
def knightRider():
    subprocess.call("sudo python3 LED_knightRider.py", shell=True)
    
def frontLight():
    subprocess.call("sudo python3 LED_front.py", shell=True)
    
def rearLight():
    subprocess.call("sudo python3 LED_rear.py", shell=True)
        
threading.Thread(target=knightRider).start()
threading.Thread(target=frontLight).start()
threading.Thread(target=rearLight).start()
import time
# time.sleep(3)
threading.Thread(target=main).start()
print("calling done")