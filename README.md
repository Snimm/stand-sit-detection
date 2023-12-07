# Stand-Sit Detection Project

This project utilizes the MediaPipe library to detect human poses in images and classifies them based on whether the person is sitting, standing, or if the lower half of the body is not visible (unknown).

## Classification Criteria

The classification is based on the angles formed by the knees and hips. Specifically:

- If all angles formed by the knees and hips are less than 120 degrees, the person is classified as **sitting**.
- If any of the angles exceeds 120 degrees, the person is classified as **standing**.
- If the lower half of the body is not visible, the person is classified as **unknown**.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Snimm/stand-sit-detection
    cd stand-sit-detection
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the main script:

    ```bash
    python main.py
    ```

2. Enter the file path of the image you want to classify.

3. View the annotated images with detected poses and classifications.

4. The annotated image is saved as `proc_{image_name}` in the `stand-sit-detection` folder.

## Project Structure

- `main.py`: Main script to run the pose detection and classification.
- `draw.py`: Module for drawing annotations on images based on pose classifications.
- `pos.py`: Module for pose-related functions (e.g., calculating angles, extracting landmarks).
- `test/`: Directory containing files for unit tests.

## Dependencies

- `mediapipe`: MediaPipe library for pose detection and landmarks.
- `numpy`: For numerical operations on landmarks.
- `opencv-python`: OpenCV for image processing and visualization.
