import cv2 as cv
import numpy as np
from options import Options
import sys


def main():

    # Options
    options = Options().get_options()

    # Files
    image_file = "woody//00001.png"
    template_file = "template//woody1.png"

    # Load the images
    image = cv.imread(image_file)

    # Convert to grayscale
    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    image_gray = cv.equalizeHist(image_gray)

    if options.mode == "cascade":
        # Load the cascade file
        cascade_file = cv.CascadeClassifier("cascade//haarcascade_frontalface_default.xml")

        # Detect faces in the image
        rects = cascade_file.detectMultiScale(
            image_gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv.CV_HAAR_SCALE_IMAGE
        )


        # TODO:
        rects[:, 2:] += rects[:, :2]

        # Draw rectangles over the matches
        for (x, y, w, h) in rects:
            cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    elif options.mode == "template":
        # Load the template file

        template = cv.imread(template_file)

        # Convert to grayscale
        template_gray = cv.cvtColor(template, cv.COLOR_BGR2GRAY)

        # Get template height and width
        w, h = template_gray.shape[::-1]

        # Apply template Matching
        res = cv.matchTemplate(image_gray, template_gray, cv.TM_CCOEFF_NORMED)
        threshold = 0.4
        print(np.max(res))

        """if np.any(res >= threshold):
            _, _, _, max_loc = cv2.minMaxLoc(res)
    
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
    
            cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), 2)"""

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
