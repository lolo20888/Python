import webbrowser
class Video():

    """Contain The Duration"""
    def __init__(self,Title,Duration):
        self.Title = Title
        self.Duration = Duration
class Movie(Video):

    """ THIS IS A DOC"""
    def __init__(self,Title, movie_storyline , movie_poster_image_url , movie_trailer_youtube_url,Duration):
        Video.__init__(self,Title,Duration)
        self.storyline= movie_storyline
        self.poster_image_url = movie_poster_image_url
        self.trailer_youtube_url = movie_trailer_youtube_url
        
        
class TvShow(Video):

    """Contains All Of The TV Shows"""
    def __init__(self,Title,Image,Season,Eposode,Tv_Station,Duration):
        Video.__init__(self,Title,Duration)
        self.image = Image
        self.Season = Season
        self.Eposode = Eposode
        self.Tv_Station = Tv_Station
        



x = TvShow("mina",'http://image.tmdb.org/t/p/w500/dE5s2yagw4CNOSznMwn0LMBmPbx.jpg','10','1',"CBC","10 min")

print x.Duration