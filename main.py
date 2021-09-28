class song_machine:

    def init_songs():
        from song import Song
        from album import Album
        from discography import Discography
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
        jump_then_fall = Song("Jump Then Fall", album_fearless, 14, "discography/fearless/jump_then_fall_lyrics.txt")
        untouchable = Song("Untouchable", album_fearless, 15, "discography/fearless/untouchable_lyrics.txt")
        forever_and_always_piano = Song("Forever And Always (Piano Version)", album_fearless, 16, "discography/fearless/forever_and_always_lyrics.txt")
        come_in_with_the_rain = Song("Come In With The Rain", album_fearless, 17, "discography/fearless/come_in_with_the_rain_lyrics.txt")
        superstar = Song("Superstar", album_fearless, 18, "discography/fearless/superstar_lyrics.txt")
        the_other_side_of_the_door = Song("The Other Side of the Door", album_fearless, 19, "discography/fearless/the_other_side_of_the_door_lyrics.txt")
        today_was_a_fairytale = Song("Today Was a Fairytale", album_fearless, 20, "discography/fearless/today_was_a_fairytale_lyrics.txt")
        you_all_over_me = Song("You All Over Me", album_fearless, 21, "discography/fearless/you_all_over_me_lyrics.txt")
        mr_perfectly_fine = Song("Mr.Perfectly Fine", album_fearless, 22, "discography/fearless/mr_perfectly_fine_lyrics.txt")
        we_were_happy = Song("We Were Happy", album_fearless, 23, "discography/fearless/we_were_happy_lyrics.txt")
        thats_when = Song("That's When", album_fearless, 24, "discography/fearless/thats_when_lyrics.txt")
        dont_you = Song("Don't You", album_fearless, 25, "discography/fearless/dont_you_lyrics.txt")
        bye_bye_baby = Song("Bye Bye Baby", album_fearless, 26, "discography/fearless/bye_bye_baby_lyrics.txt")

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

        # 1989 songs
        welcome_to_new_york = Song("Welcome to New York", album_1989, 1, "discography/1989/welcome_to_new_york_lyrics.txt")
        blank_space = Song("Blank Space", album_1989, 2, "discography/1989/blank_space_lyrics.txt")
        style = Song("Style", album_1989, 3, "discography/1989/style_lyrics.txt")
        out_of_the_woods = Song("Out of the Woods", album_1989, 4, "discography/1989/out_of_the_woods_lyrics.txt")
        all_you_had_to_do_was_stay = Song("All You Had To Do Was Stay", album_1989, 5, "discography/1989/all_you_had_to_do_was_stay_lyrics.txt")
        shake_it_off = Song("Shake It Off", album_1989, 6, "discography/1989/shake_it_off_lyrics.txt")
        i_wish_you_would = Song("I Wish You Would", album_1989, 7, "discography/1989/i_wish_you_would_lyrics.txt")
        bad_blood = Song("Bad Blood", album_1989, 8, "discography/1989/bad_blood_lyrics.txt")
        wildest_dreams = Song("Wildest Dreams", album_1989, 9, "discography/1989/wildest_dreams_lyrics.txt")
        how_you_get_the_girl = Song("How You Get The Girl", album_1989, 10, "discography/1989/how_you_get_the_girl_lyrics.txt")
        this_love = Song("This Love", album_1989, 11, "discography/1989/this_love_lyrics.txt")
        i_know_places = Song("I Know Places", album_1989, 12, "discography/1989/i_know_places_lyrics.txt")
        clean = Song("Clean", album_1989, 13, "discography/1989/clean_lyrics.txt")
        wonderland = Song("Wonderland", album_1989, 14, "discography/1989/wonderland_lyrics.txt")
        you_are_in_love = Song("You Are In Love", album_1989, 15, "discography/1989/you_are_in_love_lyrics.txt")
        new_romantics = Song("New Romantics", album_1989, 16, "discography/1989/new_romantics_lyrics.txt")

        # reputation songs
        ready_for_it = Song("...Ready For It?", album_reputation, 1, "discography/reputation/ready_for_it_lyrics.txt")
        end_game = Song("End Game", album_reputation, 2, "discography/reputation/end_game_lyrics.txt")
        i_did_something_bad = Song("I Did Something Bad", album_reputation, 3, "discography/reputation/i_did_something_bad_lyrics.txt")
        dont_blame_me = Song("Don't Blame Me", album_reputation, 4, "discography/reputation/dont_blame_me_lyrics.txt")
        delicate = Song("Delicate", album_reputation, 5, "discography/reputation/delicate_lyrics.txt")
        look_what_you_made_me_do = Song("Look What You Made Me Do", album_reputation, 6,
        "discography/reputation/look_what_you_made_me_do_lyrics.txt")
        so_it_goes = Song("So It Goes...", album_reputation, 7, "discography/reputation/so_it_goes_lyrics.txt")
        gorgeous = Song("Gorgeous", album_reputation, 8, "discography/reputation/gorgeous_lyrics.txt")
        getaway_car = Song("Getaway Car", album_reputation, 9, "discography/reputation/getaway_car_lyrics.txt")
        king_of_my_heart = Song("King of my Heart", album_reputation, 10, "discography/reputation/king_of_my_heart_lyrics.txt")
        dancing_with_our_hands_tied = Song("Dancing With Our Hands Tied", album_reputation, 11,
        "discography/reputation/dancing_with_our_hands_tied_lyrics.txt")
        dress = Song("Dress", album_reputation, 12, "discography/reputation/dress_lyrics.txt")
        this_is_why_we_cant_have_nice_things = Song("This Is Why We Can't Have Nice Things", album_reputation, 13,
         "discography/reputation/this_is_why_we_cant_have_nice_things_lyrics.txt")
        call_it_what_you_want = Song("Call It What You Want", album_reputation, 14, "discography/reputation/call_it_what_you_want_lyrics.txt")
        new_years_day = Song("New Year's Day", album_reputation, 15, "discography/reputation/new_years_day_lyrics.txt")

        # lover songs
        i_forgot_that_you_existed = Song("I Forgot That You Existed", album_lover, 1, "discography/lover/i_forgot_that_you_existed_lyrics.txt")
        cruel_summer = Song("Cruel Summer", album_lover, 2, "discography/lover/cruel_summer_lyrics.txt")
        lover = Song("Lover", album_lover, 3, "discography/lover/lover_lyrics.txt")
        the_man = Song("The Man", album_lover, 4, "discography/lover/the_man_lyrics.txt")
        the_archer = Song("The Archer", album_lover, 5, "discography/lover/the_archer_lyrics.txt")
        i_think_he_knows = Song("I Think He Knows", album_lover, 6, "discography/lover/i_think_he_knows_lyrics.txt")
        miss_americana_and_the_heartbreak_prince = Song("Miss Americana & The Heartbreak Prince", album_lover,
        7, "discography/lover/miss_americana_and_the_heartbreak_prince_lyrics.txt")
        paper_rings = Song("Paper Rings", album_lover, 8, "discography/lover/paper_rings_lyrics.txt")
        cornelia_street = Song("Cornelia Street", album_lover, 9, "discography/lover/cornelia_street_lyrics.txt")
        death_by_a_thousand_cuts = Song("Death by a Thousand Cuts", album_lover, 10,
        "discography/lover/death_by_a_thousand_cuts_lyrics.txt")
        london_boy = Song("London Boy", album_lover, 11, "discography/lover/london_boy_lyrics.txt")
        soon_youll_get_better = Song("Soon You'll Get Better", album_lover, 12,
        "discography/lover/soon_youll_get_better_lyrics.txt")
        false_god = Song("False God", album_lover, 13, "discography/lover/false_god_lyrics.txt")
        you_need_to_calm_down = Song("You Need To Calm Down", album_lover, 14,
        "discography/lover/you_need_to_calm_down_lyrics.txt")
        afterglow = Song("Afterglow", album_lover, 15, "discography/lover/afterglow_lyrics.txt")
        me = Song("ME!", album_lover, 16, "discography/lover/me_lyrics.txt")
        its_nice_to_have_a_frend = Song("It's Nice To Have A Friend", album_lover,
        17, "discography/lover/its_nice_to_have_a_friend_lyrics.txt")
        daylight = Song("Daylight", album_lover, 18, "discography/lover/daylight_lyrics.txt")


        # folklore songs
        the_1 = Song("The 1", album_folklore, 1, "discography/folklore/the_1_lyrics.txt")
        cardigan = Song("cardigan", album_folklore, 2, "discography/folklore/cardigan_lyrics.txt")
        the_last_great_american_dynasty = Song("the last great american dynasty", album_folklore, 3,
        "discography/folklore/the_last_great_american_dynasty_lyrics.txt")
        exile = Song("exile", album_folklore, 4, "discography/folklore/exile_lyrics.txt")
        my_tears_ricochet = Song("my tears ricochet", album_folklore, 5, "discography/folklore/my_tears_ricochet_lyrics.txt")
        mirrorball = Song("mirrorball", album_folklore, 6, "discography/folklore/mirrorball_lyrics.txt")
        seven = Song("seven", album_folklore, 7, "discography/folklore/seven_lyrics.txt")
        august = Song("august", album_folklore, 8, "discography/folklore/august_lyrics.txt")
        this_is_me_trying = Song("this is my trying", album_folklore, 9, "discography/folklore/this_is_me_trying_lyrics.txt")
        illicit_affairs = Song("illicit affairs", album_folklore,  10, "discography/folklore/illicit_affairs_lyrics.txt")
        invisible_string = Song("invisible string", album_folklore, 11, "discography/folklore/invisible_string_lyrics.txt")
        mad_woman = Song("mad woman", album_folklore, 12, "discography/folklore/mad_woman_lyrics.txt")
        epiphany = Song("epiphany", album_folklore, 13, "discography/folklore/epiphany_lyrics.txt")
        betty = Song("betty", album_folklore, 14, "discography/folklore/betty_lyrics.txt")
        peace = Song("peace", album_folklore, 15, "discography/folklore/peace_lyrics.txt")
        hoax = Song("hoax", album_folklore, 16, "discography/folklore/hoax_lyrics.txt")
        the_lakes = Song("the lakes", album_folklore, 17, "discography/folklore/the_lakes_lyrics.txt")

        listofsongs = [tim_mcgraw, picture_to_burn, teardrops_on_my_guitar,
        a_place_in_this_world, cold_as_you, the_outside, tied_together_with_a_smile, stay_beautiful, shouldve_said_no,
        marys_song, our_song, im_only_me_when_im_with_you, invisible, a_perfectly_good_heart, mine, sparks_fly, back_to_december,
        speak_now, dear_john, mean, the_story_of_us, never_grow_up, enchanted, better_than_revenge, innocent,
        haunted, last_kiss, long_live, fearless, fifteen, love_story, hey_stephen, white_horse, you_belong_with_me, breathe,
        tell_me_why, youre_not_sorry, the_way_i_loved_you, forever_and_always, the_best_day, change, come_in_with_the_rain, jump_then_fall, superstar,
                       the_other_side_of_the_door, today_was_a_fairytale, untouchable, mr_perfectly_fine, dont_you, bye_bye_baby, thats_when, we_were_happy, you_all_over_me,
                       forever_and_always_piano,
        state_of_grace, red, treacherous, i_knew_you_were_trouble, all_too_well, _22, i_almost_do,
        we_are_never_ever_getting_back_together, stay_stay_stay, the_last_time, holy_ground, sad_beautiful_tragic,
        the_lucky_one, everything_has_changed, starlight, begin_again, the_moment_i_knew, come_back_be_here,
        girl_at_home,
        welcome_to_new_york, blank_space,style, out_of_the_woods, all_you_had_to_do_was_stay, shake_it_off,
        i_wish_you_would, bad_blood, how_you_get_the_girl, this_love, i_know_places,clean,you_are_in_love,
        wonderland, wildest_dreams, new_romantics,
        ready_for_it, end_game, i_did_something_bad, dont_blame_me, delicate, look_what_you_made_me_do,
        so_it_goes, gorgeous, getaway_car, king_of_my_heart, dancing_with_our_hands_tied, dress, this_is_why_we_cant_have_nice_things,
        call_it_what_you_want, new_years_day,
        i_forgot_that_you_existed, cruel_summer, lover, the_man, the_archer, i_think_he_knows, miss_americana_and_the_heartbreak_prince,
        paper_rings, cornelia_street, death_by_a_thousand_cuts, london_boy, soon_youll_get_better, false_god, you_need_to_calm_down,
        afterglow, me, its_nice_to_have_a_frend, daylight,
        the_1, cardigan, the_last_great_american_dynasty, exile, my_tears_ricochet, mirrorball, seven, august, this_is_me_trying,
        illicit_affairs, invisible_string, mad_woman, epiphany, betty, peace, hoax, the_lakes]

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
        words = ["cold", "lakes", "red", "peace", "woman", "girl"]
        # print(disc.occursInDiscography(random.choice(words)))
        # print(str(disc.numSongs()), "num songs")
        # tracks = []
        # for i in range(1, 20):
        #     tracks.append(i)
        # disc.allSongsTrackNum(random.choice(tracks))
        # disc.allSongsStartWith('b')
        # disc.allSongsTitleLength(1)
        # disc.allSongsTitleLength(5)
        # for i in range(1,18):
        #     disc.allSongsTrackNum(i)
        #disc.allSongsTrackNum(22)
        #disc.occursInDiscography("page")
        disc.wordInDiscography("happy")
        # for some reason does not include pages from DBATC because it is pages? so do some character matching with punctuation





