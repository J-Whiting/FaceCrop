import cv2 as cv
import numpy as np
from options import Options
import os.path

if __name__ == "__main__":
    # Options
    options = Options().options

    # Looping over the images in the output folder
    files = []
    for image_filename in os.listdir(options.output_folder):
        files.append(int(image_filename.split("-")[0].split(".")[0]))

    files = sorted(files)

    scene_current = files[0]
    scene_start = files[0]
    scenes = {}
    for i in range(0, len(files)):
        if files[i] == (files[i - 1] + 1):
            scenes[scene_start] += 1
        else:
            scene_start = files[i]
            scenes[scene_start] = 1

    # Limiting the output to scenes when they have at least 5 frames in the scene
    scenes = {k: v for k, v in scenes.items() if v >= 5}

    #for scene in sorted(scenes, key=scenes.get, reverse=True):
    #    print(scene, scenes[scene])

    for k, v in scenes.items():
        for i in range(k, k + v - 2):
            n1 = cv.imread(os.path.join(options.output_folder, str(i) + ".png"))
            n2 = cv.imread(os.path.join(options.output_folder, str(i + 1) + ".png"))
            n3 = cv.imread(os.path.join(options.output_folder, str(i + 2) + ".png"))

            combined = np.concatenate((n1, n2, n3), axis=1)

            print(os.path.join("triples", str(i) + ".png"))
            cv.imwrite(os.path.join("triples", str(i) + ".png"), combined)
