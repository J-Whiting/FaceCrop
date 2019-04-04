import argparse


class Options:
    def __init__(self):
        self.parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

        self.parser.add_argument("--video_file", type=str, default=r"", help="filename of video file")
        self.parser.add_argument("--classifier_file", type=str, default=r"classifier/haarcascade_frontalface_default.xml",
                                 help="filepath to the classifier file")
        self.parser.add_argument("--output_folder", type=str, default=r"output/", help="path to output folder")
        self.parser.add_argument("--output_size", type=int, default=256, help="size in pixels of the output image")

        self.options = self.parser.parse_args()

        # Print the option values to the console
        args = vars(self.options)

        print('------------ Options -------------')
        for k, v in sorted(args.items()):
            print('%s: %s' % (str(k), str(v)))
        print('-------------- End ----------------')
        print()
