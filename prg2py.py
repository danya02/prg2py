#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser(description="Translate .prg code into Python.")
parser.add_argument("input", type=argparse.FileType('r'), help="the input file containg the .prg code")
parser.add_argument("output", type=argparse.FileType('w'), help="the file to which the Python code will be written")

args = parser.parse_args()

# TODO: actual translation.
args.output.write(args.input.read())
