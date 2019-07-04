import unittest
import os

from filelibrary import Directory

TEST_DIR_PATH = os.path.dirname(__file__) + '/../tests/test'
TEST_TXT_FILE = TEST_DIR_PATH + '/test.txt'

test_dir = Directory(TEST_DIR_PATH)
test_file = Directory(TEST_TXT_FILE)


class DirectoryTest(unittest.TestCase):

    def test_class_variables_real_dir(self):
        self.assertEqual(test_dir.path, TEST_DIR_PATH)
        self.assertEqual(test_dir.name, 'test')

    def test_class_variables_file(self):
        self.assertIsNone(test_file.path)
        self.assertIsNone(test_file.name)
