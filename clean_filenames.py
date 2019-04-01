from options import Options
import os.path

if __name__ == "__main__":
    # Options
    options = Options().options

    print("Cleaning filenames")
    print()

    print("Loading scene_info.txt")
    scene_info = []
    with open("scene_info.txt", "r") as f:
        for line in f:
            line_stripped = line.strip()
            scene = line_stripped.split(" ")
            scene_info.append(scene)
    print("...Done")
    print()

    print("Removing old information from list")
    for scene in scene_info[:]:
        if not os.path.isfile(scene[0]):
            scene_info.remove(scene)
    print("...Done")
    print()

    print("Updating filenames")
    for scene in scene_info[:]:
        scene[0] = scene[0].split("-")[0] + ".png"
    print("...Done")
    print()

    print("Deleting old information")
    with open("scene_info.txt", "r+") as f:
        f.truncate(0)
    print("...Done")
    print()

    print("Saving new information")
    with open("scene_info.txt", "w") as f:
        for scene in scene_info:
            f.write(" ".join(scene) + "\n")
    print("...Done")
    print()

    print("Renaming image filenames")
    for image_filename in os.listdir(options.output_folder):
        os.rename(os.path.join(options.output_folder, image_filename),
                  os.path.join(options.output_folder, image_filename.split("-")[0] + ".png"))
    print("...Done")
    print()
