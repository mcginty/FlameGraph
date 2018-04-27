#!/usr/bin/env python3

import re
import sys

SUBS = [
  [r'\$u20\$', r' '],
  [r'\$u27\$', r"'"],
  [r'\$u5b\$', r'['],
  [r'\$u5d\$', r']'],
  [r'\$u7b\$', r'{'],
  [r'\$u7d\$', r'}'],
  [r'\$u7e\$', r'~'],
  [r'\$C\$',   r','],
  [r'\$SP\$',  r'@'],
  [r'\$BP\$',  r'*'],
  [r'\$RF\$',  r'&'],
  [r'\$LT\$',  r'<'],
  [r'\$GT\$',  r'>'],
  [r'\$LP\$',  r'('],
  [r'\$RP\$',  r')'],
  [r'\.\.', r'::'],
  [r'`_', r'`'],
  [r'::_', r'::'],
  [r'::h[0-9a-f]{16}', r''],
]

def demangle_line(line):
    demangled = line.rstrip()
    for sub in SUBS:
      demangled = re.sub(sub[0], sub[1], demangled)
    print(demangled)

if sys.argv[1] == '-':
  for line in sys.stdin:
    demangle_line(line)
else:
  with open(sys.argv[1]) as f:
    for line in f:
      demangle_line(line)
