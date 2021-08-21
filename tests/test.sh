#! /usr/bin/bash
for inputfile in tests/input/*.txt; do
    outputfile=tests/output/$(basename $inputfile)
    touch $outputfile 
    python health_tracker.py < $inputfile > $outputfile
done