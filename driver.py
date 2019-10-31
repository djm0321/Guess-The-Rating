import pandas as pd

def main():
    file = "movie_metadata.csv"
    movies = pd.read_csv(file)
    movies.drop("id", axis = 1, inplace = True)
    movies.to_csv(file)


main()