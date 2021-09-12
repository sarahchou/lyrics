import unittest, random, album

class Discography:
    def __init__(self, albums):
        self.albums = albums

    # Add albums
    def addAlbum(self, a):
        self.albums.append(a)

    # return the number of songs
    def numSongs(self):
        c = 0
        for a in self.albums:
            c += len(a.getSongs())
        return c

    # Return all of the songs
    def getSongs(self):
        arr = []
        for a in self.albums:
            for s in a.getSongs():
                arr.append(s)
        return arr

    # Return all of the songs in the given album
    def getSongsInAlbum(self, album):
        album_songs = []
        for a in self.albums:
            if a == album:
                album_songs.append(a.getSongs())
        return album_songs

    # how many times does the given word occur in the given album?
    def occursInAlbum(self, word, album):
        num = 0
        for song in self.getSongsInAlbum(album):
            num += song.occurencesInLyrics(word)
        print(word + " occurs in " + album + " " + str(num) + " times")
        return num

    # how many times does the given word occur in Taylor Swift's discography?
    def occurencesInDiscography(self, word):
        num = 0
        for s in self.getSongs():
            num += s.occurencesInLyrics(word)
        print("The word " + word.lower() + " occurs in discography a total of " + str(num) + " times")
        return num

    def occursInDiscography(self, word):
        print("Songs that have the word " + word + ":")
        songsWithWord = []
        for s in self.getSongs():
            if s.occursInLyrics(word):
                songsWithWord.append(s.getTitle)
                print(s.getTitle())
        return songsWithWord

    # If the word is present in the discography, return the list of song titles and lyrics that the word occurs in
    def wordInDiscography(self, word):
        print("word is: " + word)
        lyricsWithWord = {}
        for s in self.getSongs():
            if s.occursInLyrics(word):
                lyricsWithWord[s.getTitle()] = s.wordInSong(word)
        for l, v in lyricsWithWord.items():
            print(l + ": " + str(v))
        return lyricsWithWord


    # Generate a random lyric and tell us what song and album it is from
    def randomLyric(self):
        randomSong = random.choice(self.getSongs())
        fileObj = open(randomSong.getLyricFile(), "r")
        lyrics = fileObj.read().splitlines()
        fileObj.close()
        print("A random lyric was chosen from the song", str(randomSong.getTitle()), "from the album", randomSong.getAlbumTitle() + ":")
        return random.choice(lyrics)

    # Print all of the songs with the given track number
    def allSongsTrackNum(self, track_num):
        allTracks = []
        for s in self.getSongs():
            if s.getTrackNum() == track_num:
                allTracks.append(s)
                print(s.getTitle(), "is track", track_num, "from ", s.getAlbumTitle())
        if len(allTracks) == 0:
            print("There are no albums with", track_num, "songs")
        return allTracks

    # Return all of the songs that start with the given letter
    def allSongsStartWith(self, letter):
        allSongs = []
        for s in self.getSongs():
            if s.songStartsWith(letter):
                allSongs.append(s)
                print(s.getTitle(), "starts with", letter)
        return allSongs

    # Return all of the songs that the title is the length of the given number
    def allSongsTitleLength(self, num):
        allSongs = []
        for s in self.getSongs():
            if s.titleLength() == num:
                allSongs.append(s)
                print(s.getTitle(), "has", num, "words")
        return allSongs

