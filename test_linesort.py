import os
import tempfile
import unittest

from linesort import LineSort

_FILE1 = """
apple
apple

banana
banana
banana

cactus




"""
_FILE2 = """


a
a
apple banana

dinosaur
dinosaurs

  frankfurter
frankfurter
frankfurter
frankfurter
frankfurter
frankfurter
frankfurter
frankfurter
frankfurter



"""

_FILE3 = """



"""

class TestLineSort(unittest.TestCase):
    def test_single_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            with open(os.path.join(temp_dir, "file1.txt"), "w") as f1:
                f1.write(_FILE1)
            output_file = os.path.join(temp_dir, "sorted.txt")
            ls = LineSort(base_dir=temp_dir, output_file=output_file)
            ls.run()
            with open(output_file) as f:
                lines = f.readlines()
                self.assertEqual(lines, ['apple\n', 'banana\n', 'cactus\n'])

    def test_empty_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            with open(os.path.join(temp_dir, "file3.txt"), "w") as f1:
                f1.write(_FILE3)
            output_file = os.path.join(temp_dir, "sorted.txt")
            ls = LineSort(base_dir=temp_dir, output_file=output_file)
            ls.run()
            with open(output_file) as f:
                lines = f.readlines()
                self.assertFalse(lines)  # Empty file is ignored

    def test_all_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            for i, file in enumerate((_FILE1, _FILE2, _FILE3)):
                with open(os.path.join(temp_dir, f"file{i}.txt"), "w") as f:
                    f.write(file)
            output_file = os.path.join(temp_dir, "sorted.txt")
            ls = LineSort(base_dir=temp_dir, output_file=output_file)
            ls.run()
            expected = ['a\n', 'apple\n', 'apple banana\n', 'banana\n', 'cactus\n',
                        'dinosaur\n', 'dinosaurs\n', '  frankfurter\n', 'frankfurter\n']
            with open(output_file) as f:
                lines = f.readlines()
                self.assertEqual(lines, expected)


if __name__ == "__main__":
    unittest.main()