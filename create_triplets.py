import cv2 as cv
import numpy as np
from options import Options
import os.path

if __name__ == "__main__":
    # Options
    options = Options().options

    # Check whether `triplets` folder exists
    if not os.path.exists("triplets"):
        print("Creating triplets folder")
        os.makedirs("triplets")
        print("...Done")
        print()

    # Looping over the images in the output folder
    files = []
    for image_filename in os.listdir(options.output_folder):
        files.append(int(image_filename.split("-")[0].split(".")[0]))

    # Sorting the files numerically
    files = sorted(files)

    scene_current = files[0]
    scene_start = files[0]
    scenes = {}
    # Making a dictionary of how many frames are in each 'scene', without gaps
    for i in range(0, len(files)):
        if files[i] == (files[i - 1] + 1):
            scenes[scene_start] += 1
        else:
            scene_start = files[i]
            scenes[scene_start] = 1

    # Limiting the output to scenes if they have at least 5 frames
    scenes = {k: v for k, v in scenes.items() if v >= 5}

    # TODO: Debug (Outputs the longest scenes)
    """for scene in sorted(scenes, key=scenes.get, reverse=True):
        print(scene, scenes[scene])"""

    # Looping over all scenes
    print("Creating triples")
    for k, v in scenes.items():

        # Looping over the frames in each scene
        for i in range(k, k + v - 2):

            # Load the n, n+1 and n+2 frames
            n1 = cv.imread(os.path.join(options.output_folder, str(i) + ".png"))
            n2 = cv.imread(os.path.join(options.output_folder, str(i + 1) + ".png"))
            n3 = cv.imread(os.path.join(options.output_folder, str(i + 2) + ".png"))

            # Concatenate the images horizontally
            combined = np.concatenate((n1, n2, n3), axis=1)

            # Save the combined image
            print(os.path.join("triplets", str(i) + ".png"))
            cv.imwrite(os.path.join("triplets", str(i) + ".png"), combined)

    print("...Done")
    print()
