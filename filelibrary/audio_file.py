# audio_file.py
# Purpose: to provide a parent class for Audio files, such as mp3 and flac files
# Author: Alex Reynen

import os

from filelibrary import File


class AudioFile(File):

    def __init__(self, dir):
        super().__init__(dir)

        if str.lower(self.extension) == 'flac':
            print('is flac')

        if str.lower(self.extension) == 'mp3':
            print('is mp3')


if __name__ == '__main__':
    flac_file = AudioFile(os.path.dirname(__file__) + '/../tests/test/audio_files/example.flac')
    print (flac_file)

    mp3_file = AudioFile(os.path.dirname(__file__) + '/../tests/test/audio_files/example.mp3')
    print(mp3_file)
