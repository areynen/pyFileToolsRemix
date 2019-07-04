# file.py
# Purpose: to provide a class for files. a parent to future specified file types
# Author: Alex Reynen

import os

from filelibrary import Directory


class File(Directory):

    def __init__(self, dir):
        super().__init__(dir)
        if os.path.isfile(dir):
            self.name = str.split(dir, '/')[-1]
            self.path = dir
            self.extension = dir.split('.')[-1]
            self.file_name = dir.split('.')[-2].split('/')[-1]

        else:
            self.name = None
            self.path = None
            self.extension = None
            self.file_name = None

    def __str__(self):
        return f'Located at path: {self.path}\n' + \
               f'It is named: {self.name}\n' + \
               f'File is named: {self.file_name}\n' + \
               f'Extension = {self.extension}\n'


if __name__ == '__main__':
    file = File(os.path.dirname(__file__) + '/../tests/test/test.txt')
    print(file)

    dir = File(os.path.dirname(__file__) + '/../tests/test')
    print(dir)
