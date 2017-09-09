#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import datetime

version = "0.1a"
parser = argparse.ArgumentParser(description="Translate .prg code into Python.")
parser.add_argument("input", type=argparse.FileType('r'), help="the input file containg the .prg code")
parser.add_argument("output", type=argparse.FileType('w', 0), help="the file to which the Python code will be written")

global args
args = parser.parse_args()

global input_data
input_data = args.input.read()

def output(line, newline=True):
    args.output.write(line)
    if newline:
        args.output.write("\n")

output('#/usr/bin/python3')
output('# -*- coding: utf-8 -*-')
output('')
output('# Generated using prg2py v.' + version + ' at ' + datetime.datetime.now().isoformat())
output('# (https://github.com/danya02/py2prg/)')
output('')
output('import turtle')
output('from math import *')
output('')
output('turtle.mode(mode="logo")')

args.output.flush()
