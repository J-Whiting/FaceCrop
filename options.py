import argparse


class Options:
    def __init__(self):
        self.parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

        self.parser.add_argument("--input_folder", type=str, default="woody//", help="path to images")
        self.parser.add_argument("--output_size", type=int, default=256, help="size in pixels of the output image")

        self.parser.add_argument("--mode", type=str, default="cascade",
                                 help="method to find faces. [cascade | template]")

        # Cascade options
        self.parser.add_argument("--cascade_file", type=str, default="cascade//haarcascade_frontalface_default.xml",
                                 help="filepath to the cascade file")

        # Template options
        self.parser.add_argument("--template_file", type=str, default="template//woody1.png",
                                 help="filepath to the template file")
        self.parser.add_argument("--zoom-steps", type=int, default=20, help="Number of times to resize the template image")

        self.options = self.parser.parse_args()

        # Print the option values to the console
        self.print()

    def print(self):
        args = vars(self.options)

        print('------------ Options -------------')
        for k, v in sorted(args.items()):
            print('%s: %s' % (str(k), str(v)))
        print('-------------- End ----------------')
