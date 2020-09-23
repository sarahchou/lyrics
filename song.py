import unittest, random
class Discography:
    def __init__(self, albums):
        self.albums = albums
    def numSongs(self):
        c = 0
        for a in self.albums:
            c += len(a.getSongs())
        return c
    def getSongs(self):
        arr = []
        for a in self.albums:
            for s in a.getSongs():
                arr.append(s)
        return arr
    def getSongsInAlbum(self, album):
        album_songs = []
        for a in self.albums:
            if a == album:
                album_songs.append(a.getSongs())
        return album_songs

    def occursInAlbum(self, word, album):
        num = 0
        for song in self.getSongsInAlbum(album):
            num += song.occursInLyrics(word)
        print(word + " occurs in " + album + " " + str(num) + " times")
        return num
    def occursInDiscography(self, word):
        num = 0
        for s in self.getSongs():
            num += s.occursInLyrics(word)
        print(word + " occurs in discography " + str(num) + " times")
        return num

    def randomLyric(self):
        randomSong = random.choice(self.getSongs())
        print("rando song title", randomSong.getTitle())
        fileObj = open(randomSong.getLyricFile(), "r")
        lyrics = fileObj.read().splitlines()
        fileObj.close()
        print("random song ", str(randomSong.getTitle()))
        return random.choice(lyrics)

class Album:
    def __init__(self, title, songs):
        self.title = title
        self.songs = songs
    def getTitle(self):
        return self.title
    def numSongs(self):
        return len(self.songs)

    def getSongs(self):
        return self.songs

    def occursInAlbum(self, word):
        num = 0
        for song in self.getSongs():
            num += song.occursInLyrics(word)
        print(word + " occurs in " + self.title + " " + str(num) + " times")
        return num
    def addSongToAlbum(self, song):
        if song.getAlbum() == self.title and song not in self.songs:
            self.songs.append(song)

class Song:
    
    def __init__(self, title="", album="", track_num=0, lyric_file = ""):
        self.title = title
        self.album = album
        self.track_num = track_num
        self.lyric_file = lyric_file

    def getTitle(self):
        return self.title
    def getAlbum(self):
        return self.album
    def getTrackNum(self):
        return self.track_num
    def getLyrics(self):
        return readFile(self.lyric_file)
    def getLyricFile(self):
        return self.lyric_file

    def occursInLyrics(self, word):
        counter = 0
        for w in self.getLyrics():
            if word.lower() == w.lower():
                counter += 1
        print(word + " occurs in " + self.getTitle() + " " + str(counter) + " times.")
        return counter
def readFile(fileName):
    fileObj = open(fileName, "r")
    lyrics = fileObj.read().split()
    fileObj.close()
    return lyrics

def init_songs():
    wonderland = Song("Wonderland", "1989", 5, "wonderland_lyrics.txt")
    new_romantics = Song("New Romantics", "1989", 2, "new_romantics_lyrics.txt")
    wildest_dreams = Song("Wildest Dreams", "1989", 1, "wildest_dreams_lyrics.txt")
    red = Song("Red", "Red", 1, "red_lyrics.txt")


    album_red = Album("Red", [])
    album_1989 = Album("1989", [])


    listofsongs = [wonderland, wildest_dreams, new_romantics, red]
    listofalbums = [album_1989, album_red]
    for s in listofsongs:
        for a in listofalbums:
            a.addSongToAlbum(s)
    disc = Discography([album_1989, album_red])
    return disc


if __name__ == "__main__":
    disc = init_songs()
    print(disc.randomLyric())
    words = ["my", "and", "wonderland", "he", "wOndErlaNd", "rEd", "RED"]
    print(disc.occursInDiscography(random.choice(words)))
    print(str(disc.numSongs()), "num songs")



  