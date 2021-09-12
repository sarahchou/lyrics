import song, random

class Album:
    def __init__(self, title, songs):
        self.title = title
        self.songs = songs
    def getTitle(self):
        return self.title

    # How many songs are in this album?
    def numSongs(self):
        return len(self.songs)

    # What songs are in this album?
    def getSongs(self):
        return self.songs

    # How many times does the given word occur in this album?
    def occurencesInAlbum(self, word):
        num = 0
        for song in self.getSongs():
            num += song.occurencesInLyrics(word)
        print(word + " occurs in " + self.title + " " + str(num) + " times")
        return num

    # Does the word occur in the album?
    def occursInAlbum(self, word):
        for song in self.getSongs():
            if song.occursInLyrics(word):
                return True
        return False

    # Add the song to this album's list of songs if it is not already there and belongs in this album
    def addSongToAlbum(self, song):
        if song.getAlbumTitle() == self.title and song not in self.songs:
            self.songs.append(song)

    # Return a random lyric from this album? or is it a random song? printing and returning something different
    def randomSongFromAlbum(self):
        randomSong = random.choice(self.getSongs())
        fileObj = open(randomSong.getLyricFile(), "r")
        lyrics = fileObj.read().splitlines()
        fileObj.close()
        print("Random lyric from ", self.getTitle(), " ", str(randomSong.getTitle()))
        return random.choice(lyrics)
