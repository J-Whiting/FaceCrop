from options import Options
import os.path

if __name__ == "__main__":
    # Options
    options = Options().options

    print("Loading the images")
    files = []
    # Looping over the images in the output folder
    for image_filename in os.listdir(options.output_folder):
        files.append(int(image_filename.split(".")[0]))
    print("...Done")
    print()

    # Sorting the files numerically
    files = sorted(files)

    print("Generating missing images list")
    gap_start = files[0]
    gaps = {}
    # Looping over all the files
    for i in range(0, len(files) - 1):
        if (files[i] + 1) != files[i + 1]:
            gap = files[i + 1] - (files[i] + 1)
            if gap in gaps:
                gaps[gap] += 1
            else:
                gaps[gap] = 1

    print("...Done")
    print()

    # Checking if gaps contains missing images
    if gaps:
        # If so, print out the missing image information
        print("Missing Images Size > Count")
        for k, v in sorted(gaps.items()):
            print(k, ">", v)
    else:
        # Otherwise no missing images found
        print("No Missing Images found")
