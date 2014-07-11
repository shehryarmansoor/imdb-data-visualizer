
class ArtistMovieRelation:
        def __init__(self, artistId, movieId):
                self.artistId = artistId
                self.movieId = movieId
                
        def getArtistId(self):
                """ get artist id """
                return self.artistId

        def getMovieId(self):
                """ get movie id """
                return self.movieId

        def getArtistsByMovieId(self, movieId, relationsList):
                """ get all artists of a movie by movie id in relations list"""
                allArtists = []
                for relation in relationsList:
                        if relation.getMovieId() == movieId:
                                allArtists.append(relation.getArtistId())
                return allArtists

        def isArtistStarring(self, artistId, movieId, relationsList, index=0):
                """ check if an artist is starring a movie RECURSIVELY"""
                if index == len(relationsList):
                        return False

                if relationsList[index].getMovieId() == artistId and \
                   relationsList[index].getArtistId() == movieId:
                        return True

                return self.isArtistStarring(artistId, movieId, relationsList, index + 1)

