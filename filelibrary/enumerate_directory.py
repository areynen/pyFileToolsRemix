# enumerate_directory.py
# Purpose: to obtain files within a directory recursively
# Author: Alex Reynen

import os

TESTING_DIRECTORY = os.path.dirname(__file__) + '/../tests/test'


def main():
    print(os.path.isdir(TESTING_DIRECTORY))


if __name__ == '__main__':
    main()
