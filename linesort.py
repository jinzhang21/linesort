"""
Sort and dedup text file contents in a directory. Lines are deduped and sorted lexicographically.
Empty lines are omitted.
Note that
1. sub-directories are not traversed.
2. Spaces are considered valid characters and will be sorted against alphabets.

For instance, if the input directory contains:
input_dir/a.txt:
apple
banana

cactus

input_dir/b.txt:
apple banana

dinosaur
dinosaur
frankfurter

The output of your program should be:
apple
apple banana
banana
cactus
dinosaur
frankfurter
"""

from typing import Optional, Iterator

import argparse
import os


class LineSort:
    def __init__(self, base_dir: str, output_file: str) -> None:
        self.base_dir = base_dir
        self.output_file = output_file
    
    def _get_next_line(self, file) -> Optional[str]:
        """Returns the content of next line or None if reaching end of the file. Empty lines are skipped."""
        line = "\n"
        while line == "\n":
            line = file.readline()
            if not line: return None
        return line
    
    def run(self) -> None:
        """Runs all logic to sort and output."""
        from heapq import heapify, heappush, heappop

        # Get the iterator for all text files under base_dir and the output iterator
        file_paths = filter(os.path.isfile, [os.path.join(self.base_dir, f) for f in os.listdir(self.base_dir)])
        files = [open(f, mode="r") for f in file_paths]
        output = open(self.output_file, mode="w")
        
        # Construct a min-heap, do the standard k-way merge
        heap = []
        for file in files:
            next_line = self._get_next_line(file)
            if next_line is not None:  # Skips empty files
                heap.append((next_line, file))
        heapify(heap)
        
        to_write = None
        while heap:
            next_line, file = heappop(heap)
            if next_line is None: continue
            if to_write is not None and to_write != next_line:  # De-dup here
                output.write(to_write)
            to_write = next_line
            to_heap = self._get_next_line(file)
            if to_heap is not None:
                heappush(heap, (to_heap, file))
        if to_write is not None:
            output.write(to_write)  # Make sure the last line is written
        
        # Close all files
        for f in files:
            f.close()
        output.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This program sorts all lines in all files under a directory lexicographically.")
    parser.add_argument('-i', '--input_dir', help='Input directory.', required=True)
    parser.add_argument('-o', '--output_file', help='Output file', default='sorted.txt')
    
    args = parser.parse_args()
    ls = LineSort(base_dir=args.input_dir, output_file=args.output_file)
    ls.run()
