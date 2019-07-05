import unittest
import os

from filelibrary import AudioFile

TEST_DIR_PATH = os.path.dirname(__file__) + '/../tests/test'
TEST_FLAC_FILE = TEST_DIR_PATH + '/audio_files/example.flac'
TEST_MP3_FILE = TEST_DIR_PATH + '/audio_files/example.mp3'
TEST_NON_AUDIO_FILE = TEST_DIR_PATH + '/test.txt'

test_flac = AudioFile(TEST_FLAC_FILE)
test_mp3 = AudioFile(TEST_MP3_FILE)
test_txt = AudioFile(TEST_NON_AUDIO_FILE)


class AudioFile(unittest.TestCase):

    def test_mp3_file_variables(self):
        self.assertEqual(test_mp3.disc_number, '1')
        self.assertEqual(test_mp3.album, 'Album')
        self.assertEqual(test_mp3.genre, 'Jazz')
        self.assertEqual(test_mp3.track_number, '1')
        self.assertEqual(test_mp3.artist, 'Artist')
        self.assertEqual(test_mp3.album_artist, 'AlbumArtist')
        self.assertEqual(test_mp3.title, 'Title')
        self.assertEqual(test_mp3.composer, 'Composer')

    def test_flac_file_variables(self):
        self.assertEqual(test_flac.disc_number, '1')
        self.assertEqual(test_flac.album, 'Album')
        self.assertEqual(test_flac.genre, 'Jazz')
        self.assertEqual(test_flac.track_number, '1')
        self.assertEqual(test_flac.artist, 'Artist')
        self.assertEqual(test_flac.album_artist, 'AlbumArtist')
        self.assertEqual(test_flac.title, 'Title')
        self.assertEqual(test_flac.composer, 'Composer')

    def test_non_audio_file(self):
        self.assertIsNone(test_txt.disc_number)
        self.assertIsNone(test_txt.album)
        self.assertIsNone(test_txt.genre)
        self.assertIsNone(test_txt.track_number)
        self.assertIsNone(test_txt.artist)
        self.assertIsNone(test_txt.album_artist)
        self.assertIsNone(test_txt.title)
        self.assertIsNone(test_txt.composer)
