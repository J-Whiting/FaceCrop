import cv2 as cv
import numpy as np
from options import Options
import os.path
import sys

if __name__ == "__main__":
    # Options
    options = Options().options

    # Check whether `output_folder` folder exists
    if not os.path.exists(options.output_folder):
        print("Creating " + options.output_folder + " folder")
        os.makedirs(options.output_folder)
        print("...Done")
        print()

    # Load the classifier file
    classifier = cv.CascadeClassifier(options.classifier_file)

    # Opening the video file
    cap = cv.VideoCapture(options.video_file)

    # TODO: Debug
    cap.set(cv.CAP_PROP_POS_FRAMES, 11002)

    while cap.isOpened():

        # Capture frame
        ret, frame = cap.read()

        if ret:
            # Convert to grayscale
            frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            frame_gray = cv.equalizeHist(frame_gray)

            # Detect faces in the image
            rects = classifier.detectMultiScale(frame_gray)

            for (x, y, w, h) in rects:
                # Crop image
                crop = frame[y:y + h, x:x + w]

                # Resize image to `output_size` pixels
                zoom = cv.resize(crop, (options.output_size, options.output_size))

                # Saving the frames
                cv.imwrite(os.path.join(options.output_folder, str(int(cap.get(cv.CAP_PROP_POS_FRAMES))) + ".png"),
                           zoom)

        else:
            break

    # Closing the video file
    cap.release()
