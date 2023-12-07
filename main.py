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
from pos import get_interst_landmards, check_visibility, find_class, find_angles, calculate_angle
mp_pose = mp.solutions.pose



def cv2_imshow(cv2_image):
  cv2_image = cv2.resize(cv2_image, (960, 540))
  cv2.imshow('MediaPipe Pose', cv2_image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()




image_path = "test_resource/sport-ball-kind-274494.jpg"
# img = cv2.imread(image_path)
# cv2_imshow(img)



# STEP 2: Create an PoseLandmarker object.
base_options = python.BaseOptions(model_asset_path='pose_landmarker_full.task')
options = vision.PoseLandmarkerOptions(
    base_options=base_options,
    output_segmentation_masks=True)
detector = vision.PoseLandmarker.create_from_options(options)

image = mp.Image.create_from_file(image_path)



detection_result = detector.detect(image)
#pp.pprint(detection_result.pose_world_landmarks[0][0])
landmark_dict = get_interst_landmards(detection_result.pose_world_landmarks[0])
# pp.pprint(landmark_dict)


# STEP 5: Process the detection result. In this case, visualize it.
annotated_image = draw_landmarks_on_image(image.numpy_view(), detection_result)


l_hip_angle, l_knee_angle, r_hip_angle, r_knee_angle = find_angles(landmark_dict)
output_class = find_class(l_hip_angle, l_knee_angle, r_hip_angle, r_knee_angle, landmark_dict)
annotated_image= draw_image(0.5, annotated_image, 0.5, output_class)
cv2_imshow(cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR))

#get landmarks of hips
lm = detection_result.pose_landmarks
# lmPose  = mp_pose.PoseLandmark[0]
# Left shoulder.


person = 0
landmark_point = 32

person_landmark = detection_result.pose_world_landmarks[person]


get_interst_landmards(person_landmark)