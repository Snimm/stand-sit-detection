import math
import pprint
import logging
import numpy as np
pp = pprint.PrettyPrinter(indent=4)

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
import logging.config
#For some reason, improting logging is not enough to import logging.config, it needs to be imported explicitly
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})

def findDistance(point1, point2):
    x1 = point1.x
    y1 = point1.y
    z1 = point1.z  
    x2 = point2.x
    y2 = point2.y
    z2 = point2.z
    dist = math.sqrt((x2-x1)**2+(y2-y1)**2 + (z2-z1)**2)
    return dist


def calculate_angle(point1, point2, point3):
    # Calculate vectors
    vec1 = [point1.x - point2.x, point1.y - point2.y, point1.z - point2.z]
    vec2 = [point3.x - point2.x, point3.y - point2.y, point3.z - point2.z]

    # Calculate magnitudes
    mag_vec1 = math.sqrt(vec1[0]**2 + vec1[1]**2 + vec1[2]**2)
    mag_vec2 = math.sqrt(vec2[0]**2 + vec2[1]**2 + vec2[2]**2)

    # Calculate dot product
    dot_product = vec1[0] * vec2[0] + vec1[1] * vec2[1] + vec1[2] * vec2[2]

    # Calculate the angle in radians
    angle_radians = math.acos(dot_product / (mag_vec1 * mag_vec2))

    # Convert angle to degrees
    angle_degrees = math.degrees(angle_radians)

    return angle_degrees







def get_interst_landmards(person_landmark):
  # pp.pprint(person_landmark)
  assert len(person_landmark) == 33
  dict_landmark = {}
  dict_landmark['left_shoulder'] = person_landmark[11]
  dict_landmark['right_shoulder'] = person_landmark[12]
  dict_landmark['left_hip'] = person_landmark[23]
  dict_landmark['right_hip'] = person_landmark[24]
  dict_landmark['left_knee'] = person_landmark[25]
  dict_landmark['right_knee'] = person_landmark[26]
  dict_landmark['left_ankle'] = person_landmark[27]
  dict_landmark['right_ankle'] = person_landmark[28]
  # logging.debug(pprint.pformat(dict_landmark))
  return dict_landmark


def check_visibility(landmark_dict):
    for key in landmark_dict:
        if landmark_dict[key].visibility < 0.5:
            return False
    return True


def find_angles(landmark_dict):
    left_shoulder = landmark_dict['left_shoulder']
    right_shoulder = landmark_dict['right_shoulder']
    left_hip = landmark_dict['left_hip']
    right_hip = landmark_dict['right_hip']
    left_knee = landmark_dict['left_knee']
    right_knee = landmark_dict['right_knee']
    left_ankle = landmark_dict['left_ankle']
    right_ankle = landmark_dict['right_ankle']
    l_hip_angle = calculate_angle(left_shoulder, left_hip, left_knee)
    l_knee_angle = calculate_angle(left_hip, left_knee, left_ankle)
    r_hip_angle = calculate_angle(right_shoulder, right_hip, right_knee)
    r_knee_angle = calculate_angle(right_hip, right_knee, right_ankle)
    return l_hip_angle, l_knee_angle, r_hip_angle, r_knee_angle


def find_class(l_hip_angle, l_knee_angle, r_hip_angle, r_knee_angle, landmark_dict):
  visible = check_visibility(landmark_dict)
  logging.debug(f"l_hip_angle, l_knee_angle, r_hip_angle, r_knee_angle: {l_hip_angle, l_knee_angle, r_hip_angle, r_knee_angle}")
  if visible == True:
      if l_hip_angle<120 and l_knee_angle<120 and r_hip_angle<120 and r_knee_angle <120:
        return "sitting"
      else:
        return "standing"
  else: 
    return "Unknown"