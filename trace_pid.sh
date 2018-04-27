#!/bin/bash
timestamp=`date "+%Y%m%d-%H%M%S"`
trace_file="$timestamp.trace"
svg_file="$timestamp.svg"

echo "dtracing for 60 seconds..."
sudo dtrace -x ustackframes=100 -n "profile-97 /pid == $1/ { @[ustack()] = count(); } tick-60s { exit(0); }" -o $trace_file

echo "generating demangled flamegraph..."
./stackcollapse.pl $trace_file | ./rust_demangle.py - | ./flamegraph.pl - > $svg_file

echo "output: $svg_file"
