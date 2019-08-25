#!/usr/bin/env python3
import fileinput
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file")
parser.add_argument("-r", "--regex", required=True)
parser.add_argument("-s", "--sub", required=True)

args = parser.parse_args()
r = re.compile(args.regex)

for i, line in enumerate(fileinput.input(files = (args.file,) if args.file else ("-",))):
	print(r.sub(args.sub, line), end="")


