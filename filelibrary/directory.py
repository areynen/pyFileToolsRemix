# directory.py
# Purpose: to provide a class for directories
# Author: Alex Reynen

import os


class Directory:

    def __init__(self, dir):
        self.name = str.split(dir, '/')[-1]
        self.path = dir

    def __str__(self):
        return f'Located at path: {self.path}\n' + f'It is named: {self.name}'


if __name__ == '__main__':
    bb = Directory(os.path.dirname(__file__) + '/../tests/test')
    print(bb)
