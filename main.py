import mediapipe
import cv2
import numpy as np
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import math
from draw import draw_landmarks_on_image
from draw import draw_image
import pprint
from pos import find_angles, get_interest_landmarks, check_visibility, find_distance, calculate_angle, find_class
mp_pose = mp.solutions.pose



def cv2_imshow(cv2_image):
  cv2_image = cv2.resize(cv2_image, (960, 540))
  cv2.imshow('MediaPipe Pose', cv2_image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()




image_path = "test_resource/images (1).jpeg"
# img = cv2.imread(image_path)
# cv2_imshow(img)



# STEP 2: Create an PoseLandmarker object.
base_options = python.BaseOptions(model_asset_path='pose_landmarker_full.task')
options = vision.PoseLandmarkerOptions(
    base_options=base_options,
    output_segmentation_masks=True)
detector = vision.PoseLandmarker.create_from_options(options)

image = mp.Image.create_from_file(image_path)
print("image_type" , type(image))


detection_result = detector.detect(image)
#pp.pprint(detection_result.pose_world_landmarks[0][0])
if len(detection_result.pose_world_landmarks) == 0:
  print('No pose found.')
  exit()

landmark_dict = get_interest_landmarks(detection_result.pose_world_landmarks[0])
# pp.pprint(landmark_dict)


# STEP 5: Process the detection result. In this case, visualize it.


l_hip_angle, l_knee_angle, r_hip_angle, r_knee_angle = find_angles(landmark_dict)
output_class = find_class(l_hip_angle, l_knee_angle, r_hip_angle, r_knee_angle, landmark_dict)

image = image.numpy_view()


annotated_image= draw_image( image, output_class)
cv2_imshow(cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR))
