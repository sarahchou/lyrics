import unittest
class Discography:
    def __init__(self, songs):
        self.songs = songs
    def numSongs(self):
        return len(self.songs)
    def getSongs(self):
        return self.songs
    def getSongsInAlbum(self, album):
        album_songs = []
        for s in self.songs:
            if s.getAlbum() == album:
                album_songs.append(s)
        return album_songs

    def occursInAlbum(self, word, album):
        num = 0
        for song in self.getSongsInAlbum(album): #self
            num += song.occursInLyrics(word)
        print(word + " occurs in " + album + " " + str(num) + " times")
        return num
    def occursInDiscography(self, word):
        num = 0
        for s in self.songs:
            num += s.occursInLyrics(word)
        print(word + " occurs in discography " + str(num) + " times")
        return num

class Song:
    
    def __init__(self, title="", album="", track_num=0, lyrics=[]):
        self.title = title
        self.album = album
        self.track_num = track_num
        self.lyrics = lyrics

    def getTitle(self):
        return self.title
    def getAlbum(self):
        return self.album
    def getTrackNum(self):
        return self.track_num
    def getLyrics(self):
        return self.lyrics
    def occursInLyrics(self, word):
        counter = 0
        for w in self.lyrics:
            if word == w:
                counter += 1
        print(word + " occurs in " + self.getTitle() + " " + str(counter) + " times.")
        return counter
def readFile(fileName):
    fileObj = open(fileName, "r")
    lyrics = fileObj.read().split()
    fileObj.close()
    return lyrics

# class Test(unittest.TestCase):
#     wonderland = Song("Wonderland", "1989", 5, ["hi","there"])
#     def test_lyrics(self):
#         self.assertEqual("1989", wonderland.getAlbum())

if __name__ == "__main__":
    wonderland = Song("Wonderland", "1989", 5, readFile("wonderland_lyrics.txt"))
    new_romantics = Song("New Romantics", "1989", 2, readFile("new_romantics_lyrics.txt"))
    disc = Discography([wonderland, new_romantics])
    print(disc.numSongs()) #this should be true
    print(disc.occursInAlbum("my", "1989"))
    
    # Test.test_lyrics()
    print(wonderland.album)
    # print(wonderland.getLyrics())
    # print(new_romantics.lyrics)
    # print("wonderland occurs in " + wonderland.getTitle() + " " + str(wonderland.occursInLyrics("wonderland")) + " times")
    wonderland.occursInLyrics("wonderland")
    wonderland.occursInLyrics("a")
    new_romantics.occursInLyrics("a")



  