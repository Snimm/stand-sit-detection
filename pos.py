import math

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
    vec1 = [point2.x - point1.x, point2.y - point1.y, point2.z - point1.z]
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
  for i in range(33):
    print(i)
    dict_landmark = {}
    if i == 11:
      dict_landmark['left_shoulder'] = person_landmark[i]
    elif i == 12:
      dict_landmark['right_shoulder'] = person_landmark[i]
    elif i == 23:
      dict_landmark['left_hip'] = person_landmark[i]
    elif i == 24:
      dict_landmark['right_hip'] = person_landmark[i]
    elif i == 25:
      dict_landmark['left_knee'] = person_landmark[i]
    elif i == 26:
      dict_landmark['right_knee'] = person_landmark[i]
    elif i == 27:
      dict_landmark['left_ankle'] = person_landmark[i]
    elif i == 28:
      dict_landmark['right_ankle'] = person_landmark[i]
      
  return dict_landmark


def check_visibility(landmark_dict):
    for key in landmark_dict:
        if landmark_dict[key].visibility < 0.5:
            return False
    return True


def check_sittingness(landmark_dict):
    left_shoulder = landmark_dict['left_shoulder']
    right_shoulder = landmark_dict['right_shoulder']
    left_hip = landmark_dict['left_hip']
    right_hip = landmark_dict['right_hip']
    left_knee = landmark_dict['left_knee']
    right_knee = landmark_dict['right_knee']
    left_ankle = landmark_dict['left_ankle']
    right_ankle = landmark_dict['right_ankle']



    return False
