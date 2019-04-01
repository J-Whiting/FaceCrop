import cv2 as cv
from options import Options
import os.path

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

    # Read the scene list into the list
    with open("scenes.txt", "r") as f:
        s = f.read().split("\n")
    print(s)

    # Create scene tuples
    scenes = []
    if len(s) == 0:
        # If scenes.txt is empty, check all scenes in the video
        scenes.append(0, float("inf"))
    else:
        # Otherwise declare all individual scenes into a start frame and end frame
        for i in s:
            p = i.split(":")
            scenes.append((int(p[0]), int(p[1])))

    print(scenes)

    for scene in scenes:

        # TODO: Debug
        # cap.set(cv.CAP_PROP_POS_FRAMES, 29992)
        cap.set(cv.CAP_PROP_POS_FRAMES, scene[0])

        while cap.isOpened():
            #
            # Capture frame
            ret, frame = cap.read()

            if int(cap.get(cv.CAP_PROP_POS_FRAMES)) >= scene[1]:
                break

            if ret:
                # Convert to grayscale
                frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                frame_gray = cv.equalizeHist(frame_gray)

                # Detect faces in the image
                rects = classifier.detectMultiScale(frame_gray)

                i = 1
                for (x, y, w, h) in rects:

                    if w < 256:
                        continue

                    # Crop image
                    crop = frame[y:y + h, x:x + w]

                    # Resize image to `output_size` pixels
                    zoom = cv.resize(crop, (options.output_size, options.output_size))

                    # Saving the frames
                    filename = os.path.join(options.output_folder,
                                            str(int(cap.get(cv.CAP_PROP_POS_FRAMES))) + "-" + str(i) + ".png")
                    print(filename)
                    cv.imwrite(filename, zoom)
                    with open("scene_info.txt", "a") as scene_info:
                        scene_info.write(filename + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h) + "\n")
                    # cv.imwrite(os.path.join(options.output_folder, str(int(cap.get(cv.CAP_PROP_POS_FRAMES))) + ".png"), zoom)
                    i += 1

            else:
                break

    # Closing the video file
    cap.release()
