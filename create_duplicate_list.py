from options import Options
import os.path

if __name__ == "__main__":
    # Options
    options = Options().options

    print("Generating duplicate list")
    dictionary = {}
    # Looping over the images in the output folder
    for image_filename in os.listdir(options.output_folder):
        frame = image_filename.split("-")[0]
        if frame not in dictionary:
            dictionary[frame] = 1
        else:
            dictionary[frame] += 1

    for k, v in sorted(dictionary.items()):
        if v > 1:
            print(k, ">", v)
