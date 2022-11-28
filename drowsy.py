
import cv2
import time
import numpy as np
import mediapipe as mp
from mediapipe.python.solutions.drawing_utils import _normalized_to_pixel_coordinates as denormalize_coordinates

def distance(point_1, point_2):
    dist = sum([(i - j) ** 2 for i, j in zip(point_1, point_2)]) ** 0.5
    return dist
 
def get_ear(landmarks, refer_idxs, frame_width, frame_height):
    ...
    ...
    return ear, coords_points
 
def calculate_avg_ear(landmarks, left_eye_idxs, right_eye_idxs, image_w, image_h):
    ...
    ...
    return Avg_EAR, (left_lm_coordinates, right_lm_coordinates)
 
def get_mediapipe_app(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
):
    """Initialize and return Mediapipe FaceMesh Solution Graph object"""
    face_mesh = mp.solutions.face_mesh.FaceMesh(
        max_num_faces=max_num_faces,
        refine_landmarks=refine_landmarks,
        min_detection_confidence=min_detection_confidence,
        min_tracking_confidence=min_tracking_confidence,
    )
 
    return face_mesh
 
def plot_eye_landmarks(frame, left_lm_coordinates, 
                       right_lm_coordinates, color
                       ):
    for lm_coordinates in [left_lm_coordinates, right_lm_coordinates]:
        if lm_coordinates:
            for coord in lm_coordinates:
                cv2.circle(frame, coord, 2, color, -1)
 
    frame = cv2.flip(frame, 1)
    return frame
 
 
def plot_text(image, text, origin, 
              color, font=cv2.FONT_HERSHEY_SIMPLEX, 
              fntScale=0.8, thickness=2
              ):
    image = cv2.putText(image, text, origin, font, fntScale, color, thickness)
    return image