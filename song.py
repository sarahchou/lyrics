import unittest, random
class Discography:
    def __init__(self, albums):
        self.albums = albums
    def addAlbum(self, a):
        self.albums.append(a)

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
        print("The word " + word.lower() + " occurs in discography a total of " + str(num) + " times")
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
        if song.getAlbumTitle() == self.title and song not in self.songs:
            self.songs.append(song)

class Song:
    
    def __init__(self, title="", album=None, track_num=0, lyric_file = ""):
        self.title = title
        self.album = album
        self.track_num = track_num
        self.lyric_file = lyric_file

    def getTitle(self):
        return self.title
    def getAlbum(self):
        return self.album
    def getAlbumTitle(self):
        return self.album.getTitle()
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
        if counter > 0:
            print(word + " occurs in " + self.getTitle() + " " + str(counter) + " times.")
        return counter

def readFile(fileName):
    fileObj = open(fileName, "r")
    lyrics = fileObj.read().split()
    fileObj.close()
    return lyrics

def init_songs():
    album_taylorswift = Album("Taylor Swift", [])
    album_fearless = Album("Fearless", [])
    album_speaknow = Album("Speak Now", [])
    album_red = Album("Red", [])
    album_1989 = Album("1989", [])
    album_reputation = Album("reputation", [])
    album_lover = Album("Lover", [])
    album_folklore = Album("folklore", [])
    # debut songs
    tim_mcgraw = Song("Tim McGraw", album_taylorswift, 1, "discography/taylorswift/tim_mcgraw_lyrics.txt")
    picture_to_burn = Song("Picture to Burn", album_taylorswift, 2, "discography/taylorswift/picture_to_burn_lyrics.txt")
    teardrops_on_my_guitar = Song("Teardrops on my Guitar", album_taylorswift, 3, "discography/taylorswift/teardrops_on_my_guitar_lyrics.txt")
    a_place_in_this_world = Song("A Place in this World", album_taylorswift, 4, "discography/taylorswift/a_place_in_this_world_lyrics.txt")
    cold_as_you = Song("Cold as You", album_taylorswift, 5, "discography/taylorswift/cold_as_you_lyrics.txt")
    the_outside = Song("The Outside", album_taylorswift, 6, "discography/taylorswift/the_outside_lyrics.txt")
    tied_together_with_a_smile = Song("Tied Together with a Smile", album_taylorswift, 7, "discography/taylorswift/tied_together_with_a_smile_lyrics.txt")
    stay_beautiful = Song("Stay Beautiful", album_taylorswift, 8, "discography/taylorswift/stay_beautiful_lyrics.txt")
    shouldve_said_no = Song("Should've Said No", album_taylorswift, 9, "discography/taylorswift/shouldve_said_no_lyrics.txt")
    marys_song = Song("Mary's Song (Oh My My My)", album_taylorswift, 10, "discography/taylorswift/marys_song_lyrics.txt")
    our_song = Song("Our Song", album_taylorswift, 11, "discography/taylorswift/our_song_lyrics.txt")
    im_only_me_when_im_with_you = Song("I'm Only Me When I'm With You", album_taylorswift, 12, "discography/taylorswift/im_only_me_when_im_with_you_lyrics.txt")
    invisible = Song("Invisible", album_taylorswift, 13, "discography/taylorswift/invisible_lyrics.txt")
    a_perfectly_good_heart = Song("A Perfectly Good Heart", album_taylorswift, 14, "discography/taylorswift/a_perfectly_good_heart_lyrics.txt")

    # speak now songs
    

    wonderland = Song("Wonderland", album_1989, 5, "discography/1989/wonderland_lyrics.txt")
    new_romantics = Song("New Romantics", album_1989, 2, "discography/1989/new_romantics_lyrics.txt")
    wildest_dreams = Song("Wildest Dreams", album_1989, 1, "discography/1989/wildest_dreams_lyrics.txt")
    red = Song("Red", album_red, 1, "discography/red/red_lyrics.txt")


    listofsongs = [wonderland, wildest_dreams, new_romantics, red, tim_mcgraw, picture_to_burn, teardrops_on_my_guitar,
    a_place_in_this_world, cold_as_you, the_outside, tied_together_with_a_smile, stay_beautiful, shouldve_said_no,
    marys_song, our_song, im_only_me_when_im_with_you, invisible, a_perfectly_good_heart]
    listofalbums = [album_taylorswift, album_fearless, album_speaknow, album_red, album_1989, album_reputation,
    album_lover, album_folklore]
    for s in listofsongs:
        for a in listofalbums:
            if s.getAlbum() == a:
                a.addSongToAlbum(s)
    disc = Discography([])
    for a in listofalbums: 
        disc.addAlbum(a)
    return disc


if __name__ == "__main__":
    disc = init_songs()
    print(disc.randomLyric())
    words = ["my", "and", "wonderland", "he", "wOndErlaNd", "rEd", "RED", "heart", "cold"]
    print(disc.occursInDiscography(random.choice(words)))
    print(str(disc.numSongs()), "num songs")



  