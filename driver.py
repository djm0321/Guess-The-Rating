import pandas as pd
import random
import gameFunctions

def main():
    score1 = 0
    score2 = 0
    scores = [0, 0]
    keepPlaying = True
    movies = gameFunctions.openFile()
    while keepPlaying:
        randMovie = gameFunctions.randomMovie(movies)
        print(str(movies.values[randMovie][11]) + ", " + str(movies.values[randMovie][25]))
        gameFunctions.guess(movies, randMovie, scores)
        print(scores)
        keepPlaying = gameFunctions.playAgain()
    
    
     
main()