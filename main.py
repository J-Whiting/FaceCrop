import cv2 as cv
import numpy as np
from options import Options
import os.path
import sys


def main():
    # Options
    options = Options().options

    # Files
    image_file = os.path.join(options.input_folder, "00001.png")

    # Load the images
    image = cv.imread(image_file)

    # Convert to grayscale
    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    image_gray = cv.equalizeHist(image_gray)

    if options.mode == "cascade":

        # Load the cascade file
        cascade_file = cv.CascadeClassifier(options.cascade_file)
        eye_file = cv.CascadeClassifier("cascade//haarcascade_eye.xml")

        # Detect faces in the image
        rects = cascade_file.detectMultiScale(
            image_gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(40, 40),
            flags=cv.CASCADE_SCALE_IMAGE
        )

        # Draw rectangles over the matches
        for (x, y, w, h) in rects:
            cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        """TEST"""
        # Detect faces in the image
        rects2 = eye_file.detectMultiScale(
            image_gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv.CASCADE_SCALE_IMAGE
        )

        # Draw rectangles over the matches
        for (x, y, w, h) in rects2:
            cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)

    elif options.mode == "template":

        # Load the template file
        template = cv.imread(options.template_file)

        # Convert to grayscale
        template_gray = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
        template_gray = cv.equalizeHist(template_gray)
        template_width, template_height = template_gray.shape[::-1]

        for i in range(options.zoom_steps):
            for flip in [True, False]:
                scaling_factor = 1 - (i / options.zoom_steps)

                if template_width * scaling_factor < options.output_size:
                    break;

                print()
                print("Scaling Factor: " + str(scaling_factor))

                template_scaled = cv.resize(template_gray.copy(), (0, 0), fx=scaling_factor, fy=scaling_factor, interpolation=cv.INTER_AREA)

                # Flip the template image vertically
                print("Template Flipped: " + str(flip))
                if flip:
                    template_scaled = cv.flip(template_scaled, 1)

                # Get template height and width
                w, h = template_scaled.shape[::-1]

                # Apply template Matching
                res = cv.matchTemplate(image_gray, template_scaled, cv.TM_CCOEFF_NORMED)
                threshold = 0.5
                print(np.max(res))

                """if np.any(res >= threshold):
                    _, _, _, max_loc = cv.minMaxLoc(res)
            
                    top_left = max_loc
                    bottom_right = (top_left[0] + w, top_left[1] + h)
            
                    cv.rectangle(image, top_left, bottom_right, (255, 0, 0), 2)"""

                # Filtering results to examples over the threshold
                location = np.where(res >= threshold)

                # Draw rectangles over the matches
                for x, y in zip(*location[::-1]):
                    cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    else:
        print("Incorrect mode selected")
        sys.exit()

    # cv.imwrite('res.png', image)
    # Show the results
    cv.imshow("", image)
    cv.waitKey(0)


if __name__ == '__main__':
    main()
