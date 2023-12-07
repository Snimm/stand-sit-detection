# Stand-Sit Detection Project

This project utilizes the MediaPipe library to detect human poses in images and classifies them based on whether the person is sitting, standing, or if the lower half of the body is not visible (unknown).

## Examples 
![proc_download](https://github.com/Snimm/stand-sit-detection/assets/53926889/12f866a6-6acd-41f4-975b-ee90cffb6dd7)
![proc_images](https://github.com/Snimm/stand-sit-detection/assets/53926889/d0bf9e56-6934-4bfa-afe3-bbd698a6c492)
![proc_download (1)](https://github.com/Snimm/stand-sit-detection/assets/53926889/341dc6ab-82ad-4ac2-9972-c894dfae89ef)

![proc_download (2)](https://github.com/Snimm/stand-sit-detection/assets/53926889/d140be46-0b1f-4d0e-b4a3-7dd944fb6f05)


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
