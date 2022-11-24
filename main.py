import threading
import time

import cv2
from pupil_apriltags import Detector

import constants
import graphics
import gyro
import network
import pose

camera = cv2.VideoCapture(constants.CAMERA_PORT)
camera.set(cv2.CAP_PROP_EXPOSURE, constants.CAMERA_EXPOSURE)

tag_detector = Detector(families="tag36h11")

r_gyro = gyro.Gyro()
gyro_thread = threading.Thread(target=r_gyro.run_gyro)
gyro_thread.start()

# Main Control Loop
while True:

    # Start of profiling
    start_time = time.time()

    network.log_camera_open(camera.isOpened())

    ret, frame = camera.read()

    # Convert to grayscale or processing
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Search for tags
    detections = tag_detector.detect(img=gray_frame, estimate_tag_pose=True,
                                     camera_params=(646, 645, 640, 400), tag_size=.02)

    for detection in detections:
        n_pose = pose.normalize_pose(detection)

        if constants.ENABLE_GRAPHICS:
            graphics.annotate(frame, detection, n_pose)

        network.log_pos(detection.tag_id, n_pose[0], n_pose[1], n_pose[2])

    if constants.ENABLE_GRAPHICS:
        cv2.imshow("View", frame)
        c = cv2.waitKey(1)

        # breaks out of loop if esc key is pressed
        if c == 27:
            o_gyro.stop()
            break

    # End of profiling
    network.log_looptime(time.time() - start_time)
    network.flush()

camera.release()
cv2.destryAllWindows()
