class Artist:
        def __init__(self, artistId, name):
                """ initate artist """
                self.artistId = artistId
                self.artistName = name

        def getArtistId(self):
                return self.artistId

        def getArtistName(self):
                return self.artistName
        
        def getArtistByid(self, artistId, listOfArtists):
                """ get artist by artist id """
                for artist in listOfArtists:
                        if artist.getArtistId() == artistId:
                                return artist
                return None

        def getArtistByName(self, artistName, listOfArtists):
                """ get artist by artist name """
                for artist in listOfArtists:
                        if artist.getArtistName() == artistName:
                                return artist
                return None

        def doesArtistExist(self, artistName, artistsList):
                """ check if artist already exists in list and return artist id if exists """
                for artist in artistsList:
                        if artist.getArtistName() == artistName:
                                return True
                return False
        
        