# stand-sit-detection
def get_landmarks_interst(detection_result):

  lm = keypoints.pose_landmarks
  lmPose  = mp_pose.PoseLandmark
  # Left shoulder.
  l_shldr_x = int(lm.landmark[lmPose.LEFT_SHOULDER].x * w)
  l_shldr_y = int(lm.landmark[lmPose.LEFT_SHOULDER].y * h)
  
  # Right shoulder.
  r_shldr_x = int(lm.landmark[lmPose.RIGHT_SHOULDER].x * w)
  r_shldr_y = int(lm.landmark[lmPose.RIGHT_SHOULDER].y * h)
  

  
  # Left hip.
  l_hip_x = int(lm.landmark[lmPose.LEFT_HIP].x * w)
  l_hip_y = int(lm.landmark[lmPose.LEFT_HIP].y * h)

  # Right hip.
  r_hip_x = int(lm.landmark[lmPose.RIGHT_HIP].x * w)
  r_hip_y = int(lm.landmark[lmPose.RIGHT_HIP].y * h)

  
  # Left knee.
  l_knee_x = int(lm.landmark[lmPose.LEFT_KNEE].x * w)
  l_knee_y = int(lm.landmark[lmPose.LEFT_KNEE].y * h)

  # Right knee.
  r_knee_x = int(lm.landmark[lmPose.RIGHT_KNEE].x * w)
  r_knee_y = int(lm.landmark[lmPose.RIGHT_KNEE].y * h)

  # Left ankle.
  l_ankle_x = int(lm.landmark[lmPose.LEFT_ANKLE].x * w)
  l_ankle_y = int(lm.landmark[lmPose.LEFT_ANKLE].y * h)

  # Right ankle.
  r_ankle_x = int(lm.landmark[lmPose.RIGHT_ANKLE].x * w)
  r_ankle_y = int(lm.landmark[lmPose.RIGHT_ANKLE].y * h)