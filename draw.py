import numpy as np
import mediapipe as mp
from mediapipe.framework.formats import landmark_pb2
from mediapipe.python import solutions
import cv2
import pprint


def draw_landmarks_on_image(rgb_image, detection_result):
    
    pose_landmarks_list = detection_result.pose_landmarks
    annotated_image = np.copy(rgb_image)


    # Loop through the detected poses to visualize.
    for idx in range(len(pose_landmarks_list)):

        pose_landmarks = pose_landmarks_list[idx]
        # Draw the pose landmarks.
        pose_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
        pose_landmarks_proto.landmark.extend([
        landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in pose_landmarks
        ])
        solutions.drawing_utils.draw_landmarks(
        annotated_image,
        pose_landmarks_proto,
        solutions.pose.POSE_CONNECTIONS,
        solutions.drawing_styles.get_default_pose_landmarks_style())
    return annotated_image



# lm = keypoints.pose_landmarks
# lmPose  = mp_pose.PoseLandmark
# # Left shoulder.
# l_shldr_x = int(lm.landmark[lmPose.LEFT_SHOULDER].x * w)
# l_shldr_y = int(lm.landmark[lmPose.LEFT_SHOULDER].y * h)
 
# # Right shoulder.
# r_shldr_x = int(lm.landmark[lmPose.RIGHT_SHOULDER].x * w)
# r_shldr_y = int(lm.landmark[lmPose.RIGHT_SHOULDER].y * h)
 

 
# # Left hip.
# l_hip_x = int(lm.landmark[lmPose.LEFT_HIP].x * w)
# l_hip_y = int(lm.landmark[lmPose.LEFT_HIP].y * h)

# # Right hip.
# r_hip_x = int(lm.landmark[lmPose.RIGHT_HIP].x * w)
# r_hip_y = int(lm.landmark[lmPose.RIGHT_HIP].y * h)

 
# # Left knee.
# l_knee_x = int(lm.landmark[lmPose.LEFT_KNEE].x * w)
# l_knee_y = int(lm.landmark[lmPose.LEFT_KNEE].y * h)

# # Right knee.
# r_knee_x = int(lm.landmark[lmPose.RIGHT_KNEE].x * w)
# r_knee_y = int(lm.landmark[lmPose.RIGHT_KNEE].y * h)

# # Left ankle.
# l_ankle_x = int(lm.landmark[lmPose.LEFT_ANKLE].x * w)
# l_ankle_y = int(lm.landmark[lmPose.LEFT_ANKLE].y * h)

# # Right ankle.
# r_ankle_x = int(lm.landmark[lmPose.RIGHT_ANKLE].x * w)
# r_ankle_y = int(lm.landmark[lmPose.RIGHT_ANKLE].y * h)




def draw_image(sittingness: float, image: cv2.Mat, sittingness_threshold: float) -> cv2.Mat:
    Fontsize=5

    # Determine jaw class based on the threshold
    class_pos = "Sitting" if sittingness > sittingness_threshold else "standing"
    
    # Create text to put on the image
    text_to_put = f"{class_pos}"
    text_location = (image.shape[1] -170*Fontsize,  40*Fontsize)

    # Put text on the image
    put_text(image, text_to_put, text_location, Fontsize)

    return image

def put_text(image, text_to_put, text_location, size):
    cv2.putText(image, text_to_put, text_location, cv2.FONT_HERSHEY_COMPLEX, size, (255, 255, 255), 4*size, cv2.LINE_AA)
    cv2.putText(image, text_to_put, text_location, cv2.FONT_HERSHEY_COMPLEX, size, (0, 0, 0), size, cv2.LINE_AA)