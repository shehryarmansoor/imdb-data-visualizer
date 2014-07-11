import sys
from tkinter import *
import random
from actor import Actor
from actress import Actress
from movie import Movie
from artistmovierelation import ArtistMovieRelation


class GUI(Frame):
        
        # class for the GUI
        def __init__(self, parent):
                Frame.__init__(self, parent)
        

                # counters to generate data id's of movies and actors
                self.artistCounter = 0
                self.movieCounter = 0

                # these lists contain objects of type actors, actresses, movies and relations between them
                self.actorsList = []
                self.actressesList = []
                self.moviesList = []
                self.relationsList = []
                self.movieNames = [] # this list stores the movie names that are currently displayed on the visualization
                self.moviesDrawnCount = 0
                self.moviesToLoadEachTime = 20

                # load data from files
                self.fileHandleActors = open('actors.list', 'r')
                self.filePointerActors = 0
                self.filePointerActresses = 0
                self.fileHandleActresses = open('actresses.list', 'r')
                self.loadActors(self.moviesToLoadEachTime)
                self.loadActresses(self.moviesToLoadEachTime)

                # create a GUI
                self.parent = parent
                self.movieDetailsVar = StringVar()
                self.canvas = None
                self.initUI()


        def initUI(self):
                """function to initalize the GUI"""

                # set label of the windowf
                self.parent.title("Movies Visualization using Actors and Actresses")

                # add button for loading more movies
                btn = Button(self, text="Load More Films", command=self.loadMoreMovies)
                btn.pack()

                # drawing ellipses

                self.canvas = Canvas(self, width=830, height=450)


                for i in range(self.moviesDrawnCount, len(self.moviesList)):
                        # generate random x-axis and y-axis for the ellipses
                        x = random.randint(10, 800)
                        y = random.randint(10, 420)

                        # draw ellipses on the circle
                        oval = self.canvas.create_oval(x, y, x + 20, y + 20, outline="gold", fill="black", width=1)

                        # keep a reference of the oval within movie object
                        self.moviesList[i].setOvalId(oval)

                        # to click
                        self.canvas.tag_bind(oval, '<Button-1>', self.onObjectClick)
        
                self.moviesDrawnCount += len(self.moviesList) - self.moviesDrawnCount

                self.canvas.pack(side="top")

                # create a label to diplay movie details
                movieDetailsLabel = Label(self, textvariable=self.movieDetailsVar, justify=LEFT, background="blue", wraplength="830", width="830", height="20", anchor=W, foreground="white")

                movieDetailsLabel.pack(side="left", fill=BOTH, expand=1)

                self.movieDetailsVar.set("Click on any circle to view movie information.\nProgram Created by Rusheel Shahani \n Created for Mr. Seidel, ICS4U \n Version: 1.00, 2014 ")

                # load overall frame
                self.pack(fill=BOTH, expand=1)
                
        def Sort(self,movieList): 
                """function for the bubble sort"""
                
                # bubble sort algorithm
                nums = list(movieList)
                for i in range(len(nums)):
                        
                        for j in range(i+1, len(movieList)):
                                if movieList[j] < movieList[i]:
                                        movieList[j], movieList[i] = movieList[i], movieList[j]
                print ("The sorted list of movies are below:"+ '\n')
                for i in range(len(nums)):
                        print (str(movieList[i]))
                print ('\n' + "Movies that are currently displayed on the visualization are sorted and displayed above.")
                
        def cls(self):
                '''function to clear the screen'''
                
                print ('\n' * 50)
        
        def loadMoreMovies(self):
                """function to load more movies"""
                
                self.loadActors(self.moviesToLoadEachTime)

                self.loadActresses(self.moviesToLoadEachTime)
                

                if self.moviesDrawnCount < len(self.moviesList):
                        
                        for i in range(self.moviesDrawnCount, len(self.moviesList)):
                                
                                titleOfMovie=((Movie.getMovieTitle(self.moviesList[i])))
                                #adds the title of the movie to the movieNames array.
                                self.movieNames.append(titleOfMovie)
                                
                                
                                # generate random x-axis and y-axis for the ellipses
                                
                                x = random.randint(10, 800)

                                y = random.randint(10, 420)

                                # draw ellipses on the circle
                                oval = self.canvas.create_oval(x, y, x + 20, y + 20, outline="gold", fill="black", width=1)
                                
                                # keep a reference of the oval 


                                self.moviesList[i].setOvalId(oval)
                                self.canvas.tag_bind(oval, '<Button-1>', self.onObjectClick)
                        self.cls()
                        
                        self.Sort(self.movieNames)  
        
                        self.moviesDrawnCount += len(self.moviesList) - self.moviesDrawnCount
                        
        def onObjectClick(self, event): 
                """function to get movie details on the movie when clicked."""
                

                tempMovie = Movie(2, 4, "132")
                tempMovie = tempMovie.getMovieByOvalId(event.widget.find_closest(event.x, event.y)[0], self.moviesList)

                # get id's of the artists starring in this movie
                artistmovierelation = ArtistMovieRelation(0,0)
                artistStarring = artistmovierelation.getArtistsByMovieId(tempMovie.getMovieId(), self.relationsList)

                tempActor = Actor("","")
                tempActress = Actress("","")

                # fetches the name of the actor or actress. finds out whether it originated from tbe actor or actress class.

                artistsStartingNames = []
                for artistId in artistStarring:
                        actor = tempActor.getArtistByid(artistId, self.actorsList)
                        if actor != None:
                                artistsStartingNames.append(actor.getArtistName())
                        else:
                                actress = tempActress.getArtistByid(artistId, self.actressesList)
                                if actress != None:
                                        artistsStartingNames.append(actress.getArtistName())

                #  labels to show the film details
                self.movieDetailsVar.set('Title of the Film   : ' + tempMovie.getMovieTitle() + "\n" + "\n" 
                                         "Year Film Released : " + tempMovie.getMovieYear() + "\n"+ "\n" 
                                         "Actor/Actress Name  : " + ", ".join(artistsStartingNames))
        
        
        def loadActors(self, count=100):
                """function to read actors data and create a relationship between actors and movie."""

                actors = self.readArtists("actor", count)
                self.filePointerActors = self.fileHandleActors.tell()

                objActor = Actor("", 0)
                objMovie = Movie("", "", 0)

                for actor in actors:
                        name, title, year = actor
                        
                        # check if actor does not exist else create ID
                        if objActor.getArtistByName(name, self.actorsList) == None:
                                self.artistCounter += 1
                                actorId = self.artistCounter
                                newActor = Actor(actorId, name)
                                self.actorsList.append(newActor)
                                
                                # searches the movie list to check if movies have not been already visualized
                                if not objMovie.doesMovieExist(title, self.moviesList) and \
                                   objMovie.getMovieByName(title, self.moviesList) == None:
                                        self.movieCounter += 1
                                        movieId = self.movieCounter
                                        movie = Movie(movieId, title, year)
                                        self.moviesList.append(movie)

                                        # create relation between actor and  movie
                                        relation = ArtistMovieRelation(actorId, movieId)
                                        self.relationsList.append(relation)

        def loadActresses(self, count=100):	
                """function to read actresses data and create a relationship between actress and movie,"""

                # read actresses from file
                actresses = self.readArtists("actress", count)
                self.filePointerActresses = self.fileHandleActresses.tell()
                objActress = Actress("", 0)
                objMovie = Movie("", "", 0)

                for actress in actresses:
                        name, title, year = actress
                        actress = objActress.getArtistByName(name, self.actressesList)

                        # check if actress already not exist then add it
                        if actress == None:
                                self.artistCounter += 1
                                actressId = self.artistCounter
                                newActress = Actress(actressId, name)
                                self.actressesList.append(newActress)
                        else:
                                actressId = actress.getArtistId()

                        # check if movie already exists. only if the movie doesn't exist, it will create an ID and 
                        if not objMovie.doesMovieExist(title, self.moviesList) and \
                           objMovie.getMovieByName(title, self.moviesList) == None:
                                self.movieCounter += 1
                                movieId = self.movieCounter
                                movie = Movie(movieId, title, year)
                                self.moviesList.append(movie)

                                # create relation between actor and  movie
                                relation = ArtistMovieRelation(actressId, movieId)

                                self.relationsList.append(relation)

        def readArtists(self, artistType, linesToRead):
                """function to read artists."""
                
                artists = []
                currentName = None
                readArtist = False
                linesCount = 0
                isReadingFromBegining = False

                while linesCount < linesToRead:
                        if artistType == "actor":
                                line = self.fileHandleActors.readline()
                                if self.filePointerActors == 0:
                                        isReadingFromBegining = True
                                else:
                                        isReadingFromBegining = False
                        else:
                                line = self.fileHandleActresses.readline()
                                if self.filePointerActresses == 0:
                                        isReadingFromBegining = True
                                else:
                                        isReadingFromBegining = False

                        # if file ends then return with the artists
                        if line == '':
                                return artists

                        if isReadingFromBegining == True:
                                # skip all the lines not having artists data
                                if not line.startswith("----			------") and readArtist == False:
                                        continue
                                else:
                                        if readArtist == False:
                                                readArtist = True
                                                continue

                        # if line does not have tab then it is not have any data
                        if '\t' not in line:
                                continue

                        title = ""
                        year = ""
                        name = ""
                        if not line.startswith("\t"):
                                arrStr = line.split('\t', 1)
                                name = arrStr[0].strip()
                                otherStr = arrStr[1].strip()
                                title = otherStr[:otherStr.find('(')].strip()
                                year = otherStr[otherStr.find('(') + 1 : otherStr.find(')')].strip()
                        else:
                                continue

                        if name != "":
                                if ',' in name:
                                        name = name.split(',', 1)
                                        name[0] = name[0].rstrip()
                                        name[1] = name[1].lstrip()
                                        name.reverse()
                                        name = ' '.join(name)
                                artists += [[name, title, year]]

                                linesCount += 1

                return artists

def main():
        # create a window using tkinter
        root = Tk()

        # load GUI with all movies and details
        ex = GUI(root)

        # set window size and start position
        root.geometry("830x620+100+100")

        root.mainloop()  

if __name__ == '__main__':
        # Call the main function
        main()
