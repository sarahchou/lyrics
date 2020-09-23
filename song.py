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
    def randomLyricFromAlbum(self):        
        randomSong = random.choice(self.getSongs())
        fileObj = open(randomSong.getLyricFile(), "r")
        lyrics = fileObj.read().splitlines()
        fileObj.close()
        print("random song from ", self.getTitle(), " ", str(randomSong.getTitle()))
        return random.choice(lyrics)

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
    def randomLyricFromSong(self):
        fileObj = open(self.getLyricFile(), "r")
        lyrics = fileObj.read().splitlines()
        fileObj.close()
        print("random lyric from", self.getTitle())
        return random.choice(lyrics)

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

    #fearless songs
    fearless = Song("Fearless", album_fearless, 1, "discography/fearless/fearless_lyrics.txt")
    fifteen = Song("Fifteen", album_fearless, 2, "discography/fearless/fifteen_lyrics.txt")
    love_story = Song("Love Story", album_fearless, 3, "discography/fearless/love_story_lyrics.txt")
    hey_stephen = Song("Hey Stephen", album_fearless, 4, "discography/fearless/hey_stephen_lyrics.txt")
    white_horse = Song("White Horse", album_fearless, 5, "discography/fearless/white_horse_lyrics.txt")
    you_belong_with_me = Song("You Belong With Me", album_fearless, 6, "discography/fearless/you_belong_with_me_lyrics.txt")
    breathe = Song("Breathe", album_fearless, 7, "discography/fearless/breathe_lyrics.txt")
    tell_me_why = Song("Tell Me Why", album_fearless, 8, "discography/fearless/tell_me_why_lyrics.txt")
    youre_not_sorry = Song("You're Not Sorry", album_fearless, 9, "discography/fearless/youre_not_sorry_lyrics.txt")
    the_way_i_loved_you = Song("The Way I Loved You", album_fearless, 10, "discography/fearless/the_way_i_loved_you_lyrics.txt")
    forever_and_always = Song("Forever & Always", album_fearless,11, "discography/fearless/forever_and_always_lyrics.txt")
    the_best_day = Song("The Best Day", album_fearless, 12, "discography/fearless/the_best_day_lyrics.txt")
    change = Song("Change", album_fearless, 13, "discography/fearless/change_lyrics.txt")

    # speak now songs
    mine = Song("Mine", album_speaknow, 1, "discography/speaknow/mine_lyrics.txt")
    sparks_fly = Song("Sparks Fly", album_speaknow, 2, "discography/speaknow/sparks_fly_lyrics.txt")
    back_to_december = Song("Back to December", album_speaknow, 3, "discography/speaknow/back_to_december_lyrics.txt")
    speak_now = Song("Speak Now", album_speaknow, 4, "discography/speaknow/speak_now_lyrics.txt")
    dear_john = Song("Dear John", album_speaknow, 5, "discography/speaknow/dear_john_lyrics.txt")
    mean = Song("Mean", album_speaknow,6, "discography/speaknow/mean_lyrics.txt")
    the_story_of_us = Song("The Story of Us", album_speaknow, 7, "discography/speaknow/the_story_of_us_lyrics.txt")
    never_grow_up = Song("Never Grow Up", album_speaknow, 8, "discography/speaknow/never_grow_up_lyrics.txt")
    enchanted = Song("Enchanted", album_speaknow, 9, "discography/speaknow/enchanted_lyrics.txt")
    better_than_revenge = Song("Better Than Revenge", album_speaknow, 10, "discography/speaknow/better_than_revenge_lyrics.txt")
    innocent = Song("Innocent", album_speaknow, 11, "discography/speaknow/innocent_lyrics.txt")
    haunted = Song("Haunted", album_speaknow,12, "discography/speaknow/haunted_lyrics.txt")
    last_kiss = Song("Last Kiss", album_speaknow, 13, "discography/speaknow/last_kiss_lyrics.txt")
    long_live = Song("Long Live", album_speaknow, 14, "discography/speaknow/long_live_lyrics.txt")

    # red songs
    state_of_grace = Song("State of Grace", album_red, 1, "discography/red/state_of_grace_lyrics.txt")
    red = Song("Red", album_red, 2, "discography/red/red_lyrics.txt")
    treacherous = Song("Treacherous", album_red, 3, "discography/red/treacherous_lyrics.txt")
    i_knew_you_were_trouble = Song("I Knew You Were Trouble", album_red, 4, "discography/red/i_knew_you_were_trouble_lyrics.txt")
    all_too_well = Song("All Too Well", album_red, 5, "discography/red/all_too_well_lyrics.txt")
    _22 = Song("22", album_red, 6, "discography/red/22_lyrics.txt")
    i_almost_do = Song("I Almost Do", album_red, 7, "discography/red/i_almost_do_lyrics.txt")
    we_are_never_ever_getting_back_together = Song("We Are Never Ever Getting Back Together", album_red, 8, 
    "discography/red/we_are_never_ever_getting_back_together_lyrics.txt")
    stay_stay_stay = Song("Stay Stay Stay", album_red, 9, "discography/red/stay_stay_stay_lyrics.txt")
    the_last_time = Song("The Last Time", album_red, 10, "discography/red/the_last_time_lyrics.txt")
    holy_ground = Song("Holy Ground", album_red, 11, "discography/red/holy_ground_lyrics.txt")
    sad_beautiful_tragic = Song("Sad Beautiful Tragic", album_red, 12, "discography/red/sad_beautiful_tragic_lyrics.txt")
    the_lucky_one = Song("The Lucky One", album_red, 13, "discography/red/the_lucky_one_lyrics.txt")
    everything_has_changed = Song("Everything Has Changed", album_red, 14, "discography/red/everything_has_changed_lyrics.txt")
    starlight = Song("Starlight", album_red, 15, "discography/red/starlight_lyrics.txt")
    begin_again = Song("Begin Again", album_red, 16, "discography/red/begin_again_lyrics.txt")
    the_moment_i_knew = Song("The Moment I Knew", album_red, 17, "discography/red/the_moment_i_knew_lyrics.txt")
    come_back_be_here = Song("Come Back...Be Here", album_red, 18, "discography/red/come_back_be_here_lyrics.txt")
    girl_at_home = Song("Girl At Home", album_red, 19, "discography/red/girl_at_home_lyrics.txt")










    wonderland = Song("Wonderland", album_1989, 5, "discography/1989/wonderland_lyrics.txt")
    new_romantics = Song("New Romantics", album_1989, 2, "discography/1989/new_romantics_lyrics.txt")
    wildest_dreams = Song("Wildest Dreams", album_1989, 1, "discography/1989/wildest_dreams_lyrics.txt")


    listofsongs = [wonderland, wildest_dreams, new_romantics, red, tim_mcgraw, picture_to_burn, teardrops_on_my_guitar,
    a_place_in_this_world, cold_as_you, the_outside, tied_together_with_a_smile, stay_beautiful, shouldve_said_no,
    marys_song, our_song, im_only_me_when_im_with_you, invisible, a_perfectly_good_heart, mine, sparks_fly, back_to_december,
    speak_now, dear_john, mean, the_story_of_us, never_grow_up, enchanted, better_than_revenge, innocent,
    haunted, last_kiss, long_live, fearless, fifteen, love_story, hey_stephen, white_horse, you_belong_with_me, breathe,
    tell_me_why, youre_not_sorry, the_way_i_loved_you, forever_and_always, the_best_day, change]
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




  