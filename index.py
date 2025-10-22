import dxcam
import numpy as np
import win32api, win32con
import keyboard
import time

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# Iniciar DXCam
camera = dxcam.create()  # captura monitor principal
camera.start(region=(0, 0, 1920, 1080), target_fps=60)  # captura apenas a região

print("Aperte 'Q' para iniciar, 'C' para parar.")

while True:
    if keyboard.is_pressed('c'):
        camera.stop()
        break

    if keyboard.is_pressed('q'):
        frame = camera.get_latest_frame()  # numpy array (H, W, 3) → BGR

        if frame is None:
            continue

        # Find all white pixels at once (BGR = 255,255,255)
        white_pixels = np.where(np.all(frame == (255,  87,  34), axis=2))

        if len(white_pixels[0]) > 0:
            # Get first white pixel (or last, up to you)
            y = white_pixels[0][-1]
            x = white_pixels[1][-1]
            click(x, y)
            time.sleep(0.05)
    time.sleep(0.001)  # evita uso de CPU a 100%