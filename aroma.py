#!/usr/bin/python
import argparse
from transform import *

parser = argparse.ArgumentParser()
parser.add_argument("--add_parameter", help="perform an add parameter refactoring")
args = parser.parse_args()

if args.add_parameter:
	add_parameter.aptest()
