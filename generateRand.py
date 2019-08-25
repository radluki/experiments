#!/usr/bin/env python3

import random as r
from tqdm import tqdm
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("number_of_lines", type=int)
parser.add_argument("filename")
args = parser.parse_args()

number_of_values_per_line = 10
with open(args.filename, "w") as f:
    for _ in tqdm( range(args.number_of_lines) ):
        line = [r.random() for _ in range(number_of_values_per_line)]
        f.write(f"{line}\n")
