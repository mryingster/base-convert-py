#!/usr/bin/python
import sys, os

mode=sys.argv[0]

# Binary conversion
def bin2oct(input): return oct(int(str(input),2))
def bin2dec(input): return int(int(str(input),2))
def bin2hex(input): return hex(int(str(input),2))

# Octal conversion
def oct2bin(input): return bin(int(str(input),8))
def oct2dec(input): return int(int(str(input),8))
def oct2hex(input): return hex(int(str(input),8))

# Decimal converison
def dec2bin(input): return bin(int(str(input),10))
def dec2oct(input): return oct(int(str(input),10))
def dec2hex(input): return hex(int(str(input),10))

# Hexedecimal conversion
def hex2bin(input): return bin(int(str(input),16))
def hex2oct(input): return oct(int(str(input),16))
def hex2dec(input): return int(int(str(input),16))

def ProcessInput(input):
    import re
    reBIN='^0?b?[01]+$'
    reOCT='^[0-7]+$'
    reDEC='^[0-9]+$'
    reHEX='^0?x?[0-9A-Fa-f]+$'
    reASC='^.+$'

    if   mode.endswith("bin2oct"): return bin2oct(input) if re.match(reBIN, input) else "Non binary input, %s." % input
    elif mode.endswith("bin2dec"): return bin2dec(input) if re.match(reBIN, input) else "Non binary input, %s." % input
    elif mode.endswith("bin2hex"): return bin2hex(input) if re.match(reBIN, input) else "Non binary input, %s." % input
    elif mode.endswith("oct2bin"): return oct2bin(input) if re.match(reOCT, input) else "Non octal input, %s." % input
    elif mode.endswith("oct2dec"): return oct2dec(input) if re.match(reOCT, input) else "Non octal input, %s." % input
    elif mode.endswith("oct2hex"): return oct2hex(input) if re.match(reOCT, input) else "Non octal input, %s." % input
    elif mode.endswith("dec2bin"): return dec2bin(input) if re.match(reDEC, input) else "Non decimal input, %s." % input
    elif mode.endswith("dec2oct"): return dec2oct(input) if re.match(reDEC, input) else "Non decimal input, %s." % input
    elif mode.endswith("dec2hex"): return dec2hex(input) if re.match(reDEC, input) else "Non decimal input, %s." % input
    elif mode.endswith("hex2bin"): return hex2bin(input) if re.match(reHEX, input) else "Non hexidecimal input, %s." % input
    elif mode.endswith("hex2oct"): return hex2oct(input) if re.match(reHEX, input) else "Non hexidecimal input, %s." % input
    elif mode.endswith("hex2dec"): return hex2dec(input) if re.match(reHEX, input) else "Non hexidecimal input, %s." % input
    else: return "Nothing to do..."

# Retrieve input from commandline arguments
if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        print ProcessInput(sys.argv[i])

# Retrieve input from stdin if piped info exists
elif sys.stdin.isatty() != True:
    for input in sys.stdin:
        print ProcessInput(input)

else:
    while True:
        try: input=raw_input()
        except EOFError: break
        print ProcessInput(input)
