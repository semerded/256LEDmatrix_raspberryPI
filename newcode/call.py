import subprocess, threading


def main():
    subprocess.call("main.py", shell=True)
    
threading.Thread(target=main).start()