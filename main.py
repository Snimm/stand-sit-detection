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
from pos import get_interst_landmards 
mp_pose = mp.solutions.pose



def cv2_imshow(cv2_image):
  cv2_image = cv2.resize(cv2_image, (960, 540))
  cv2.imshow('MediaPipe Pose', cv2_image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()




image_path = "test_resource/download (2).jpeg"
# img = cv2.imread(image_path)
# cv2_imshow(img)



# STEP 2: Create an PoseLandmarker object.
base_options = python.BaseOptions(model_asset_path='pose_landmarker_full.task')
options = vision.PoseLandmarkerOptions(
    base_options=base_options,
    output_segmentation_masks=True)
detector = vision.PoseLandmarker.create_from_options(options)

# STEP 3: Load the input image.
image = mp.Image.create_from_file(image_path)

# STEP 4: Detect pose landmarks from the input image.
detection_result = detector.detect(image)

# STEP 5: Process the detection result. In this case, visualize it.
annotated_image = draw_landmarks_on_image(image.numpy_view(), detection_result)
annotated_image= draw_image(0.5, annotated_image, 0.5)
cv2_imshow(cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR))

#get landmarks of hips
lm = detection_result.pose_landmarks
# lmPose  = mp_pose.PoseLandmark[0]
# Left shoulder.


pp = pprint.PrettyPrinter(indent=4)
person = 0
landmark_point = 32

person_landmark = detection_result.pose_world_landmarks[person]


get_interst_landmards(person_landmark)