import webbrowser
class MovieTrailer():
    def __init__(self,movie_title,story_lines,movie_poster,movie_trailer):
        self.title=movie_title
        self.movie_story=story_lines
        self.poster_image_url=movie_poster
        self.trailer_youtube_url=movie_trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
