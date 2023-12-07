import logging
import numpy as np
from dataclasses import dataclass

# Configure logging
logging.basicConfig(level=logging.WARNING, format=' %(asctime)s -  %(levelname)s -  %(message)s')

# Define a dataclass for representing 3D points
@dataclass
class Point:
    x: float
    y: float
    z: float
    visibility: float

def find_distance(point1: Point, point2: Point) -> float:
    # Calculate Euclidean distance between two 3D points
    coordinates1 = np.array([point1.x, point1.y, point1.z])
    coordinates2 = np.array([point2.x, point2.y, point2.z])
    dist = np.linalg.norm(coordinates2 - coordinates1)
    return dist

def calculate_angle(point1: Point, point2: Point, point3: Point) -> float:
    # Calculate vectors
    vec1 = np.array([point1.x, point1.y, point1.z]) - np.array([point2.x, point2.y, point2.z])
    vec2 = np.array([point3.x, point3.y, point3.z]) - np.array([point2.x, point2.y, point2.z])
    logging.debug(f"vec1, vec2: {vec1, vec2}")
    # Calculate magnitudes
    mag_vec1 = np.linalg.norm(vec1)
    mag_vec2 = np.linalg.norm(vec2)
    assert mag_vec1 != 0 and mag_vec2 != 0
    logging.debug(f"mag_vec1, mag_vec2: {mag_vec1, mag_vec2}")
    # Calculate dot product
    dot_product = np.dot(vec1, vec2)
    logging.debug(f"dot_product: {dot_product}")
    

    scaled_dot =  dot_product / (mag_vec1 * mag_vec2)
    scaled_dot  = np.around(scaled_dot, 3) #because float point arithmetic error can cause scaled_dot to be slightly greater than 1 or less than -1

    assert -1 <= scaled_dot <= 1

    logging.debug(f"scaled_dot: {scaled_dot}")

    # Calculate the angle in radians
    angle_radians = np.arccos(scaled_dot)

    # Convert angle to degrees
    angle_degrees = np.degrees(angle_radians)

    return angle_degrees


def get_interest_landmarks(person_landmark: list[Point]) -> dict[str, Point]:
    # Extract specific landmarks of interest from a list of landmarks
    assert len(person_landmark) == 33
    return {
        'left_shoulder': person_landmark[11],
        'right_shoulder': person_landmark[12],
        'left_hip': person_landmark[23],
        'right_hip': person_landmark[24],
        'left_knee': person_landmark[25],
        'right_knee': person_landmark[26],
        'left_ankle': person_landmark[27],
        'right_ankle': person_landmark[28]
    }

def check_visibility(landmark_dict: dict[str, Point]) -> bool:
    # Check if all landmark points have sufficient visibility
    return all(landmark.visibility >= 0.5 for landmark in landmark_dict.values())

def find_angles(landmark_dict: dict[str, Point]) -> tuple[float, float, float, float]:
    # Calculate angles for various body parts using landmark points
    left_shoulder, right_shoulder, left_hip, right_hip, left_knee, right_knee, left_ankle, right_ankle = (
        landmark_dict[key] for key in [
            'left_shoulder', 'right_shoulder', 'left_hip', 'right_hip', 'left_knee', 'right_knee', 'left_ankle', 'right_ankle'
        ]
    )
    l_hip_angle = calculate_angle(left_shoulder, left_hip, left_knee)
    l_knee_angle = calculate_angle(left_hip, left_knee, left_ankle)
    r_hip_angle = calculate_angle(right_shoulder, right_hip, right_knee)
    r_knee_angle = calculate_angle(right_hip, right_knee, right_ankle)
    return l_hip_angle, l_knee_angle, r_hip_angle, r_knee_angle

def find_class(l_hip_angle: float, l_knee_angle: float, r_hip_angle: float, r_knee_angle: float, landmark_dict: dict[str, Point]) -> str:
    # Determine the person's class based on angles and visibility
    visible = check_visibility(landmark_dict)
    logging.debug(f"l_hip_angle, l_knee_angle, r_hip_angle, r_knee_angle: {l_hip_angle, l_knee_angle, r_hip_angle, r_knee_angle}")
    if visible:
        if all(angle < 120 for angle in [l_hip_angle, l_knee_angle, r_hip_angle, r_knee_angle]):
            return "sitting"
        else:
            return "standing"
    else:
        return "Unknown"
