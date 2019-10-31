import pandas as pd

def main():
    file = "movie_metadata.csv"
    movies = pd.read_csv(file)
    movies.to_csv(file)


main()