#!/usr/bin/env python3
import re
from argparse import ArgumentParser
from tqdm import tqdm
import sys

parser = ArgumentParser()
parser.add_argument("-r", "--regex", required=True)
parser.add_argument("-f", "--filename", required=True)

args = parser.parse_args()

regexp = re.compile(args.regex)

n=0
cr='\r'
with open(args.filename, "r") as f:
	for i, line in enumerate(f):
		if i % 100000 == 0:
			n = len(str(i))+1
			print(f"{cr*n}{i}", file=sys.stderr, end="")
		if regexp.search(line):
			print(line, end="")
