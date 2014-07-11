from artist import Artist

class Actor(Artist):
        def __init__(self, actorId, name):
                """ initialize actor """
                Artist.__init__(self,actorId, name)
                self.gender = 'Male'
