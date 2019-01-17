#   Example call:
#    python command_line_arguments.py --dir my_folder/ --num 0

import argparse


def get_input_args():
    # Creates Argument Parser object named parser
    parser = argparse.ArgumentParser()

    # Argument 1: that's a path to a folder
    parser.add_argument("--dir", type=str,
                        default="/Users/carlosmertens/Documents/AI Python Nanodegree/Classifying Images/",
                        help="path to the folder my_folder")

    # Argument 2: that's an integer
    parser.add_argument("--num", type=int, default=1,
                        help="Number (integer) input")

    # Assigns variable in_args to parse_args()
    in_args = parser.parse_args()

    # Accesses values of Arguments 1 and 2 by printing them
    print("Argument 1:", in_args.dir, "  Argument 2:", in_args.num)


in_arg = get_input_args()

in_arg = get_input_args()
print("Command Line Arguments:\n	dir =", in_arg.dir,
      "\n	arch =", in_arg.arch, "\n	dogfile =", in_arg.dogfile)

