import random
class Song:
    # A Song has a title, album, track number, and lyric file
    def __init__(self, title="", album=None, track_num=0, lyric_file = ""):
        self.title = title
        self.album = album
        self.track_num = track_num
        self.lyric_file = lyric_file

    def readFile(self, fileName):
        fileObj = open(fileName, "r")
        lyrics = fileObj.read().split()
        fileObj.close()
        return lyrics

    # Return the title of the song
    def getTitle(self):
        return self.title

    # What album does this song belong in?
    def getAlbum(self):
        return self.album

    # Return the album title
    def getAlbumTitle(self):
        return self.album.getTitle()

    # Return the track number of the song
    def getTrackNum(self):
        return self.track_num

    # Return all of the lyrics of this song
    def getLyrics(self):
        return self.readFile(self.lyric_file)

    # Get the lyric file of the song
    def getLyricFile(self):
        return self.lyric_file

    # How many times does the given word occur in this song
    def occurencesInLyrics(self, word):
        counter = 0
        for w in self.getLyrics():
            if word.lower() == w.lower():
                counter += 1
        if counter > 0:
            print(word + " occurs in " + self.getTitle() + " " + str(counter) + " times.")
        return counter

    # does the word occur in the song?
    def occursInLyrics(self, word):
        for w in self.getLyrics():
            if word.lower() == w.lower():
                return True
        return False

    # Return a random lyric from this song
    def randomLyricFromSong(self):
        fileObj = open(self.getLyricFile(), "r")
        lyrics = fileObj.read().splitlines()
        fileObj.close()
        print("random lyric from: ", self.getTitle())
        return random.choice(lyrics)

    def wordInLyric(self, word, lyric):
        for w in lyric.split(" "):
            if word.lower() == w.lower():
                return True
        return False

    # If the given word is in the song, return a list of all of the lyrics that the word occurs in
    def wordInSong(self, word):
        fileObj = open(self.getLyricFile(), "r")
        lyrics = fileObj.read().splitlines()
        fileObj.close()
        listOfLyrics = []
        for l in lyrics:
            if self.wordInLyric(word, l):
                listOfLyrics.append(l)
        return listOfLyrics

    # Does this song start with the given letter?
    def songStartsWith(self, letter):
        return self.getTitle()[0].lower() == letter.lower()

    # How many letters is this song title?
    def titleLength(self):
        return len(self.getTitle().split(" "))
