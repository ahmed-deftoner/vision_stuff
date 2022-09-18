from asyncio.windows_events import NULL
import io
import os
import PySimpleGUI as sg
import cv2
import numpy as np
from PIL import Image

file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]

def main():
    sg.theme("LightGreen")

    # Define the window layout
    layout = [
        [sg.Image(key="-IMAGE-")],
        [
            sg.Text("Image File"),
            sg.Input(size=(10, 1), key="-FILE-"),
            sg.FileBrowse(file_types=file_types),
            sg.Button("Load Image"),
        ],
        [sg.Radio("None", "Radio", True, size=(5, 1))],
        [
            sg.Radio("Pixelate", "Radio", size=(5, 1), key="-PIXELATE-"),
            sg.Slider(
                (8, 2048),
                1024,
                1,
                orientation="h",
                size=(20, 5),
                key="-PIXELATE SLIDER-",
            ),
        ],
        [sg.Button("Exit", size=(5, 1))],
    ]

    # Create the window and show it without the plot
    window = sg.Window("OpenCV Integration", layout, location=(200, 200),size=(600,600))

    image = NULL
    original = NULL
    while True:
        event, values = window.read(timeout=20)
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if values["-PIXELATE-"]:
            enh_val = values["-PIXELATE SLIDER-"]
            # Get input size
            height, width = image.shape[:2]

            # Desired "pixelated" size
            w, h = (int(enh_val), int(enh_val))

            # Resize input to "pixelated" size
            temp = cv2.resize(original, (w, h), interpolation=cv2.INTER_LINEAR)

            # Initialize output image
            image = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

        if event == "Load Image":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                image = Image.open(values["-FILE-"])
                image.thumbnail((400, 400))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue())
                original = image
                original = np.asarray(original)
        image = np.asarray(image)
        imgbytes = cv2.imencode(".png", image)[1].tobytes()
        window["-IMAGE-"].update(data=imgbytes)
    window.close()

main()
