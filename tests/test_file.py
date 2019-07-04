import unittest
import os

from filelibrary import File

TEST_DIR_PATH = os.path.dirname(__file__) + '/../tests/test'
TEST_TXT_FILE = TEST_DIR_PATH + '/test.txt'

test_file = File(TEST_TXT_FILE)
test_dir = File(TEST_DIR_PATH)


class DirectoryTest(unittest.TestCase):

    def test_class_variables_real_file(self):
        self.assertEqual(test_file.path, TEST_TXT_FILE)
        self.assertEqual(test_file.name, 'test.txt')
        self.assertEqual(test_file.extension, 'txt')
        self.assertEqual(test_file.file_name, 'test')

    def test_class_variables_dir(self):
        self.assertIsNone(test_dir.path)
        self.assertIsNone(test_dir.name)
        self.assertIsNone(test_dir.extension)
        self.assertIsNone(test_dir.file_name)
