#!/usr/bin/python
import argparse
from transform import *

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="input xml file")
parser.add_argument("--add_parameter", help="perform an add parameter refactoring")
parser.add_argument("--pull_up_field", action='store_true', default=False, help="preform a pull up field refactoring")
parser.add_argument("-o", "--output", help="output xml filename")
args = parser.parse_args()

if args.add_parameter:
	add_parameter.refactor(args.input_file, args.add_parameter, args.output)

if args.pull_up_field:
	pull_up_field.refactor(args.input_file, args.output)
