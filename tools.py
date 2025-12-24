# -*- coding: utf-8 -*-
#Action
import subprocess

#This function handles the physical interaction with the android phone
def get_screenshot():
    #Takes a screenshot of the phone
    subprocess.run(["adb", "shell", "screencap", "-p", "/sdcard/screen.png"])
    subprocess.run(["adb", "pull", "/sdcard/screen.png", "current_state.png"])
    print("Screenshot captured as current_state.png")

def execute_tap(x, y):
    """Taps the screen at specific coordinates."""
    subprocess.run(["adb", "shell", "input", "tap", str(x), str(y)])
    print("Tapped at: " + str(x) + ", " + str(y))

def input_text(text):
    """Types text into the phone."""
    # Replace spaces with %s for ADB compatibility
    formatted_text = text.replace(" ", "%s")
    subprocess.run(["adb", "shell", "input", "text", formatted_text])
    print("Typed text: " + text)