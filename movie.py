import sys
sys.setrecursionlimit(15000000)

class Movie:
	def __init__(self, id, title, year):
		""" iniate movie """
		self.movieId = id
		self.movieTitle = title
		self.movieYear = year
		self.ovalId = ""
		
	def getMovieId(self):
		""" return id of current movie """
		return self.movieId
		
	def getMovieTitle(self):
		""" return title of current movie """
		return self.movieTitle
		
	def getMovieYear(self):
		""" return year of current movie """
		return self.movieYear
	
	def setOvalId(self, ovalId):
		""" set oval shape object id """
		self.ovalId = ovalId
		
	def getOvalId(self):
		""" return oval shape object id """
		return self.ovalId

	def getMovieById(self, movieId, listOfMovies):
		""" get movie by movie id """
		for movie in listOfMovies:
			if movie.getMovieId() == movieId:
				return movie
		return None
	
	def getMovieByOvalId(self, ovalId, listOfMovies):
		""" get movie by oval id """
		for movie in listOfMovies:
			if movie.getOvalId() == ovalId:
				return movie
		return None

	def getMovieByName(self, movieTitle, listOfMovies):
		for movie in listOfMovies:
			if movie.getMovieTitle() == movieTitle:
				return movie
		return None

	def doesMovieExist(self, movieTitle, moviesList, index=0):
		""" SEARCHES the movie list to check if movie already exists in list, RECURSIVELY."""
		if index == len(moviesList):
			return False
		if moviesList[index].getMovieTitle() == movieTitle:
			return True
		return self.doesMovieExist(movieTitle, moviesList, index + 1)
	