import csv
import cv2 as cv
import math
from options import Options
import os.path


def save_frame(frame_number, x, y, w, h):
    # Opening the video file
    cap = cv.VideoCapture(options.video_file)

    cap.set(cv.CAP_PROP_POS_FRAMES, frame_number - 1)

    if cap.isOpened():
        # Capture frame
        ret, frame = cap.read()

        if ret:
            # Crop image
            crop = frame[y:y + h, x:x + w]

            # Resize image to `output_size` pixels
            zoom = cv.resize(crop, (options.output_size, options.output_size))

            # Saving the frames
            filename = os.path.join(options.output_folder, str(frame_number) + ".png")
            print(filename)
            cv.imwrite(filename, zoom)
            with open("scene_info.txt", "a") as g:
                g.write(filename + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h) + "\n")

    # Closing the video file
    cap.release()


if __name__ == "__main__":
    # Options
    options = Options().options

    gap = 1

    print("Loading scene_info.txt")
    scene_info = []
    with open("scene_info.txt", "r") as f:
        for line in f:
            line_stripped = line.strip()
            scene = line_stripped.split(" ")
            scene_info.append(scene)
    print("...Done")
    print()

    missing_scenes = []
    for i in range(len(scene_info) - 1):
        frame_1 = scene_info[i]
        frame_2 = scene_info[i + 1]
        frame_file_1 = frame_1[0].split("/")[-1]
        frame_file_2 = frame_2[0].split("/")[-1]
        frame_number_1 = int(frame_file_1.split(".")[0])
        frame_number_2 = int(frame_file_2.split(".")[0])

        if frame_number_1 + gap + 1 == frame_number_2:
            frame_x_1 = int(frame_1[1])
            frame_x_2 = int(frame_2[1])
            frame_x_d = (frame_x_2 - frame_x_1) / (gap + 1)
            frame_y_1 = int(frame_1[2])
            frame_y_2 = int(frame_2[2])
            frame_y_d = (frame_y_2 - frame_y_1) / (gap + 1)
            frame_w_1 = int(frame_1[3])
            frame_w_2 = int(frame_2[3])
            frame_w_d = (frame_w_2 - frame_w_1) / (gap + 1)
            frame_h_1 = int(frame_1[4])
            frame_h_2 = int(frame_2[4])
            frame_h_d = (frame_h_2 - frame_h_1) / (gap + 1)

            # print(frame_number_1, frame_x_1, frame_y_1, frame_w_1, frame_h_1)

            for j in range(1, gap + 1):

                frame_number = frame_number_1 + j

                x = math.floor(frame_x_1 + (j * frame_x_d))
                y = math.floor(frame_y_1 + (j * frame_y_d))
                w = math.ceil(frame_w_1 + (j * frame_w_d))
                h = math.ceil(frame_h_1 + (j * frame_h_d))

                # print(frame_number, x, y, w, h)

                save_frame(frame_number, x, y, w, h)

            # print(frame_number_2, frame_x_2, frame_y_2, frame_w_2, frame_h_2)

    print("Sort scene_info.txt")
    with open("scene_info.txt", "r") as f:
        csv = csv.reader(f, delimiter=" ")
        scene_info_sorted = sorted(csv, key=lambda x: int(x[0].split("/")[-1].split(".")[0]))
    print("...Done")
    print()

    print("Deleting old information")
    with open("scene_info.txt", "r+") as f:
        f.truncate(0)
    print("...Done")
    print()

    print("Saving new information")
    with open("scene_info.txt", "w") as f:
        for scene in scene_info_sorted:
            f.write(" ".join(scene) + "\n")
    print("...Done")
    print()
