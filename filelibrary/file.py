# file.py
# Purpose: to provide a class for files. a parent to future specified file types
# Author: Alex Reynen

import os

from filelibrary import Directory


class File(Directory):

    def __init__(self, dir):
        super().__init__(dir)
        self.extension = dir.split('.')[-1]
        self.file_name = dir.split('.')[-2].split('/')[-1]

    def __str__(self):
        return super().__str__() + f'\nFile is named: {self.file_name}\n' + f'Extension = {self.extension}'


if __name__ == '__main__':
    file = File(os.path.dirname(__file__) + '/../tests/test/test.txt')
    print(file)
