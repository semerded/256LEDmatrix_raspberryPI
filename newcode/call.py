import subprocess, threading


def main():
    subprocess.call("main.py", shell=True)
    
def knightRider():
    subprocess.call("LED_knightRider.py", shell=True)
    
threading.Thread(target=knightRider).start()
threading.Thread(target=main).start()

while True:
    try:
        pass
    except KeyboardInterrupt:
        subprocess.call("terminate.py", shell=True)