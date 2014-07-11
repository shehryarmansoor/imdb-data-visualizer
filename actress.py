from artist import Artist

class Actress(Artist):
        def __init__(self, actoressId, name):
                """ initialize actoress """
                Artist.__init__(self,actoressId, name)
                self.gender = 'Female'
