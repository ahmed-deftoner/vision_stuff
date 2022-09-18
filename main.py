import PySimpleGUI as sg
import cv2
import numpy as np

def main():
    sg.theme("LightGreen")

    # Define the window layout
    layout = [
        [sg.Text("OpenCV Demo", size=(1, 1), justification="center")],
        [sg.Image(filename="", key="-IMAGE-",size=(4,4))],
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

    cap = cv2.VideoCapture(0)

    while True:
        event, values = window.read(timeout=20)
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        ret, frame = cap.read()

        if values["-ENHANCE-"]:
            enh_val = values["-ENHANCE SLIDER-"] / 40
            clahe = cv2.createCLAHE(clipLimit=enh_val, tileGridSize=(8, 8))
            lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
            lab[:, :, 0] = clahe.apply(lab[:, :, 0])
            frame = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

        imgbytes = cv2.imencode(".png", frame)[1].tobytes()
        window["-IMAGE-"].update(data=imgbytes)

    window.close()

main()