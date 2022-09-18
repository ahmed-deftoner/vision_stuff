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
        [sg.Text("OpenCV Demo", size=(1, 1), justification="center")],
        [sg.Image(key="-IMAGE-")],
        [
            sg.Text("Image File"),
            sg.Input(size=(10, 1), key="-FILE-"),
            sg.FileBrowse(file_types=file_types),
            sg.Button("Load Image"),
        ],
        [sg.Radio("None", "Radio", True, size=(5, 1))],
        [
            sg.Radio("enhance", "Radio", size=(5, 1), key="-ENHANCE-"),
            sg.Slider(
                (1, 255),
                128,
                1,
                orientation="h",
                size=(20, 5),
                key="-ENHANCE SLIDER-",
            ),
        ],
        [sg.Button("Exit", size=(5, 1))],
    ]

    # Create the window and show it without the plot
    window = sg.Window("OpenCV Integration", layout, location=(200, 200),size=(600,600))

    #cap = cv2.VideoCapture(0)
    image = NULL
    while True:
        event, values = window.read(timeout=20)
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        #ret, frame = cap.read()
        loaded = 0
        if values["-ENHANCE-"]:
            enh_val = values["-ENHANCE SLIDER-"] / 40
            clahe = cv2.createCLAHE(clipLimit=enh_val, tileGridSize=(8, 8))
            lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
            lab[:, :, 0] = clahe.apply(lab[:, :, 0])
            image = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
            #input = cv2.imread('cloud.png')

            # Get input size
            height, width = image.shape[:2]

            # Desired "pixelated" size
            w, h = (32, 32)

            # Resize input to "pixelated" size
            temp = cv2.resize(image, (w, h), interpolation=cv2.INTER_LINEAR)

            # Initialize output image
            image = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
            #bio = io.BytesIO()
            #image.save(bio, format="PNG")
            #window["-IMAGE-"].update(data=bio.getvalue())
            #cv2.imshow('Input', input)
            #cv2.imshow('Output', output)
            #print("in")
            #cv2.waitKey(0)

        if event == "Load Image":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                image = Image.open(values["-FILE-"])
                image.thumbnail((400, 400))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue())
                loaded = 1
        if loaded == 1:
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            window["-IMAGE-"].update(data=bio.getvalue())
        image = np.asarray(image)
        imgbytes = cv2.imencode(".png", image)[1].tobytes()
        window["-IMAGE-"].update(data=imgbytes)
    window.close()

main()
