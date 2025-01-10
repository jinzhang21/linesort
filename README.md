# Description
This repository contains a single Python program that takes in a directory of text files,
sorts and dedups all lines lexicographically, and outputs to a destination file.

# Algorithmic consideration
There are many ways to reach a solution. For example,
1. Load all files into memory, each line is an element in an array, sort, dedup then output it to a file.
This approach is not very scalable, however, limited by the memory size of the machine.
2. Since all files are already sorted by itself, we can just load only 1 line from each file into memory,
do a k-way merge (k files in total), dedup on spot, and output the results.
It's much more scalable since it treats files as streams. The main limiting factor is the disk I/O.
3. This is out of scope, but if the files are located in the cloud (distributed on many machines),
instead of downloading all files to a single machine and carry out approch 2,
alternatively one can run map reduce directly via Apache Spark or Apache Beam.
The pro is that it can handle really large amount of files (PBs or more).
The con is it will be costly to run, write and maintain.
We leave this option as a mental excercise here,
given the task at hand is just to sort a local directory.

We use solution 2 in the implementation given the constraints.

# How to run
The program is written in Python 3, depending on only Python STL. To run it, simply type
```
python linesort.py --input_dir=${INPUT_DIR} --output_file=${OUTPUT_FILE}
```

To run the test:
```
python test_linesort.py
```
