# audio_file.py
# Purpose: to provide a parent class for Audio files, such as mp3 and flac files
# Author: Alex Reynen

import os
from mutagen.flac import FLAC
from mutagen.mp3 import MP3

from filelibrary import File


class AudioFile(File):

    def __init__(self, dir):
        super().__init__(dir)

        if str.lower(self.extension) == 'flac':
            self.tag_flac()

        if str.lower(self.extension) == 'mp3':
            self.tag_mp3()

    def tag_flac(self):
        meta_data = FLAC(self.path)
        for key in meta_data.keys():
            print(f'{key} = {meta_data[key][0]}')

    def tag_mp3(self):
        meta_data = MP3(self.path)
        for key in meta_data.keys():
            print(f'{key} = {meta_data[key]}')


if __name__ == '__main__':
    flac_file = AudioFile(os.path.dirname(__file__) + '/../tests/test/audio_files/example.flac')
    print(flac_file)

    mp3_file = AudioFile(os.path.dirname(__file__) + '/../tests/test/audio_files/example.mp3')
    print(mp3_file)
