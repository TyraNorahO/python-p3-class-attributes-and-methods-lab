class Song:
    count = 0
    genres = [] #empty list/array
    artists = []
    genre_count = {} #empty bject
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
# ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
# print(ninety_nine_problems.name)
# print(ninety_nine_problems.artist)
# print(ninety_nine_problems.genre)
       
        Song.count += 1  # Incrases count when a new song is created
        #  if statements Adds the logged data to the list if it's unique
        if genre not in Song.genres:
            Song.genres.append(genre)
       
        if artist not in Song.artists:
            Song.artists.append(artist)
       
       #updating the counts
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1  
      
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1

    @classmethod #using a decorator so as to not repeat attributes
    def add_song_to_count(cls):
        cls.count += 1
    #the if statements are made so repetition cannot be made
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1