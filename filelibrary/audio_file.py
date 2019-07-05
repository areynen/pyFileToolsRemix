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
        self.disc_number = self.date = self.album = self.genre = self.track_number = self.artist = self.album_artist =\
            self.title = self.composer = None

        if str.lower(self.extension) == 'flac':
            self.tag_flac()

        if str.lower(self.extension) == 'mp3':
            self.tag_mp3()

    def __str__(self):
        return super().__str__() +\
               f'Disc Number = {self.disc_number}\n' +\
               f'Album = {self.album}\n' +\
               f'Genre = {self.genre}\n' +\
               f'Track Number = {self.track_number}\n' +\
               f'Artist = {self.artist}\n' +\
               f'Album Artist = {self.album_artist}\n' +\
               f'Title = {self.title}\n' +\
               f'Composer = {self.composer}\n'

    def tag_flac(self):
        meta_data = FLAC(self.path)
        self.disc_number = meta_data['discnumber'][0]
        self.date = meta_data['date'][0]
        self.album = meta_data['album'][0]
        self.genre = meta_data['genre'][0]
        self.track_number = meta_data['tracknumber'][0]
        self.artist = meta_data['artist'][0]
        self.album_artist = meta_data['albumartist'][0]
        self.title = meta_data['title'][0]
        self.composer = meta_data['composer'][0]

    def tag_mp3(self):
        meta_data = MP3(self.path)
        self.disc_number = meta_data['TPOS']
        self.date = meta_data['TDRC']
        self.album = meta_data['TALB']
        self.genre = meta_data['TCON']
        self.track_number = meta_data['TRCK']
        self.artist = meta_data['TPE1']
        self.album_artist = meta_data['TPE2']
        self.title = meta_data['TIT2']
        self.composer = meta_data['TCOM']


if __name__ == '__main__':
    flac_file = AudioFile(os.path.dirname(__file__) + '/../tests/test/audio_files/example.flac')
    print(flac_file)

    mp3_file = AudioFile(os.path.dirname(__file__) + '/../tests/test/audio_files/example.mp3')
    print(mp3_file)
