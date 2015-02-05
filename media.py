import webbrowser

class Movie():
	""" This class provides a way to store information about movies """

	def __init__(self, movie_title, movie_release_date, movie_storyline, movie_poster_image_url, movie_trailer_youtube_url):
		self.title = movie_title
		self.release_date = movie_release_date
		self.storyline = movie_storyline
		self.poster_image_url = movie_poster_image_url
		self.trailer_youtube_url = movie_trailer_youtube_url
	
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)