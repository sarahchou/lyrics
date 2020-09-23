import unittest, random
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

    def randomLyric(self):
        randomSong = random.choice(self.songs)
        fileObj = open(randomSong.getLyricFile(), "r")
        lyrics = fileObj.read().splitlines()
        fileObj.close()
        print("random song ", str(randomSong.getTitle()))
        return random.choice(lyrics)

class Song:
    
    def __init__(self, title="", album="", track_num=0, lyric_file = "", lyrics=[]):
        self.title = title
        self.album = album
        self.track_num = track_num
        self.lyric_file = lyric_file
        self.lyrics = lyrics

    def getTitle(self):
        return self.title
    def getAlbum(self):
        return self.album
    def getTrackNum(self):
        return self.track_num
    def getLyrics(self):
        return self.lyrics
    def getLyricFile(self):
        return self.lyric_file

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
    wonderland = Song("Wonderland", "1989", 5, "wonderland_lyrics.txt", readFile("wonderland_lyrics.txt"))
    new_romantics = Song("New Romantics", "1989", 2, "new_romantics_lyrics.txt", readFile("new_romantics_lyrics.txt"))
    wildest_dreams = Song("Wildest Dreams", "1989", 1, "wildest_dreams_lyrics.txt", readFile("wildest_dreams_lyrics.txt"))
    red = Song("Red", "Red", 1, "red_lyrics.txt", readFile("red_lyrics.txt"))
    disc = Discography([wonderland, new_romantics, wildest_dreams, red])
    print(disc.randomLyric())
    # print(disc.numSongs()) #this should be true
    print(disc.occursInDiscography("my"))
    
    # Test.test_lyrics()
    # print(wonderland.album)
    # print(wonderland.getLyrics())
    # print(new_romantics.lyrics)
    # print("wonderland occurs in " + wonderland.getTitle() + " " + str(wonderland.occursInLyrics("wonderland")) + " times")
    # wonderland.occursInLyrics("wonderland")
    # wonderland.occursInLyrics("a")
    # new_romantics.occursInLyrics("a")



  