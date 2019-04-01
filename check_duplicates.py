from options import Options
import os.path

if __name__ == "__main__":
    # Options
    options = Options().options

    print("Generating duplicate list")
    frames = {}
    # Looping over the images in the output folder
    for image_filename in os.listdir(options.output_folder):

        # Getting the frame index from the filename
        frame = image_filename.split("-")[0]

        # Checking if the frame is already in the frames dictionary
        if frame in frames:
            # If so, increment its count
            frames[frame] += 1
        else:
            # Otherwise add it to the dictionary
            frames[frame] = 1
    print("...Done")
    print()

    # Limiting the output to frames if they contain duplicates
    frames = {k: v for k, v in frames.items() if v > 1}

    # Checking if frames contains duplicated values
    if frames:
        # If so, print out the duplicate information
        print("Frame Index > Duplicate Count")
        for k, v in sorted(frames.items()):
            print(k, ">", v)
    else:
        # Otherwise no duplicates found
        print("No duplicates found")
