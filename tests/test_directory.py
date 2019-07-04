import unittest
import os

from filelibrary import Directory

TEST_DIR_PATH = os.path.dirname(__file__) + '/../tests/test'

test_dir = Directory(TEST_DIR_PATH)


class DirectoryTest(unittest.TestCase):

    def test_is_directory(self):
        self.assertTrue(TEST_DIR_PATH)

    def test_class_variables(self):
        self.assertEqual(test_dir.path, TEST_DIR_PATH)
