import cv2
from pupil_apriltags import Detector

import graphics

camera = cv2.VideoCapture(1)

tag_detector = Detector(families="tagStandard41h12", quad_decimate=1,
                        refine_edges=1, decode_sharpening=.25, nthreads=8)

# Check if camera is connected
if not camera.isOpened():
    raise IOError("Cannot access camera")

while True:

    # Start of profiling
    # start_time = time.time()

    ret, frame = camera.read()

    # Convert to grayscale or processing
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Search for tags
    detections = tag_detector.detect(img=gray_frame, estimate_tag_pose=True,
                                     camera_params=(2491, 1401, 640, 360), tag_size=.02)

    for detection in detections:
        graphics.annotate(frame, detection)

    cv2.imshow("View", frame)

    c = cv2.waitKey(1)

    # breaks out of loop if esc key is pressed
    if c == 27:
        break

    # End of profiling
    # print("Loop Time: " + str(time.time() - start_time))

camera.release()
cv2.destryAllWindows()
