from options import Options
import os.path

if __name__ == "__main__":
    # Options
    options = Options().options

    print("Cleaning filenames")
    print()

    print("Loading `scene_info.txt`")
    scene_info = []
    with open("scene_info.txt", "r") as f:
        for line in f:
            line_stripped = line.strip()
            scene = line_stripped.split(" ")
            scene_info.append(scene)
    print("...Done")
    print()

    print("Removing old information from `scene_info.txt`")
    # Looping over all frames in the scene_info file
    for scene in scene_info[:]:
        # Checking whether the associated file does not exists
        if not os.path.isfile(scene[0]):
            # If so, remove its reference from scene_info
            scene_info.remove(scene)
    print("...Done")
    print()

    print("Updating filenames in `scene_info.txt`")
    for scene in scene_info[:]:
        scene[0] = scene[0].split("-")[0] + ".png"
    print("...Done")
    print()

    print("Saving `scene_info.txt`")
    # Deleting old information from `scene_info.txt`
    with open("scene_info.txt", "r+") as f:
        f.truncate(0)

    # Saving new information to `scene_info.txt`
    with open("scene_info.txt", "w") as f:
        for scene in scene_info:
            f.write(" ".join(scene) + "\n")
    print("...Done")
    print()

    print("Renaming output filenames")
    # Looping over all files in the `output_folder`
    for image_filename in os.listdir(options.output_folder):
        # Rename the files, removing "-"
        os.rename(os.path.join(options.output_folder, image_filename),
                  os.path.join(options.output_folder, image_filename.split("-")[0] + ".png"))
    print("...Done")
    print()
