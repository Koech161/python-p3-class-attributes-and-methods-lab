class Song:
    all = []
    count = 0
    genres = set()  
    artists = set()  
    genre_count = {}  
    artist_count = {}
    def __init__(self,name ,artist,genre):
        self.name =name
        self.artist =artist
        self.genre = genre
        Song.all.append(self)
        Song.count +=1 

        Song.genres.add(genre)
        Song.artists.add(artist)
        
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1
        
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1

    @classmethod
    def get_total_count(cls):
        return cls.count

    @classmethod
    def get_all_songs(cls):
        return cls.all

    @classmethod
    def get_genres(cls):
        return cls.genres

    @classmethod
    def get_artists(cls):
        return cls.artists

    @classmethod
    def get_genre_count(cls):
        return cls.genre_count

    @classmethod
    def get_artist_count(cls):
        return cls.artist_count
    
    # def add_song_to_count(self):
    #      self.count += 1

# class Circle():
#     pi = 3.14159
#     def __init__(self,radius):
#         self.radius =radius
#     def area(self):
#         return Circle.pi * self.radius  * self.radius
    
# c = Circle(7)    
# print(c.area())

# class Myclass:
#     limit = 10
#     def __init__(self):
#         self.data = []
#     def item(self, i):
#         return self.data[i]  
#     def add(self, e):
#         if(self.data ) >= self.limit:
#             raise Exception('To many items')
#         self.data.append(e)
# print(Myclass.limit)  
# foo = Myclass()
# foo.limit = 50    
# print(foo.limit)  

# class Person:
#     all_names =[]
#     def __init__(self,name):
#         self.name =name
#         Person.all_names.append(self)
#     @classmethod
#     def print_names(cls,name):
#         cls.all_names.append(name)
#     @classmethod
#     def show_names(cls):
#         print([name.name for name in cls.all_names ])    
      
# abel = Person('Abel')  
# joe = Person('Joe')      
# Person.show_names()