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
from draw import draw_image
from pos import find_angles, get_interest_landmarks, find_class
mp_pose = mp.solutions.pose




def cv2_imshow(cv2_image):
  # cv2_image = cv2.resize(cv2_image, (960, 540))
  cv2.imshow('MediaPipe Pose', cv2_image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

def main(image_path:str)->str:

    # Create options for the PoseLandmarker
    base_options = python.BaseOptions(model_asset_path='pose_landmarker_full.task')
    options = vision.PoseLandmarkerOptions(
        base_options=base_options,
        output_segmentation_masks=True
    )
    
    # Create a PoseLandmarker detector using the specified options
    detector = vision.PoseLandmarker.create_from_options(options)

    # Load the input image using mediapipe.Image
    image = mp.Image.create_from_file(image_path)
    print("image_type", type(image))

    # Detect poses in the image
    detection_result = detector.detect(image)

    # Check if any pose was detected
    if len(detection_result.pose_world_landmarks) == 0:
        print('No pose found.')
        exit()

    # Extract landmarks of interest from the detected pose
    landmark_dict = get_interest_landmarks(detection_result.pose_world_landmarks[0])

    # Calculate angles for relevant joints
    l_hip_angle, l_knee_angle, r_hip_angle, r_knee_angle = find_angles(landmark_dict)

    # Determine the class based on the calculated angles and landmarks
    output_class = find_class(l_hip_angle, l_knee_angle, r_hip_angle, r_knee_angle, landmark_dict)

    # Convert mediapipe.Image to numpy array
    image = image.numpy_view()

    # Draw annotations on the image based on the determined class
    annotated_image = draw_image(image, output_class)
    annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR)
    # Display the annotated image using OpenCV
    # 
    #save in image in current directory
    image_name = image_path.split("/")[-1]
    write_name  = f"proc_{image_name}"
    cv2.imwrite(write_name, annotated_image)
    
    print("image saved as", write_name)
    print("person is", output_class)
    cv2_imshow(annotated_image)
    return output_class

if __name__ == '__main__':
  image_path = input("Enter image path: ")
  main(image_path)  