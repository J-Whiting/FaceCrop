import argparse


class Options:
    def __init__(self):
        self.parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    def get_options(self):
        self.parser.add_argument('--input_folder', type=str, default='.', help='path to images')
        self.parser.add_argument('--mode', type=str, default='cascade',
                                 help='method to find faces. [cascade | template]')

        self.opt = self.parser.parse_args()
        args = vars(self.opt)

        print('------------ Options -------------')
        for k, v in sorted(args.items()):
            print('%s: %s' % (str(k), str(v)))
        print('-------------- End ----------------')

        return self.opt
