# DINDIN Meryll
# June 04, 2018
# Dreem Headband Sleep Phases Classification Challenge

import argparse, warnings

from package.dl_model import *

# Main algorithm

if __name__ == '__main__':

    # Initialize the arguments
    prs = argparse.ArgumentParser()
    # Mandatory arguments
    prs.add_argument('-c', '--channels', help='Channels Definition', nargs='*')
    # Parse the arguments
    prs = prs.parse_args()

    # Generate the corresponding channels
    dic = generate_channels(prs.channels)

    # Build a new database
    Database().preprocess('./dataset/DTB_Headband.h5', test=0.33)

    # Build and launch the corresponding DL model
    mod = DL_Model('./dataset/DTB_Headband.h5', dic)
    mod.learn()
    mod.write_to_file()


