# directory.py
# Purpose: to provide a class for directories
# Author: Alex Reynen

import os


class Directory:

    def __init__(self, dir):
        if self.is_dir(dir):
            self.name = str.split(dir, '/')[-1]
            self.path = dir
        else:
            self.name = None
            self.path = None

    def __str__(self):
        return f'Located at path: {self.path}\n' + f'It is named: {self.name}'

    # Returns True if it is a directory, False if it is not
    def is_dir(self, dir):
        return True if os.path.isdir(dir) else False


if __name__ == '__main__':
    bb = Directory(os.path.dirname(__file__) + '/../tests/test')
    print(bb)

    aa = Directory(os.path.dirname(__file__) + '/../tests/test.test.txt')
    print(aa)
