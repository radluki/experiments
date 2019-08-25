#!/usr/bin/env python3
import re
from argparse import ArgumentParser
from tqdm import tqdm

parser = ArgumentParser()
parser.add_argument("-r", "--regex", required=True)
parser.add_argument("-f", "--filename", required=True)
parser.add_argument("-m", "--mode", type=int, default=0)

args = parser.parse_args()

regexp = re.compile(args.regex)
def listGrep(f):
	return (x for x in f.readlines() if regexp.search(x))


def reGrep(f):
	return (m.group() + "\n" for m in regexp.finditer(f.read(), re.M))


def generatorGrep(f):
	yield from (line for line in f if regexp.search(line))
	

modes = [listGrep, reGrep, generatorGrep]
	

with open(args.filename, "r") as f:
	for x in tqdm(modes[args.mode](f)):
		print(x, end="")
