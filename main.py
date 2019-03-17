import sys
import cv2
import numpy as np


def main():
    # Files
    imageFile = "00001.png"
    templateFile = "template.png"

    # Read the images
    image = cv2.imread(imageFile)
    template = cv2.imread(templateFile)

    # Convert to grayscale
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grayTemplate = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    w, h = grayTemplate.shape[::-1]

    # Apply template Matching
    res = cv2.matchTemplate(grayImage, grayTemplate, cv2.TM_CCOEFF_NORMED)
    threshold = 0.4
    print(np.max(res))

    """if np.any(res >= threshold):
        _, _, _, max_loc = cv2.minMaxLoc(res)

        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), 2)"""

    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    # cv2.imwrite('res.png', image)
    cv2.imshow("", image)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
