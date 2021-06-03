import argparse
import os.path
import sys

from nemesistool import NemesisInstrumentProgram
from latency_map.create_latency_map import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def visualize_cfg(input_binary, func_name, output_dir):
    tool = NemesisInstrumentProgram(input_binary, "")
    func = tool.functions[func_name]
    img = func.render_cfg()
    binary_name = os.path.split(input_binary)[-1]
    output_file = os.path.join(output_dir, f"{binary_name}_{func_name}.png")
    mpimg.imsave(output_file, img)


def align_cfg(input_binary, target_instructions, output_dir):
    binary_name = os.path.split(input_binary)[-1]
    output_binary = os.path.join(output_dir, f"{binary_name}_rw.s")

    tool = NemesisInstrumentProgram(input_binary, output_binary)
    tool.instrument_program(target_instructions)

    tool.dump()


def main(main_input):
    # single top-level parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    # visualize subparser
    visualize = subparsers.add_parser('visualize', help='Visualize CFG for a function in binary')
    visualize.add_argument("--binary", "-b", required=True, help="path to input binary")
    visualize.add_argument("--function", "-f", default="main", help="name of target function")
    visualize.add_argument("--output_dir", "-o", default="output", help="output directory")

    # align suparser
    align = subparsers.add_parser("align", help='align instructions in CFG given input binar and secret-dependent '
                                                'instructions')
    align.add_argument("-b", "--binary", required=True, help="path to input binary")
    align.add_argument("-f", "--function", default="main", help="name of target function")
    align.add_argument('-t', '--targets', nargs='+', help='Set of target secret-dependent instructions in hexadecimal', required=True)
    align.add_argument("-o", "--output_dir", default="output", help="output directory")

    args = parser.parse_args(main_input[1:])
    if args.command == 'visualize':
        visualize_cfg(args.binary, args.function, args.output_dir)
    elif args.command == 'align':
        align_cfg(args.binary, args.targets, args.output_dir)


if __name__ == '__main__':
    main(sys.argv)
